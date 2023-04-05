# import cv2

 

# def Find(path) :

#     # 창 이름 설정

#     cv2.namedWindow('image')

 

#     # 이미지 파일 읽기

#     img = cv2.imread(path, cv2.IMREAD_COLOR)

 

#     # 이미지 보여주기

#     cv2.imshow('image', img)

 

#     # 창 esc 끄기

#     while True :

#         if cv2.waitKey(0) == 27 :

#             cv2.destroyWindow('image')

#             break;

#     return

# Find('ex2.jpg')


# 사진 출력하기
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 컬러 있게 설정
# img_basic = cv2.imread('ex2.jpg', cv2.IMREAD_COLOR)
# plt.imshow(cv2.cvtColor(img_basic, cv2.COLOR_BGR2RGB))
# plt.show()

# 컬러 회색(흑백화)
# img_basic = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY) 
# plt.imshow(cv2.cvtColor(img_basic, cv2.COLOR_GRAY2RGB))
# plt.show()

# image = cv2.imread('ex2.jpg', cv2.IMREAD_GRAYSCALE)

# images = []
# ret, thres3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
# ret, thres4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
# images.append(thres3)
# images.append(thres4)


# for i in images:
#     plt.imshow(cv2.cvtColor(i, cv2.COLOR_GRAY2RGB))
#     plt.show()


image = cv2.imread('ex2.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
plt.show()

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()