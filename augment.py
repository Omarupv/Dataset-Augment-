import albumentations as A
import cv2
import os 
import random
import re
import numpy as np



## Variables 
class_names = { 0: "person",
1: "bike",
2: "car", 
3: "motorbike",
4: "aircraft", 
5: "bus", 
6: "train", 
7: "truck", 
8: "ship",
}

num_errors=0


inv_names = {v: k for k, v in class_names.items()}


##
# Function to generate pseudo-random numbers
#
def random_numbers():
	pass


transform = A.Compose([
    A.GaussNoise(p=0.5, mean = 0, var_limit = [50, 100]),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(brightness_limit=0.1, p = 0.5),
    A.ChannelShuffle(p=0.5),
    A.CLAHE(clip_limit=4.0, tile_grid_size=(8, 8), always_apply=False, p=0.5),
    A.ShiftScaleRotate(rotate_limit=0, shift_limit=0, p=0.5) ,
    A.HueSaturationValue(p=0.5),
    A.MotionBlur(p=0.5),
    A.RandomSizedBBoxSafeCrop(width=416, height=416),
    A.Solarize(p=0.5),
    A.Transpose(p=0.5),
    A.Perspective(p=0.5),
], bbox_params=A.BboxParams(format='yolo'))

##
# Main function, here we augment the images in the augment directory
#
def augment_image(img, img_bbox, num, augment_dir, file, ext):
		global num_errors
		transformed_image = None
		transformed_bboxes = None
		try:
		 transformed = transform(image=img, bboxes=img_bbox)
		 transformed_image = transformed['image']
		 transformed_bboxes = transformed['bboxes']	
		except ValueError as e:
		 num_errors +=1
		 

		if transformed_image is not None and transformed_bboxes!=[] :
			#image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)
			cv2.imwrite(augment_dir + "/" + (file + "_augmented_" + str(num) + "." + ext), transformed_image)
			for bbox in transformed_bboxes:
				with open(augment_dir + "/" + file + "_augmented_" + str(num) +  ".txt", "a") as filetowrite:
					yolo_format = str(inv_names[bbox[-1]]) + " " + str(bbox[0]) + " " + str(bbox[1]) + " " + str(bbox[2]) + " " + str(bbox[3])
					filetowrite.write(yolo_format  + "\n")
			#visualize(transformed_image, transformed_bboxes)


def visualize(img, bboxes):
	cv2.imshow("img", img)
	for bbox in bboxes:
		x, y, w, h = bbox[0], bbox[1], bbox[2], bbox[3]
		dh, dw, _ = img.shape
		l = int((x - w / 2) * dw) 
		r = int((x + w / 2) * dw)
		t = int((y - h / 2) * dh)
		b = int((y + h / 2) * dh)
	    
		if l < 0:
	 		l = 0
		if r > dw - 1:
	 		r = dw - 1
		if t < 0:
	 		t = 0
		if b > dh - 1:
	 		b = dh - 1
		cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 1)
		cv2.imshow("img", img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()


def load_names(folder):
	names = []
	for filename in os.listdir(folder):
		if  not filename.endswith(".txt"):
			name, ext = filename.split(".")
			names.append((name,ext))
	return names


def write_names(dataset_folder):
	for filename in os.listdir(folder + "/train"):
		with open(folder + "/" + "object_names_train.txt", "a") as filetowrite:
			if ".txt" not in filename:
				filetowrite.write(filename + "\n")
	for filename in os.listdir(folder + "/val"):
		with open(folder + "/" + "object_names_test.txt", "a") as filetowrite:
			if ".txt" not in filename:
				filetowrite.write(filename + "\n")


def progressBar(current, total, dir, barLength = 30):
	info = ' Progress of ' + dir + ' directory:'
	percent = float(current) * 100 / total
	arrow   = '-' * int(percent/100 * barLength - 1) + '>'
	spaces  = ' ' * (barLength - len(arrow))
	print('%s [%s%s] %d %%' % (info, arrow, spaces, percent), end='\r')


def load_and_transform_img(folder):
	augment_dir = folder#os.getcwd() + "/augmented"
	image_dir = folder
	os.chdir(image_dir)
	names = load_names(image_dir)
	num = 0
	if "train" in str(folder):
		work_dir = "train"
	else:
		work_dir="test"

	total = len(names)
	current = 1
	for name in names:
		progressBar(current, total, work_dir)
		current+=1
		file = name[0]
		ext = name[-1]
		img_bbox = []
		with open((str(file) + ".txt"), "r") as class_text: 
			for line in class_text:
				line_list = line.split()
				class_name = class_names[int(line_list[0])] 
				x, y, w, h = round(float(line_list[1]),4), round(float(line_list[2]),4), round(float(line_list[3]),4), round(float(line_list[4]),4) 
				bbox = [x, y, w, h, class_name]
				bbox = [x, y, w, h, class_name]
				if w and h > 0.1:
					img_bbox.append(bbox)

		img_loc = folder + "/" + file + "." + ext  
		img = cv2.imread(img_loc)
		## remove to avoid channel mixup
		#img_format = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		##print(str(x) + "/n" + str(y) + "/n" + str(w) + "/n" + str(h))
		
		for i in range(10): 
			augment_image(img, img_bbox, i, augment_dir, file, ext)
	
	print(" ", end='\n')


dataset_dir = os.getcwd() + "/dataset"
train_dir = dataset_dir + "/train"
val_dir = dataset_dir + "/val"

load_and_transform_img(train_dir)
load_and_transform_img(val_dir)

print("Total number of images skipped: " + str(num_errors))
#write_names(train_dir)
#write_names(val_dir)






















