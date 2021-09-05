import cv2
import numpy as np

def value(temp):
    print("Value: ",temp)

img=cv2.imread("opencv-logo.png")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Threshold")
cv2.createTrackbar("Low Value","Threshold",0,255,value)
cv2.createTrackbar("High Value","Threshold",0,255,value)


# ret,thresh=cv2.threshold(grayImg,100,255,0)
# contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# print("Number of contours: ",str(len(contours)))
# # print(contours[0])

# cv2.drawContours(img,contours,-1,(0,255,0),2)
# cv2.imshow("Thresholded Image",thresh)
# cv2.imshow("Original Image",img)
# cv2.imshow("Gray Image",grayImg)

#--------------------------------------İSTERSEK BURADAKİ GİBİ BİR TRACKBAR KULLANIMI İLEDE GÖRÜNTÜLEYEBİLİRİZ--------------------------------------
while True:

    l_Value=cv2.getTrackbarPos("Low Value","Threshold")
    h_Value=cv2.getTrackbarPos("High Value","Threshold")
    
    ret,thresh=cv2.threshold(grayImg,l_Value,h_Value,0)
    contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    print("Number of contours: ",str(len(contours)))
    # print(contours[0])

    cv2.drawContours(img,contours,-1,(0,255,0),2)
    cv2.imshow("Thresholded Image",thresh)
    cv2.imshow("Original Image",img)
    cv2.imshow("Gray Image",grayImg)
    
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
#--------------------------------------------------------------------------------------------------------------------------------------------------

cv2.waitKey(0)
cv2.destroyAllWindows()