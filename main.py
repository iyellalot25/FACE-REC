import cv2
import face_recognition as fc
import numpy as np
import os

path='TRAIN'
images=[]
classNames=[]
L=os.listdir(path)
#print(L)
for cl in L:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
#print(classNames)

def findEncodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode=fc.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown=findEncodings(images)
print("Encoding Complete")
cap=cv2.VideoCapture(0)
while True:
    success, img=cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facesCurFrame=fc.face_locations(imgS)
    encodesCurFrame=fc.face_encodings(imgS,facesCurFrame)
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches=fc.compare_faces(encodeListKnown, encodeFace)
        faceDis=fc.face_distance(encodeListKnown, encodeFace)
        matchIndex=np.argmin(faceDis) #*lowest value for match
        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            y1,x2,y2,x1=faceLoc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    cv2.imshow("Webcam", img)
    cv2.waitKey(1)