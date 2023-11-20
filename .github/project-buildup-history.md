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
## 2023-09-25 - Day 5: Frontend form

- Task summary: Built the simple HTML form for the salary estimation app today. Kept it deliberately minimal — a single-page form with labelled fields, a submit button, and a result div that gets populated via a fetch call to the prediction endpoint. No external dependencies, just plain HTML and a small inline script. Tested the full round trip from form submission to prediction result display.
- Deliverable: HTML form built. Full round-trip tested and working.
## 2023-11-20 - Day 6: Testing

- Task summary: Added a proper test suite for the Salary Estimation Flask app today. Wrote tests for the happy path prediction, missing required field, out-of-range input, and the model metadata endpoint. Used pytest with the Flask test client. Coverage report showed all critical paths were covered. Also added a CI configuration file so the tests run on push.
- Deliverable: Pytest suite written. All critical paths covered. CI config added.
## 2023-11-20 - Day 6: Testing

- Task summary: One of the tests was failing intermittently due to a floating point comparison with no tolerance. Fixed to use pytest.approx.
- Deliverable: Floating point test fixed with pytest.approx.
