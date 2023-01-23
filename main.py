import imghdr
import cv2
import os
import glob 

with open('coco.names', 'r') as f:
    classes = f.read().splitlines()
try:
    #model_file='guns_onnx/yolov5s.onnx'    
    net = cv2.dnn.readNet('cfg\yolov4.cfg', 'yolov4.weights' )
    #net = cv2.dnn.readNetFromONNX(model_file)    
except Exception as e:
    
    print("exception in readnet: ",e)

model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)


def detect(image):
    img = cv2.imread(image)
    
    classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)

    print("boxes =",boxes)
    print("classIds =",classIds)
    print("scores =",scores)

    return boxes,classIds,scores
