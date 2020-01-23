import cv2 # importing opencv library
import numpy as np  #importing numerical python library

img = np.ones([250,250,3],dtype = np.uint8) 

''' Taking white background image , VERY IMPORTANT to mention dtype as np.uint8,
by default it will be float64 which wont work for mixing of more than 2 colors'''

img[:,:] = 150,100,100 # mention BGR values here, Use Color Picker from Paint for reference

cv2.imshow('Output Color',img)  # Display the image

cv2.waitKey(0)  #Wait till you press any key
cv2.destroyAllWindows()  # Close all the opened windows
