<<<<<<< HEAD
from sklearn.dummy import DummyClassifier
import numpy as np
import joblib

# Create a dummy classifier model (always predicts the most frequent class)
dummy = DummyClassifier(strategy="most_frequent")

# Minimal example data (5 features, 1 sample)
X = np.zeros((1, 5))
y = [0]

dummy.fit(X, y)

# Save the model as 'illegal_occupation_model.pkl' in the models directory
joblib.dump(dummy, "illegal_occupation_model.pkl")

=======
from sklearn.dummy import DummyClassifier
import numpy as np
import joblib

# Create a dummy classifier model (always predicts the most frequent class)
dummy = DummyClassifier(strategy="most_frequent")

# Minimal example data (5 features, 1 sample)
X = np.zeros((1, 5))
y = [0]

dummy.fit(X, y)

# Save the model as 'illegal_occupation_model.pkl' in the models directory
joblib.dump(dummy, "illegal_occupation_model.pkl")

>>>>>>> 900cbc7 (Updated features and modified app.py and modules)
print("Dummy model saved as illegal_occupation_model.pkl in the models directory.")