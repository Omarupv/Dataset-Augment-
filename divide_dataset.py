import os 


##train validation 0.8 0.2
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

dataset_dir = os.getcwd()+ "/dataset"
train_dir = dataset_dir + "/train"
val_dir = dataset_dir + "/val"
os.mkdir(dataset_dir)
os.mkdir(train_dir)
os.mkdir(val_dir)

inv_names = {v: k for k, v in class_names.items()}

names = []
num_detections = []
total = []

##poner carpeta con imagenes en el directorio en el que se ponga este archivo, por ejemplo si se llama images:
folder = os.getcwd() + "/images/"
os.chdir(folder)
for filename in os.listdir(folder):
		if not filename.endswith(".txt"):
			name, ext = filename.split(".")
			names.append((name,ext))

for name in names: 
	with open((str(name[0]) + ".txt"), "r") as class_text: 
			for line in class_text:
				line_list = line.split()
				class_name = class_names[int(line_list[0])]
				num_detections.append(inv_names[class_name])

			set(num_detections)
			frequent = max(set(num_detections), key = num_detections.count)
			total.append((frequent,str(name[0] + "." + ext)))
			#total.append((frequent,(name,ext)))

person = 0
bike = 0 
car = 0
motorbike = 0
aircraft = 0
bus = 0
train = 0
truck = 0
ship = 0
for item in total:
	if item[0] == 8:
		ship +=1
	elif item[0] == 7:
		truck +=1
	elif item[0] == 6:
		train +=1
	elif item[0] == 5:
		bus +=1
	elif item[0] == 4:
		aircraft +=1
	elif item[0] == 3:
		motorbike +=1
	elif item[0] == 2:
		car +=1
	elif item[0] == 1:
		bike +=1
	elif item[0] == 0:
		person +=1


train_ship = int(ship * 0.8)
train_bus = int(bus * 0.8)
train_aircraft = int(aircraft * 0.8)
train_motorbike = int(motorbike * 0.8)
train_car = int(car * 0.8)
train_bike = int(bike * 0.8)
train_person = int(person * 0.8)
train_train = int(train * 0.8)


for item in total:
	if item[0] == 8:
		if train_ship>0:
			os.replace(folder + "/" + item[-1], train_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  train_dir + "/" + txt)
			train_ship -=1
		else:
			os.replace(folder + "/" + item[-1], val_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  val_dir + "/" + txt)


	elif item[0] == 7:
		if train_truck>0:
			os.replace(folder + "/" + item[-1], train_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  train_dir + "/" + txt)
			train_truck -=1
		else:
			os.replace(folder + "/" + item[-1], val_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  val_dir + "/" + txt)


	elif item[0] == 6:
		if train_train>0:
			os.replace(folder + "/" + item[-1], train_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  train_dir + "/" + txt)
			train_train -=1
		else:
			os.replace(folder + "/" + item[-1], val_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  val_dir + "/" + txt)


	elif item[0] == 5:
		if train_knife>0:
			os.replace(folder + "/" + item[-1], train_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  train_dir + "/" + txt)
			train_knife -=1
		else:
			os.replace(folder + "/" + item[-1], val_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  val_dir + "/" + txt)


	elif item[0] == 4:
		if train_aircraft>0:
			os.replace(folder + "/" + item[-1], train_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  train_dir + "/" + txt)
			train_aircraft -=1
		else:
			os.replace(folder + "/" + item[-1], val_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  val_dir + "/" + txt)



	elif item[0] == 3:
		if train_motorbike>0:
			os.replace(folder + "/" + item[-1], train_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  train_dir + "/" + txt)
			train_motorbike -=1
		else:
			os.replace(folder + "/" + item[-1], val_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  val_dir + "/" + txt)


	elif item[0] == 2:
		if train_car>0:
			os.replace(folder + "/" + item[-1], train_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  train_dir + "/" + txt)
			train_car -=1
		else:
			os.replace(folder + "/" + item[-1], val_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  val_dir + "/" + txt)


	elif item[0] == 1:
		if train_car>0:
			os.replace(folder + "/" + item[-1], train_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  train_dir + "/" + txt)
			train_car -=1
		else:
			os.replace(folder + "/" + item[-1], val_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  val_dir + "/" + txt)


	elif item[0] == 0:
		if train_person>0:
			os.replace(folder + "/" + item[-1], train_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  train_dir + "/" + txt)
			train_person -=1
		else:
			os.replace(folder + "/" + item[-1], val_dir + "/" + item[-1])
			name, ext = item[-1].split(".")
			txt = item[-1].replace(ext,"txt")
			os.replace(folder + "/" + txt,  val_dir + "/" + txt)