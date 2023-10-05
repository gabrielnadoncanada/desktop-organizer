import os
import shutil
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Set the base folder path
base_path = "C:\\laragon\\www\\desktop-organizer\\training-ground"

# Define the categories you want to classify files into
categories = ['Documents', 'Images', 'Music', 'Videos', 'Apps']

# Dummy feature extraction function
def extract_features(file_path):
    # This is a dummy feature extraction function.
    # Replace this with actual feature extraction code for your specific file types.
    return [ord(c) for c in file_path[-10:]]

# Create a dataset with features and labels
data = []
labels = []

for category in categories:
    folder_path = os.path.join(base_path, category)
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        features = extract_features(file_path)
        data.append(features)
        labels.append(category)

if not data:
    print("No data found in the specified folder. Please check the folder path and contents.")
    exit()
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Train a classifier (e.g., Random Forest)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluate the classifier
score = clf.score(X_test, y_test)
print("Classifier accuracy:", score)

# Save the trained model to a file
with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)

# Define a function to update the training data with corrected classifications
def update_training_data(file_path, correct_category):
    features = extract_features(file_path)
    data.append(features)
    labels.append(correct_category)

    # Retrain the model with the updated dataset
    clf.fit(data, labels)

    # Save the updated model to a file
    with open("model.pkl", "wb") as f:
        pickle.dump(clf, f)
