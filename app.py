"""
Main application file to run all 35 River AI Features with AI model loading support.

Assumptions:
- Each feature (feature_1 to feature_35) is implemented in modules/feature_X.py and imported here.
- Required AI model files exist under a 'models/' directory.
- Uses Flask for API endpoints (one per feature).
- Replace dummy model loading and processing with your actual AI model and logic as needed.
"""

from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import joblib

# --- Feature Imports (modules folder) ---
from modules.feature_1 import feature_1_func
from modules.feature_2 import feature_2_func
from modules.feature_3 import feature_3_func
from modules.feature_4 import feature_4_func
from modules.feature_5 import feature_5_func
from modules.feature_6 import feature_6_func
from modules.feature_7 import feature_7_func
from modules.feature_8 import feature_8_func
from modules.feature_9 import feature_9_func
from modules.feature_10 import feature_10_func
from modules.feature_11 import feature_11_func
from modules.feature_12 import feature_12_func
from modules.feature_13 import feature_13_func
from modules.feature_14 import feature_14_func
from modules.feature_15 import feature_15_func
from modules.feature_16 import feature_16_func
from modules.feature_17 import feature_17_func
from modules.feature_18 import feature_18_func
from modules.feature_19 import feature_19_func
from modules.feature_20 import feature_20_func
from modules.feature_21 import feature_21_func
from modules.feature_22 import feature_22_func
from modules.feature_23 import feature_23_func
from modules.feature_24 import feature_24_func
from modules.feature_25 import feature_25_func
from modules.feature_26 import feature_26_func
from modules.feature_27 import feature_27_func
from modules.feature_28 import feature_28_func
from modules.feature_29 import feature_29_func
from modules.feature_30 import feature_30_func
from modules.feature_31 import feature_31_func
from modules.feature_32 import feature_32_func
from modules.feature_33 import feature_33_func
from modules.feature_34 import feature_34_func
from modules.feature_35 import feature_35_func

# --- AI Model Loader ---
def load_ai_model(path: str):
    """Load an AI model from disk using joblib. Adjust as per your model type."""
    try:
        model = joblib.load(path)
        print(f"Loaded model: {path}")
        return model
    except Exception as e:
        print(f"Model load failed ({path}): {e}")
        return None

# --- Model Loading (adjust/add as per your features) ---
model_1 = load_ai_model("models/model_1.pkl")
model_2 = load_ai_model("models/model_2.pkl")
model_3 = load_ai_model("models/model_3.pkl")
model_4 = load_ai_model("models/model_4.pkl")
model_5 = load_ai_model("models/model_5.pkl")
model_6 = load_ai_model("models/model_6.pkl")
model_7 = load_ai_model("models/model_7.pkl")
model_8 = load_ai_model("models/model_8.pkl")
model_9 = load_ai_model("models/model_9.pkl")
model_10 = load_ai_model("models/model_10.pkl")
model_11 = load_ai_model("models/model_11.pkl")
model_12 = load_ai_model("models/model_12.pkl")
model_13 = load_ai_model("models/model_13.pkl")
model_14 = load_ai_model("models/model_14.pkl")
model_15 = load_ai_model("models/model_15.pkl")
model_16 = load_ai_model("models/model_16.pkl")
model_17 = load_ai_model("models/model_17.pkl")
model_18 = load_ai_model("models/model_18.pkl")
model_19 = load_ai_model("models/model_19.pkl")
model_20 = load_ai_model("models/model_20.pkl")
model_21 = load_ai_model("models/model_21.pkl")
model_22 = load_ai_model("models/model_22.pkl")
model_23 = load_ai_model("models/model_23.pkl")
model_24 = load_ai_model("models/model_24.pkl")
model_25 = load_ai_model("models/model_25.pkl")
model_26 = load_ai_model("models/model_26.pkl")
model_27 = load_ai_model("models/model_27.pkl")
model_28 = load_ai_model("models/model_28.pkl")
model_29 = load_ai_model("models/model_29.pkl")
model_30 = load_ai_model("models/model_30.pkl")
model_31 = load_ai_model("models/model_31.pkl")
model_32 = load_ai_model("models/model_32.pkl")
model_33 = load_ai_model("models/model_33.pkl")
model_34 = load_ai_model("models/model_34.pkl")
model_35 = load_ai_model("models/model_35.pkl")

models = [
    model_1, model_2, model_3, model_4, model_5, model_6, model_7, model_8, model_9, model_10,
    model_11, model_12, model_13, model_14, model_15, model_16, model_17, model_18, model_19, model_20,
    model_21, model_22, model_23, model_24, model_25, model_26, model_27, model_28, model_29, model_30,
    model_31, model_32, model_33, model_34, model_35
]

# --- Flask App ---
app = Flask(__name__)

@app.route("/")
def index():
    return "River AI Features API (35 features loaded)"

# --- 35 Feature Endpoints ---
@app.route("/feature/<int:feature_id>", methods=["POST"])
def run_feature(feature_id):
    if not (1 <= feature_id <= 35):
        return jsonify({"error": "Invalid feature_id"}), 404

    func = [
        feature_1_func, feature_2_func, feature_3_func, feature_4_func, feature_5_func,
        feature_6_func, feature_7_func, feature_8_func, feature_9_func, feature_10_func,
        feature_11_func, feature_12_func, feature_13_func, feature_14_func, feature_15_func,
        feature_16_func, feature_17_func, feature_18_func, feature_19_func, feature_20_func,
        feature_21_func, feature_22_func, feature_23_func, feature_24_func, feature_25_func,
        feature_26_func, feature_27_func, feature_28_func, feature_29_func, feature_30_func,
        feature_31_func, feature_32_func, feature_33_func, feature_34_func, feature_35_func
    ][feature_id - 1]
    model = models[feature_id - 1]

    # Example: Pass model and json to function if required. Adjust as per your real function signature.
    try:
        # You may want to customize input parsing for each feature.
        data = request.json if request.is_json else {}
        result = func(data, model)  # Adjust as per your function signature
        # If result is not serializable, convert accordingly
        if isinstance(result, pd.DataFrame):
            return result.to_json()
        elif isinstance(result, np.ndarray):
            return jsonify(result.tolist())
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Use debug=False and use_reloader=False to avoid signal/threading errors in all environments
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
  


    
        
=======
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
>>>>>>> 900cbc7 (Updated features and modified app.py and modules)
