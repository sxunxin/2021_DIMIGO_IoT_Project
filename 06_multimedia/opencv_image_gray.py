import cv2

img = cv2.imread('Ambition.jpg')
img2 = cv2.resize(img, (600,400))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('Ambition',img2)
cv2.imshow('Ambition_GRAY', gray)

while True:
    if cv2.waitKey() == ord('q'):
        break

cv2.imwrite('Ambition_GRAY.jpg', gray)

cv2.destoryAllWindows()