import cv2
img = cv2.imread("img.png")
grey_filter = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
final = cv2.bitwise_not(blur)

sketch_final = cv2.divide(grey_filter, final, scale=256.0)

cv2.imwrite("final.png", sketch_final)


