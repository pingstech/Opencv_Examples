import cv2

cap=cv2.VideoCapture("vtest.avi")
ret,frame1=cap.read()
ret,frame2=cap.read()

while cap.isOpened():
    diff=cv2.absdiff(frame1,frame2)                 #İKİ DEĞİŞKEN ARASINDAKİ FARKI BULUR
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)      #CONTOUR YAPACAĞIMIZ İÇİN BÖYLE BİR ÖN HAZIRLIK YAPTIK
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)

        if cv2.contourArea(contour)<800:        # BURADA GEREKSİZ OLAN ŞEYLER İÇİN YANİ KÜÇÜK HAREKETLER İÇİN CONTOUR ÇİZDİRMEMESİNİ SAĞLADIK
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,255),2)
        cv2.putText(frame1,"Durum:{}".format("Hareketli"),(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        cv2.putText(frame1,"Hedef",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)

    cv2.imshow("Motion Detect",frame1)
    frame1=frame2                                     # Bu işlemleri yapmazsak sadece videodan aldığı ilk görüntü üstüne işleme yapacaktı çünkü videodan okuma işlemini while döngüsünden önce yaptık
    ret,frame2=cap.read()                             # Bu iki işlem ile sürekli videodan veri almasını sağladık 

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()