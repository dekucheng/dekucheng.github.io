#!/usr/bin/env python
import cv2

def main():
    print('a')
    img = cv2.imread('androidbot.png')
    img = cv2.resize(img, (353, 353))
    cv2.imwrite('androidbot.png',img)
if __name__ == '__main__':
    main()
