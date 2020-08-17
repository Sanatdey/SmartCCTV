# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:35:04 2019

@author: SANAT
"""
import cv2
import numpy as np
import time

def main():
    
    w = 800
    h = 600
    status = 0
    
    cap = cv2.VideoCapture(0)
    
    cap.set(3, w)
    cap.set(4, h)
    
#    print(cap.get(3))
#    print(cap.get(4))
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    
    cap = cv2.VideoCapture(0)            
    sec =time.time()
    filepath = "C:\\Users\\G0utam\\Desktop\\Code\\Python Project\\Outbase\\Tutorila1"+str(sec)+".avi"
    codec = cv2.VideoWriter_fourcc(*"MJPG")            
    resolution = (640 , 480)
    videoFileOutput = cv2.VideoWriter(filepath , codec , 10 , resolution)
    
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()


    while True:
        status = 0
        ret , frame3 = cap.read()
        #videoFileOutput.write(frame3)   
        d = cv2.absdiff(frame1, frame2)
        #img = np.zeros((512 ,512 ,3) ,np.uint8)        
        grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)        
        blur = cv2.GaussianBlur(grey, (5, 5), 0)        
        ret, th = cv2.threshold( blur, 30, 255, cv2.THRESH_BINARY)    
        dilated = cv2.dilate(th, np.ones((3, 3), np.uint8), iterations=0 )        
        #eroded = cv2.erode(dilated, np.ones((3, 3), np.uint8), iterations=1 )        
        (cnts, _)= cv2.findContours(dilated.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in cnts:
            if cv2.contourArea(contour) < 1000:
                continue
            status = 1
        
#        videoFileOutput.write(frame1)                
#        cv2.imshow("Original", frame2)
        #videoFileOutput.release()              
        cv2.drawContours(frame1, cnts, -1, (0, 0, 255), 2)
        cv2.imshow("Output", frame1)
        cv2.imshow("Output2", th)           
       # VideoCap(status)
        

        
        if status == 1 : 
        #rat ,fram = cap.read()
            frame3 = cv2.flip(frame3 ,1)
            print("true") 
            videoFileOutput.write(frame3)                
            cv2.imshow("Original", frame2)
        else:
            videoFileOutput.release()
        
        #cv2.destroyWindow("Original")
        #print("false")
        if cv2.waitKey(1) == 27:
            videoFileOutput.release()
            break
            
        frame1 = frame2
        ret, frame2 = cap.read()
        status = 0
               
        
    videoFileOutput.release()    
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()