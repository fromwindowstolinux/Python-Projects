import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image,0)
    resized = cv2.resize(img,(500,500))
    cv2.imshow("Look at this!",resized)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,resized)