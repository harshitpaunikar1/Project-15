# Project Buildup History: Salary Estimation Flask App

- Repository: `salary-estimation-flask-app`
- Category: `flask_ml_app`
- Subtype: `prediction`
- Source: `project_buildup_2021_2025_daily_plan_extra.csv`
## 2023-09-18 - Day 4: Model integration

- Task summary: Spent today integrating the trained salary estimation model into the Flask app properly. The serialization had been done with a different version of scikit-learn than what was in the requirements file, which was causing a loading error in the environment. Retrained the model in the correct environment and re-serialized. Also verified that the prediction output matched what the notebook produced for the same inputs — it did after the retraining.
- Deliverable: Model retrained in consistent environment. Serialization/loading issue resolved.
## 2023-09-18 - Day 4: Model integration

- Task summary: Added a model metadata endpoint that returns the training date, feature names expected, and model type. Useful for debugging deployment issues without digging into code.
- Deliverable: Model metadata endpoint added at /model/info.
## 2023-09-18 - Day 4: Model integration

- Task summary: The numerical encoding for job title categories was done at training time but the Flask app was not applying the same encoding map at inference time — they diverged. Fixed by saving the encoder alongside the model and loading both.
- Deliverable: Category encoder now saved and loaded alongside model. Encoding consistency ensured.
