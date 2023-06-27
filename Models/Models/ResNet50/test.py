import numpy as np
import datetime
import Utility.general as GeneralUtils
import Utility.resnet50_utility as ResNet50Utils

from timeit import default_timer as timer

MODEL_WEIGHTS = '../../Tmp/ResNet50/resnet50_latest_10movies.hdf5'

TEST_DATASET = ResNet50Utils.create_test_dataset()
MOVIES_LIST = GeneralUtils.get_movies_list()
TEST_MOVIES_CSV = GeneralUtils.get_test_csv()

print("Creating InceptionV3 Model...")
model = ResNet50Utils.create_model()

print("Loading Model Weights...")
model.load_weights(MODEL_WEIGHTS)

print("Predicting Model...")
start = timer()
predictions = model.predict(TEST_DATASET)
end = timer()

correct_frames = 0
for i in range(len(predictions)):
    predicted_label = MOVIES_LIST[np.argmax(predictions[i])]
    actual_label = TEST_MOVIES_CSV['Movie'][i]
    if predicted_label == actual_label:
        correct_frames += 1

accuracy = correct_frames / len(TEST_MOVIES_CSV["Frames"]) * 100
print("Correct Frames: ", correct_frames)
print("Accuracy: ", accuracy, "%")

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
current_time = datetime.datetime.now().strftime("%H-%M")
ResNet50Utils.save_testing(end - start, current_date, current_time, accuracy)
