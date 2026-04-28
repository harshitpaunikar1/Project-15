"""
Training script for the salary estimation model.
Predicts salary based on test score, interview score, and other candidate features.
"""
import os
import pickle
import warnings
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

try:
    from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
    from sklearn.linear_model import LinearRegression, Ridge, Lasso
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    from sklearn.model_selection import KFold, cross_val_score, train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder, StandardScaler, PolynomialFeatures
    from sklearn.compose import ColumnTransformer
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False


class SalaryFeatureEngineer:
    """Engineers features for salary prediction from candidate data."""

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        if "test_score" in df.columns and "interview_score" in df.columns:
            df["combined_score"] = df["test_score"] * 0.4 + df["interview_score"] * 0.6
        if "experience_years" in df.columns:
            df["log_experience"] = np.log1p(df["experience_years"])
            df["experience_band"] = pd.cut(
                df["experience_years"],
                bins=[0, 2, 5, 10, 20, float("inf")],
                labels=["entry", "junior", "mid", "senior", "expert"],
            ).astype(str)
        if "test_score" in df.columns:
            df["test_percentile"] = df["test_score"].rank(pct=True)
        if "interview_score" in df.columns:
            df["interview_percentile"] = df["interview_score"].rank(pct=True)
        return df


class SalaryEstimationModel:
    """
    Multi-model salary predictor with cross-validation and feature importance.
    """

    def __init__(self, numeric_features: List[str], categorical_features: List[str],
                 target_col: str = "salary"):
        self.numeric_features = numeric_features
        self.categorical_features = categorical_features
        self.target_col = target_col
        self.engineer = SalaryFeatureEngineer()
        self.models: Dict[str, Pipeline] = {}
        self.results: List[Dict] = []
        self.best_model_name: Optional[str] = None

    def _preprocessor(self):
        transformers = []
        if self.numeric_features:
            transformers.append(("num", StandardScaler(), self.numeric_features))
        if self.categorical_features:
            transformers.append(("cat", OneHotEncoder(handle_unknown="ignore",
                                                        sparse_output=False),
                                  self.categorical_features))
        return ColumnTransformer(transformers=transformers, remainder="drop")

    def _estimators(self) -> Dict:
        return {
            "LinearRegression": LinearRegression(),
            "Ridge": Ridge(alpha=10.0),
            "Lasso": Lasso(alpha=1.0, max_iter=3000),
            "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1),
            "GradientBoosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.05,
                                                           max_depth=4, random_state=42),
        }

    def mape(self, actual: np.ndarray, predicted: np.ndarray) -> float:
        mask = actual != 0
        return float(np.mean(np.abs((actual[mask] - predicted[mask]) / actual[mask])) * 100)

    def fit(self, df: pd.DataFrame, test_size: float = 0.2) -> pd.DataFrame:
        if not SKLEARN_AVAILABLE:
            raise RuntimeError("scikit-learn required.")
        df = self.engineer.transform(df)
        num_cols = [c for c in self.numeric_features if c in df.columns]
        cat_cols = [c for c in self.categorical_features if c in df.columns]
        df_clean = df[num_cols + cat_cols + [self.target_col]].dropna(subset=[self.target_col])
        for col in num_cols:
            df_clean[col] = df_clean[col].fillna(df_clean[col].median())
        for col in cat_cols:
            df_clean[col] = df_clean[col].fillna("unknown")

        X = df_clean[num_cols + cat_cols]
        y = df_clean[self.target_col]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )

        prep = self._preprocessor()
        self.results = []
        for name, est in self._estimators().items():
            pipe = Pipeline([("preprocessor", prep), ("model", est)])
            pipe.fit(X_train, y_train)
            preds = pipe.predict(X_test)
            rmse = float(np.sqrt(mean_squared_error(y_test, preds)))
            mae = float(mean_absolute_error(y_test, preds))
            r2 = float(r2_score(y_test, preds))
            mape_val = self.mape(y_test.values, preds)
            cv_scores = cross_val_score(pipe, X, y, cv=5, scoring="neg_mean_absolute_error")
            cv_mae = float(-cv_scores.mean())
            self.models[name] = pipe
            self.results.append({
                "model": name,
                "rmse": round(rmse, 0),
                "mae": round(mae, 0),
                "r2": round(r2, 4),
                "mape_pct": round(mape_val, 2),
                "cv_mae": round(cv_mae, 0),
            })

        results_df = pd.DataFrame(self.results).sort_values("mae").reset_index(drop=True)
        self.best_model_name = results_df.iloc[0]["model"]
        return results_df

    def predict(self, df: pd.DataFrame) -> np.ndarray:
        if self.best_model_name not in self.models:
            raise RuntimeError("Call fit() first.")
        df = self.engineer.transform(df)
        num_cols = [c for c in self.numeric_features if c in df.columns]
        cat_cols = [c for c in self.categorical_features if c in df.columns]
        return np.round(self.models[self.best_model_name].predict(df[num_cols + cat_cols]), 0)

    def salary_band(self, salary: float) -> str:
        if salary < 300000:
            return "entry_level"
        if salary < 600000:
            return "mid_level"
        if salary < 1200000:
            return "senior_level"
        return "executive"

    def save_model(self, path: str = "model.pkl") -> None:
        if self.best_model_name not in self.models:
            raise RuntimeError("No model to save.")
        with open(path, "wb") as f:
            pickle.dump(self.models[self.best_model_name], f)
        print(f"Model saved to {path}")

    def feature_importance(self) -> Optional[pd.DataFrame]:
        if self.best_model_name not in self.models:
            return None
        pipe = self.models[self.best_model_name]
        est = pipe.named_steps["model"]
        if not hasattr(est, "feature_importances_"):
            if hasattr(est, "coef_"):
                imp = np.abs(est.coef_)
            else:
                return None
        else:
            imp = est.feature_importances_
        prep = pipe.named_steps["preprocessor"]
        try:
            cat_names = list(prep.named_transformers_["cat"].get_feature_names_out(
                self.categorical_features))
        except Exception:
            cat_names = []
        names = self.numeric_features + cat_names
        return pd.DataFrame({"feature": names[:len(imp)], "importance": imp}).sort_values(
            "importance", ascending=False
        ).head(10).reset_index(drop=True)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    df = pd.DataFrame({
        "test_score": np.random.uniform(0, 10, n),
        "interview_score": np.random.uniform(0, 10, n),
        "experience_years": np.random.uniform(0, 20, n),
    })
    noise = np.random.normal(0, 30000, n)
    df["salary"] = (
        200000
        + df["test_score"] * 15000
        + df["interview_score"] * 25000
        + df["experience_years"] * 20000
        + noise
    ).clip(100000)

    model = SalaryEstimationModel(
        numeric_features=["test_score", "interview_score", "experience_years"],
        categorical_features=[],
    )

    results = model.fit(df)
    print("Model comparison:")
    print(results.to_string(index=False))
    print(f"\nBest model: {model.best_model_name}")

    sample_data = pd.DataFrame({
        "test_score": [8.5, 6.0, 4.0, 9.2, 3.5],
        "interview_score": [9.0, 7.5, 5.5, 8.0, 4.0],
        "experience_years": [5.0, 3.0, 1.0, 10.0, 0.5],
    })
    preds = model.predict(sample_data)
    print("\nSample predictions:")
    for i, (_, row) in enumerate(sample_data.iterrows()):
        band = model.salary_band(preds[i])
        print(f"  Test={row['test_score']:.1f} Interview={row['interview_score']:.1f} "
              f"Exp={row['experience_years']:.0f}y -> Rs {preds[i]:,.0f} ({band})")

    fi = model.feature_importance()
    if fi is not None:
        print("\nFeature importance:")
        print(fi.to_string(index=False))

    model.save_model("salary_model.pkl")
