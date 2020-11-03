# #code for sampling image from the video @ 5fps
# #to be used only once for sampling video
import cv2
import math   # for mathematical operations
import matplotlib.pyplot as plt    # for plotting the images

count = 0
videoFile = "D:\\Practice\\Git\\HackerEarth-Emotion-Detection-Tom-Jerry-Cartoon\\Dataset\\Test Tom and jerry.mp4"
cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
x=1

while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename ="D:\\Practice\\Git\HackerEarth-Emotion-Detection-Tom-Jerry-Cartoon\\Dataset\\Test\\test%d.jpg" % count;count+=1
        cv2.imwrite(filename, frame)
        print("*", end="")
    
cap.release()
cv2.destroyAllWindows()
print ("Done!")