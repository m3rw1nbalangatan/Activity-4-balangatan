import cv2
filepath = "002.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("MerwinBalangatan",image)
cv2.waitkey(0)
cv2.destroyAllWindows()