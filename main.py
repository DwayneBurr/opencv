import cv2 as cv
import pyautogui as py
import time
import os
import numpy as np

def findClickPostions(mining_screen_path, iron_ore_image_path, threshold=0.8, debug_mode=None):

    mining_screen = cv.imread(mining_screen_path, cv.IMREAD_UNCHANGED)
    iron_ore = cv.imread(iron_ore_image_path, cv.IMREAD_UNCHANGED)

    image_w = iron_ore.shape[1]
    image_h = iron_ore.shape[0]

    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(mining_screen, iron_ore, cv.TM_CCOEFF_NORMED)

    cv.imshow('Results', result)
    print(result)

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), image_w, image_h]
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 0, 0.5)
    print(rectangles)

    points = []
    if len(rectangles):
        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS
        
        for (x, y, w, h) in rectangles:
            center_x = x + int(w/2)
            center_y = y + int(w/2)
            points.append((center_x, center_y))

            if debug_mode == 'rectangles':
                top_left = (x, y)
                bottom_right = (x + w, y + h)

                cv.rectangle(mining_screen, top_left, bottom_right, line_color, line_type)
            elif debug_mode == 'points':
                cv.drawMarker(mining_screen, (center_x, center_y), marker_color, marker_type)
        if debug_mode:
            cv.imshow('Results', mining_screen)
            cv.waitKey()
    return points

points = findClickPostions('assets/mining_start.png', 'assets/iron_ore_north.png', debug_mode='points')
print(points)
