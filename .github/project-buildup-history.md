# Project Buildup History: Salary Estimation Flask App

- Repository: `salary-estimation-flask-app`
- Category: `flask_ml_app`
- Subtype: `prediction`
- Source: `project_buildup_2021_2025_daily_plan.csv`
## 2022-04-13 - Day 1: Problem framing start

- Task summary: Started this one by sitting down and trying to understand what Salary Estimation Flask App should actually become. I did not rush into code yet. The main thing here was to write down the input fields, target output, and intended user for Salary Estimation Flask App so the project had a decent base. At this stage nothing was fully locked, so I kept a rough list of things that looked useful and ignored the rest for now. Part of the effort went into making sure a normal person could use the page without needing extra explanation.
- Deliverable: By the end of the day I had problem statement written down in a rough way, which was enough to stop guessing and move into the next step. It was not super polished, just stable enough that I felt okay moving forward.
## 2022-04-14 - Day 2: Dataset setup pass

- Task summary: Used the next day to keep the momentum going for Salary Estimation Flask App. I was still piecing things together, so I focused on trying to collect the raw dataset and create a notebook to inspect the fields and target variable and wrote down the stuff that looked important. This was still the messy setup part where I was opening files, checking examples, and trying not to overthink it too early. The code was not huge, but getting the flow to feel simple took more fiddling than expected.
- Deliverable: I wrapped up the day with starter notebook mostly in place. It was not perfect, but it was good enough to keep the project moving. I also left myself a few rough reminders for the next day so I would not have to rediscover the same context again.
## 2022-04-15 - Day 3: Cleaning pass

- Task summary: By this point I had the rough direction, so the work became more practical. I spent most of the day trying to handle missing values, bad rows, and obvious outliers so the data is usable and make the whole thing feel less half baked. Once the base made some sense, I could finally move a bit faster and stop second guessing every tiny decision. I had to think about both the model side and the form side at the same time, which made the day a bit scattered.
- Deliverable: I wrapped up the day with cleaned dataset mostly in place. It was not perfect, but it was good enough to keep the project moving. There were still a couple of loose parts, but nothing serious enough to block the next step.
## 2022-04-17 - Day 3: Cleaning pass

- Task summary: Weekend fix — the visualizations had overlapping labels in narrow viewports. Adjusted the figure size and padding.
- Deliverable: Good enough to not be embarrassing.
## 2022-04-18 - Day 4: EDA

- Task summary: By this point I had the rough direction, so the work became more practical. I spent most of the day trying to chart the strongest relationships and note which inputs appear predictive and make the whole thing feel less half baked. The middle part always takes longer than it should, mostly becuase one fix usually reveals two more things to clean up. Part of the effort went into making sure a normal person could use the page without needing extra explanation.
- Deliverable: I wrapped up the day with eDA notes and charts mostly in place. It was not perfect, but it was good enough to keep the project moving. It was not super polished, just stable enough that I felt okay moving forward.
## 2022-04-19 - Day 5: Feature prep

- Task summary: By this point I had the rough direction, so the work became more practical. I spent most of the day trying to choose the final features, encodings, and train/test split strategy and make the whole thing feel less half baked. By now I had enough structure to keep going without staring at the screen too long, which honestly helped a lot. The code was not huge, but getting the flow to feel simple took more fiddling than expected.
- Deliverable: I wrapped up the day with feature set mostly in place. It was not perfect, but it was good enough to keep the project moving. I also left myself a few rough reminders for the next day so I would not have to rediscover the same context again.
## 2022-04-20 - Day 6: Baseline model

- Task summary: By this point I had the rough direction, so the work became more practical. I spent most of the day trying to train a first model and record the basic evaluation metrics and make the whole thing feel less half baked. Once the base made some sense, I could finally move a bit faster and stop second guessing every tiny decision. I had to think about both the model side and the form side at the same time, which made the day a bit scattered.
- Deliverable: I wrapped up the day with baseline results mostly in place. It was not perfect, but it was good enough to keep the project moving. There were still a couple of loose parts, but nothing serious enough to block the next step.
## 2022-04-21 - Day 7: Model improvement

- Task summary: By this point I had the rough direction, so the work became more practical. I spent most of the day trying to try a better algorithm or tune the model to improve the score responsibly and make the whole thing feel less half baked. The middle part always takes longer than it should, mostly becuase one fix usually reveals two more things to clean up. Part of the effort went into making sure a normal person could use the page without needing extra explanation.
- Deliverable: I wrapped up the day with improved model mostly in place. It was not perfect, but it was good enough to keep the project moving. It was not super polished, just stable enough that I felt okay moving forward.
## 2022-04-21 - Day 7: Model improvement

- Task summary: Got stuck mid-afternoon and had to regroup — ran the whole thing end to end again after a fresh look. Caught a stale import that broke the flow.
- Deliverable: Should've caught it earlier but better now than later.
## 2022-04-21 - Day 7: Model improvement

- Task summary: Ended up revisiting this in the evening — resolved a merge conflict that came up when I switched branches to check something else.
- Deliverable: Pushed before end of day.
## 2022-04-22 - Day 8: Model export

- Task summary: This was the middle stretch where the project started feeling real. I kept going and tried to save the trained model and any preprocessing objects so the web app can reuse them, then cleaned up whatever looked confusing or weak from the earlier days. By now I had enough structure to keep going without staring at the screen too long, which honestly helped a lot. The code was not huge, but getting the flow to feel simple took more fiddling than expected.
- Deliverable: Ended the day with serialized model files in hand, plus a few side notes on what still needed fixing later. I also left myself a few rough reminders for the next day so I would not have to rediscover the same context again.
## 2022-04-25 - Day 9: Flask scaffold

- Task summary: This was the middle stretch where the project started feeling real. I kept going and tried to set up the Flask app structure, routes, templates, and form submission flow, then cleaned up whatever looked confusing or weak from the earlier days. Once the base made some sense, I could finally move a bit faster and stop second guessing every tiny decision. I had to think about both the model side and the form side at the same time, which made the day a bit scattered.
- Deliverable: Ended the day with running Flask app in hand, plus a few side notes on what still needed fixing later. There were still a couple of loose parts, but nothing serious enough to block the next step.
## 2022-04-25 - Day 9: Flask scaffold

- Task summary: Noticed something off from this morning — added a sanity check assertion that would catch obvious data shape issues early.
- Deliverable: Minor but worth doing.
## 2022-04-25 - Day 9: Flask scaffold

- Task summary: Late-night fix: added one more evaluation metric that felt missing from the earlier comparison.
- Deliverable: Good enough to not be embarrassing.
## 2022-04-25 - Day 9: Flask scaffold

- Task summary: Late-night fix: pushed a tiny fix after a teammate's comment — nothing major, just a wording issue in the output.
- Deliverable: Should've caught it earlier but better now than later.
## 2022-04-26 - Day 10: Prediction wiring

- Task summary: This was the middle stretch where the project started feeling real. I kept going and tried to connect form inputs to the model and show prediction results on the page, then cleaned up whatever looked confusing or weak from the earlier days. The middle part always takes longer than it should, mostly becuase one fix usually reveals two more things to clean up. Part of the effort went into making sure a normal person could use the page without needing extra explanation.
- Deliverable: Ended the day with end-to-end prediction flow in hand, plus a few side notes on what still needed fixing later. It was not super polished, just stable enough that I felt okay moving forward.
## 2022-04-27 - Day 11: Validation

- Task summary: This was the middle stretch where the project started feeling real. I kept going and tried to add input validation and user-friendly error messages for bad or missing values, then cleaned up whatever looked confusing or weak from the earlier days. By now I had enough structure to keep going without staring at the screen too long, which honestly helped a lot. The code was not huge, but getting the flow to feel simple took more fiddling than expected.
- Deliverable: Ended the day with safer form handling in hand, plus a few side notes on what still needed fixing later. I also left myself a few rough reminders for the next day so I would not have to rediscover the same context again.
## 2022-04-27 - Day 11: Validation

- Task summary: Ended up revisiting this in the evening — re-ran the plots with better axis labels and a more readable color palette.
- Deliverable: Solid now, moving on.
## 2022-04-28 - Day 12: UI styling

- Task summary: Closer to the end, I was mostly tightening things up instead of inventing new scope. The job for the day was to make the app readable and clean enough for a normal user to understand quickly so the final result looked a bit more complete. Once the base made some sense, I could finally move a bit faster and stop second guessing every tiny decision. I had to think about both the model side and the form side at the same time, which made the day a bit scattered.
- Deliverable: Ended the day with styled interface in hand, plus a few side notes on what still needed fixing later. There were still a couple of loose parts, but nothing serious enough to block the next step.
