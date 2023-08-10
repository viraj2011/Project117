import os
import cv2

path = "Images"

Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = ('width','height')
print(size)

out = cv2.VidioWriter('project.avi' ,cv2.VidioWriter_fourcc(*'DIVX',0.8 ,size))

for i in range(count-1,0,-1):
    frame = cv2.imread(Images[i])
    out.write(frame)

out.write()   
# releasing the vidio generated
print("Done")    
