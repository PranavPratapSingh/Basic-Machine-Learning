import numpy as np
import cv2

cam = cv2.VideoCapture(0)
facec =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ix=0
while True:
    ret,fr=cam.read()
    if ret==True :
        gray=cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY)
        faces=facec.detectMultiScale(gray,1.3,5)
        #ik=0
        for(x,y,w,h) in faces:
            #ik+=1
            fc=fr[y:y+h,x:x+w,:]
            r=cv2.resize(fc, (50,50))
            cv2.rectangle(fr,(x,y),(x+w,y+h),(0,0,255),2)
            #cv2.imshow('face_'+str(ik),fc)
            if ix%10==0 and len(data)<20:
                data.append(r);
        ix+=1
        cv2.imshow('frame',fr)
        if cv2.waitKey(1) & 0xff==ord('q') or len(data)>=20:
            break
    else :
        print "Error"
        break
cv2.destroyAllWindows()
data=np.asarray(data)
print data.shape
np.save('face_01',data)
