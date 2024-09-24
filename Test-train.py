import os
import shutil
import random
source_dir = 'C:/Users/A_Pant/Downloads/crop-prediction-dataset-main (2)/crop-prediction-dataset-main'
train_dir = 'C:/Users/A_Pant/Downloads/crop-prediction-dataset-main (2)/train_data'
test_dir = 'C:/Users/A_Pant/Downloads/crop-prediction-dataset-main (2)/test_data'
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# List all files in the source directory
files = os.listdir(source_dir)

# Shuffle the files
random.shuffle(files)

# Define the split index
split_index = int(0.8 * len(files))  # 80% for training

# Split the files
train_files = files[:split_index]
test_files = files[split_index:]

# Move files to respective directories
for file in train_files:
    shutil.move(os.path.join(source_dir, file), os.path.join(train_dir, file))

for file in test_files:
    shutil.move(os.path.join(source_dir, file), os.path.join(test_dir, file))

print(f'Train files: {len(os.listdir(train_dir))}')
print(f'Test files: {len(os.listdir(test_dir))}')