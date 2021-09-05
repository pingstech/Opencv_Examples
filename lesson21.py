import cv2
import numpy as np

def value(temp):
    print(temp)

img=cv2.imread("h_line.png")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cannyImg=cv2.Canny(grayImg,75,150)
linesInf=cv2.HoughLinesP(cannyImg,1,np.pi/180,50,maxLineGap=150)    # (image, rho, theta, threshold, lines=..., minLineLength=..., maxLineGap=...) şeklinde dolduruluyor

for line in linesInf:
    x1,y1,x2,y2=line[0]                             # Başlangıç ve bitiş noktalarının değerlerini aldık
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("Original Image",img)
cv2.imshow("Gray Image",grayImg)
cv2.imshow("Canny Image",cannyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#****************************************************************Trackbar Kullanarak Görüntülemek İstersek****************************************************************
#               BU İŞLEM İLE ÇİZGİ ÇİZDİRİLMİŞ HALİNİN SON HALİNİ GÖREMİYORUZ ÇÜNKÜ ÇİZDİRME İŞLEMİNİ BİR KERE YAPTIKTAN SONRA SÜREKLİ ÜSTÜNE ÇİZİYOR
# cv2.namedWindow("Original Image")
# cv2.createTrackbar("Threshold 1 Value","Original Image",0,255,value)            # İdeal değeri 180
# cv2.createTrackbar("Threshold 2 Value","Original Image",0,255,value)            # İdeal değeri 109
# cv2.createTrackbar("Hough Threshold Value","Original Image",0,255,value)

# while True:
#     threshOne=cv2.getTrackbarPos("Threshold 1 Value","Original Image")
#     threshTwo=cv2.getTrackbarPos("Threshold 2 Value","Original Image")
#     threhHou=cv2.getTrackbarPos("Hough Threshold Value","Original Image")
#     cannyImg=cv2.Canny(grayImg,threshOne,threshTwo)
#     linesInf=cv2.HoughLinesP(cannyImg,1,np.pi/180,threhHou)                     # bu kısımda ikinci ve üçüncü parametre direkt böyle giriliyor

#     for line in linesInf:
#         print("Line ın içine gelen değer: ",line)
#         x1,y1,x2,y2=line[0]
#         cv2.line(img,(x1,y1),(x2,y2),(0,0,0),2)
        
#     cv2.imshow("First Image",img)
#     cv2.imshow("Gray Image",grayImg)
#     cv2.imshow("Canny Image",cannyImg)

#     if cv2.waitKey(1) & 0xFF==ord("q"):
#         break
#cv2.destroyAllWindows()
#************************************************************************************************************************************************************************