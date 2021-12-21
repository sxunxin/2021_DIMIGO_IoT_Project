import cv2

# xml 필터 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
     print('Camera open failed')
     exit()

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    if not ret:
        break

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)
        
    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()