import cv2

img = cv2.imread('assets/wallp.jpeg',1)
img = cv2.resize(img,(500,500))

print(img.shape)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()