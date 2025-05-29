<<<<<<< HEAD
import joblib
import os

os.makedirs("models", exist_ok=True)
dummy_model = {"dummy": True}
for i in range(1, 36):
    joblib.dump(dummy_model, f"models/model_{i}.pkl")
=======
import joblib
import os

os.makedirs("models", exist_ok=True)
dummy_model = {"dummy": True}
for i in range(1, 36):
    joblib.dump(dummy_model, f"models/model_{i}.pkl")
>>>>>>> 900cbc7 (Updated features and modified app.py and modules)
print("Dummy models created!")