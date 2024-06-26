import cv2 as cv
import numpy as np
import os
import pyautogui as py

while(True):

  screenshot = py.screenshot()
  screenshot = np.array(screenshot)

  cv.imshow('Computer Vision', screenshot)

  if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows()
    break


print('done')
