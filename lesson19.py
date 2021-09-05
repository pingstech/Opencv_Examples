import cv2

def nothing():
    None

#cap=cv2.VideoCapture("vtest.avi")
cap=cv2.VideoCapture(0)
_,frame1=cap.read()
_,frame2=cap.read()
cv2.namedWindow("Settings Bar")
cv2.createTrackbar("Kernal Value","Settings Bar",1,13,nothing)
cv2.createTrackbar("Sigma Value","Settings Bar",1,13,nothing)
cv2.createTrackbar("Threshold Low","Settings Bar",0,255,nothing)
cv2.createTrackbar("Threshold High","Settings Bar",0,255,nothing)
cv2.createTrackbar("Iteration Value","Settings Bar",1,10,nothing)


while (cap.isOpened()):
    kernalVal=cv2.getTrackbarPos("Kernal Value","Settings Bar") 
    sigmaVal=cv2.getTrackbarPos("Sigma Value","Settings Bar")
    threshLow=cv2.getTrackbarPos("Threshold Low","Settings Bar")
    threshHigh=cv2.getTrackbarPos("Threshold High","Settings Bar")
    iterationVal=cv2.getTrackbarPos("Iteration Value","Settings Bar")
    

    diff=cv2.absdiff(frame1,frame2)                      # "frame1" ve "frame2" arasındaki kesin farkı bulur
    grayImg=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blurImg=cv2.GaussianBlur(grayImg,(kernalVal,kernalVal),sigmaVal)
    _,threshImg=cv2.threshold(blurImg,threshLow,threshHigh,cv2.THRESH_BINARY)
    dilated=cv2.dilate(threshImg,None,iterations=iterationVal)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 800:
            continue
        else:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),1)            
            #cv2.drawContours(frame1,contours,-1,(0,255,0),1)

    cv2.imshow("Video",frame1)
    frame1=frame2                                       # Bu işlemleri yapmazsak sadece videodan aldığı ilk görüntü üstüne işleme yapacaktı çünkü videodan okuma işlemini while döngüsünden önce yaptık
    _,frame2=cap.read()                                 # Bu iki işlem ile sürekli videodan veri almasını sağladık 

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()