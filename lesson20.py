import cv2
import numpy as np

def value(temp):
    print("Track Bar Position",temp)

img=cv2.imread("shapes.jpg")
cv2.namedWindow("Image")
cv2.createTrackbar("Min. Thresh. Val.","Image",0,255,value)
cv2.createTrackbar("Max. Thresh. Val.","Image",0,255,value)
font=cv2.FONT_HERSHEY_SIMPLEX
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
while True:
    min_Value=cv2.getTrackbarPos("Min. Thresh. Val.","Image")
    max_Value=cv2.getTrackbarPos("Max. Thresh. Val.","Image")
    _,thresh_Img=cv2.threshold(imgGray,min_Value,max_Value,cv2.THRESH_BINARY)
    contours,_=cv2.findContours(thresh_Img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        cv2.drawContours(img,[approx],0,(0,0,0),5)
        x=approx.ravel()[0]                             # "x" koordinatını "approx" isimli matristen çekiyoruz
        y=approx.ravel()[1]                             # "x" koordinatını "approx" isimli matristen çekiyoruz

        if len(approx) == 3:
            cv2.putText(img,"Triangle",(x,y),font,0.5,(0,255,0))
        
        elif len(approx) == 4:
            x,y,w,h=cv2.boundingRect(approx)                            # "x","y" koordinatını ve boyutlarını verecek
            aspectRatio=float(w/h)                                      #"cv2.drawContours" ile şeklin etrafına çizdirdiğimiz şeklin kare olması için kenarlarını birbirine eşit olması gerekiyor bu yüzden böyle bir formül kullandık
            print("Ratio: ",aspectRatio)
            if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                cv2.putText(img,"Square",(x,y),font,0.5,(0,255,0))
            else:    
                cv2.putText(img,"Rectangle",(x,y),font,0.5,(0,255,0))
        
        elif len(approx) == 5:
            cv2.putText(img,"Pentagon",(x,y),font,0.5,(0,255,0))

        elif len(approx) == 10:
            cv2.putText(img,"Star",(x,y),font,0.5,(0,255,0))
        
        else:
            cv2.putText(img,"Circle",(x,y),font,0.5,(0,255,0))

    cv2.imshow("Image",img)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()