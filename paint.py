import os 
import cv2 
import json 
import sys



paths = ["train", "val", "original"]
path = None
if len(sys.argv) == 1:
	print("Please input directory: test, train, val, or original")
	sys.exit(1)
if  sys.argv[1] in paths:
	path = os.getcwd() + "/dataset/" +  sys.argv[1] + "/"
elif sys.argv[1] == "test":
	path = os.getcwd() + "/images/" 
else:
	print("Error parsing arguments, must be test, train, val, or original")
	sys.exit(1)

def visualize(img, bboxes):
	#cv2.imshow("img", img)
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
		cv2.rectangle(img, (l, t), (r, b), (0, 255, 0), 2)

		cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
		cv2.resizeWindow('custom window', dw, dh)
		cv2.imshow("custom window", img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()




print(path)
for element in os.listdir(path):
	if element.endswith(".txt"):
		bboxes=[]
		f = open(path + element, "r")
		lines = f.read()
		line = lines.split("\n")
		for l in line:
			coord = l.split(" ")
			if len(coord)>1:
				bbox = [float(coord[1]), float(coord[2]), float(coord[3]), float(coord[4])]
				bboxes.append(bbox)

		image = element.replace(".txt", ".jpg")
		img = cv2.imread(path +image)
		visualize(img, bboxes)
