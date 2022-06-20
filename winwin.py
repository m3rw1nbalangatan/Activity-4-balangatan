import cv2
import os

while True:
	imageName = input("\nImage name [add '.jpg' at the end of the name: ")
	flag = input("\n Choose [1] for gray image or [2] for colored image: ")

	if os.path.exists(imageName) and flag == '1':
		image= cv2.imread(imageName, 0)
		cv2.imshow(imageName, image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break
	elif os.path.exists(imageName) and flag == '2':
		image= cv2.imread(imageName, 1)
		cv2.imshow(imageName, image)
		cv2.waitKey(0)
		cv2.destroyAllWindows
