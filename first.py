import cv2
from ultralytics import YOLO

model = YOLO("../YoloWeights/yolov8l.pt")
results = model("./images/image1.jpg" , show=True) 
results[0].save(filename="output2.jpg")

cv2.waitKey(0)