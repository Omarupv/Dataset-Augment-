import os

dataset_dir = os.getcwd() + "/dataset"
train_dir = dataset_dir + "/train"
val_dir = dataset_dir + "/val"

def move(folder_from, folder_to):
	for filename in os.listdir(folder_from):
		if "augmented" not in filename:
			os.replace(folder_from + "/" + filename, folder_to + "/" + filename)


def write_names(folder):
	for filename in os.listdir(folder + "/train"):
		with open(folder + "/" + "object_names_train.txt", "a") as filetowrite:
			if ".txt" not in filename:
				filetowrite.write(filename + "\n")
	for filename in os.listdir(folder + "/val"):
		with open(folder + "/" + "object_names_val.txt", "a") as filetowrite:
			if ".txt" not in filename:
				filetowrite.write(filename + "\n")
	for filename in os.listdir(folder + "/original"):
		with open(folder + "/" + "object_names_original.txt", "a") as filetowrite:
			if ".txt" not in filename:
				filetowrite.write(filename + "\n")

original_dir = dataset_dir + "/original"
os.mkdir(original_dir)

move(train_dir, original_dir)
move(val_dir, original_dir)


write_names(dataset_dir)