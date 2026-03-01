import cv2

image = cv2.imread('jiujiu.png')
image_cropped = image[:, 525:-525]
h,w = image_cropped.shape[:2]
h = (h-w*500//800)//2

image_cropped = image_cropped[h:-h+70, :]
cv2.namedWindow('cropped_image.png', cv2.WINDOW_NORMAL)
cv2.imshow('cropped_image.png', image_cropped)
cv2.waitKey(0)
cv2.imwrite('99.png', image_cropped)