import os
import shutil
import pickle

# Set the testing folder path
testing_path = "C:\\laragon\\www\\desktop-organizer\\training-ground"

# Dummy feature extraction function
def extract_features(file_path):
    # This is a dummy feature extraction function.
    # Replace this with actual feature extraction code for your specific file types.
    return [ord(c) for c in file_path[-10:]]

# Load the trained model from the file
with open("model.pkl", "rb") as f:
    clf = pickle.load(f)

def process_file(file_path):
    features = extract_features(file_path)
    prediction = clf.predict([features])[0]
    return prediction

# Test the classifier on the files in the testing folder
for root, dirs, files in os.walk(testing_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        prediction = process_file(file_path)

        print(f"Predicted category for '{file_name}': {prediction}")

        # Check if the file is in the wrong folder
        current_folder = os.path.basename(root)
        if current_folder != prediction:
            # Move the file to the appropriate folder within the testing folder (optional)
            destination_folder = os.path.join(testing_path, prediction)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            shutil.move(file_path, os.path.join(destination_folder, file_name))
