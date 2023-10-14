import gradio as gr
import numpy as np
import pandas as pd
import joblib
from xgboost import XGBClassifier


username = "mohansathya"
repo_name = "heartdisease"
save_file_name = "xgboost-model.pkl"
repo_path = username+ '/' + repo_name + '/' + save_file_name

xgb_loaded = joblib.load(save_file_name)

def predict_death_event_basic(sample):
    result = xgb_loaded.predict(sample)
    return result

def predict_death_event(age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time):
    try:
      result = predict_death_event_basic([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]]) 
      print('age ', age, 'anaemia ', anaemia, 'creatinine_phosphokinase ', creatinine_phosphokinase, 'diabetes ', diabetes, 'ejection_fraction ', ejection_fraction, 'high_blood_pressure ', high_blood_pressure, 'platelets ', platelets, 'serum_creatinine ', serum_creatinine, 'serum_sodium ', serum_sodium, 'sex ', sex, 'smoking ', smoking, 'time ', time)
    except:
      return 'age ', age, 'anaemia ', anaemia, 'creatinine_phosphokinase ', creatinine_phosphokinase, 'diabetes ', diabetes, 'ejection_fraction ', ejection_fraction, 'high_blood_pressure ', high_blood_pressure, 'platelets ', platelets, 'serum_creatinine ', serum_creatinine, 'serum_sodium ', serum_sodium, 'sex ', sex, 'smoking ', smoking, 'time ', time
    return result
    

demo = gr.Interface(
    predict_death_event,
    [
        gr.Slider(40, 100, value=60, label="age", info="Choose between 40 and 100"),
        gr.Radio(
            ["No", "Yes"], type = 'index', value='Yes', label="anaemia", info="is anemic"
        ),
        gr.Slider(23, 1300, value=588, label="creatinine_phosphokinase", info="Choose between 23 and 1300"),
        gr.Radio(
            ["No", "Yes"], type = 'index', value='Yes', label="diabetes", info="is diabetic"
        ),
        gr.Slider(14, 70, value=60, label="ejection_fraction", info="Choose between 14 and 70"),
        gr.Radio(
            ["No", "Yes"], type = 'index', value='No', label="high_blood_pressure", info="is hypertensive"
        ),
        gr.Slider(70000, 450000, value=194000, label="platelets", info="Choose between 70000 and 450000"),
        gr.Slider(0.5, 2.2, value=194000, label="serum_creatinine", info="Choose between 0.5 and 2.2"),
        gr.Slider(120, 150, value=142, label="serum_sodium", info="Choose between 120 and 150"),
        gr.Radio(
            ["No", "Yes"], type = 'index', value='No', label="Is woman", info="is woman"
        ),
        gr.Radio(
            ["No", "Yes"], type = 'index', value='No', label="Is a smoker?", info="is smoker?"
        ),
        gr.Slider(1, 300, value=33, label="follow-up period", info="Choose between 1 and 300 days")
    ],
    "text",
    examples=[
        [6.00e+01, 'Yes', 5.88e+02, 'Yes', 6.00e+01, 'No',
       1.94e+05, 1.10e+00, 1.42e+02, 'No', 'No', 3.30e+01],
        [5.30e+01, 'Yes', 2.70e+02, 'Yes', 3.50e+01, 'No',
       2.27e+05, 2.15e+00, 1.45e+02, 'Yes', 'No', 1.05e+02]
    ]
)

demo.launch(debug = True, server_port=8001, server_name="0.0.0.0")
