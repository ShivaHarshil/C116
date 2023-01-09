import cv2

image = cv2.imread("C:/Users/Rajesh Reddy/Downloads/copyFiles-main/bird.jpg")
print(image)
cv2.imshow("goku",image)
greyimg = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("graybird",greyimg)
