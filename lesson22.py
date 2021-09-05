import cv2
import numpy as np

cap=cv2.VideoCapture("line.mp4")

while (cap.isOpened()):
    _,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    hsvFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)      # HSV değerlerini bulmak istediğimiz rengi google yazarak bulabiliriz buna göre alt kısmı doldurabiliriz
    l_lineValue=np.array([18,94,140],np.uint8)
    h_lineValue=np.array([48,255,255],np.uint8)
    mask=cv2.inRange(hsvFrame,l_lineValue,h_lineValue)
    edgesFrame=cv2.Canny(mask,75,250)
    lines=cv2.HoughLinesP(edgesFrame,1,np.pi/180,50,minLineLength=10,maxLineGap=50) 

    for line in lines:

        (x1,y1,x2,y2)=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),2)
    
    cv2.imshow("Original Video",frame)
    cv2.imshow("Mask Video",mask)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()