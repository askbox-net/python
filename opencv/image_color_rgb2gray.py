# -*- coding:utf-8 -*-
#!/usr/bin/python

import cv2


input_filename = "./images/lena.jpg"
output_filename = "./output/lena_gray.jpg"

if __name__ == "__main__":
	image = cv2.imread(input_filename)
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imwrite(output_filename, image_gray)

