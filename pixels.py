import cv2
from time import sleep
import numpy
width=640
height=480
xVal=0
yVal=0
evt=0
x=0
y=0
z=0
def Mouse(event,xpos,ypos,flags,params):
    global xVal
    global yVal
    global evt
    
    if event==cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt=event
        xVal=xpos
        yVal=ypos

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('My webCam')
cv2.setMouseCallback('My webCam',Mouse)
while True:

    ignore, frame=cam.read()
    if evt==1:
        y=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        clr=y[xVal][yVal]
        print(clr)
        x=numpy.zeros([250,250,3],dtype=numpy.uint8)
        
        x[:,:]=(clr)
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        
        cv2.imshow('other one',x)
        cv2.moveWindow('other one',650,0)
        
        evt=0
   
    cv2.imshow('My webCam', frame)
    cv2.moveWindow('My webCam',0,0)
    
    if cv2.waitKey(1) == ord('q'):

        break
    
cam.release()
