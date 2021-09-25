import numpy as np
import cv2
cam = cv2.VideoCapture(0)
facec =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font=cv2.FONT_HERSHEY_SIMPLEX
f1=np.load('Pranav_Pratap_Singh.npy').reshape((20,-1))
data=np.concatenate((f1))
labels=np.zeros((data.shape[0],))
labels[20:40]=1.0
labels[40:]=2.0
print data.shape
names={0: 'Pranav Pratap Singh'}
def distance(x1, x2):
    d = np.sqrt(((x1-x2)**2).sum())
    return d

def knn(X_train, y_train, xt, k=5):
    vals = []
    for ix in range(X_train.shape[0]):
        d = distance(X_train[ix], xt)
        vals.append([d, y_train[ix]])
    sorted_labels = sorted(vals, key=lambda z: z[0])
    neighbours = np.asarray(sorted_labels)[:k, -1]

    freq = np.unique(neighbours, return_counts=True)

    return freq[0][freq[1].argmax()]
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
            r=cv2.resize(fc, (50,50)).flatten()
            text = names[int(knn(data,labels,r))]
            cv2.putText(fr,text,(x,y),font,1,(225,225,0),2)
            cv2.rectangle(fr,(x,y),(x+w,y+h),(0,0,255),2)
            #cv2.imshow('face_'+str(ik),fc)
            if ix%10==0 and len(data)<20:
                data.append(r);
        ix+=1
        cv2.imshow('frame',fr)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
    else :
        print "Error"
        break

cv2.destroyAllWindows()
