# import cv2
# import mediapipe as mp

# cap = cv2.VideoCapture(0)
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands

# hands = mp_hands.Hands(
#   max_num_hands = 1,
#   min_detection_confidence = 0.5,
#   min_tracking_confidence = 0.5
# )

# while True:
#   success, img = cap.read()
#   if not success:
#     continue

#   imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#   results = hands.process(imgRGB)
#   imgRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
  
#   if results.multi_hand_landmarks:
#     for handLms in results.multi_hand_landmarks:
#       for id, lm in enumerate(handLms.landmark):
#         h, w, c = img.shape
#         cx, cy = int(lm.x*w), int(lm.y*h)
#         print(id, " :", cx, cy)
#         if id == 0:
#           cv2.circle(img, (cx,cy), 20, (255, 0, 0), cv2.FILLED)
#     mp_drawing.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

# cv2.imshow("ex1", img)
# cv2.waitKey(1)


import numpy as np

array = np.array([1, 2, 3])
print(array.size)
print(array.dtype)
print(array[2])

import numpy as np

# 0부터 3까지 배열 만들기
array1 = np.arange(4)
print(array1)

# 0으로 초기화
array2 = np.zeros((4, 4), dtype=float)
print(array2)

# 1로 초기화
array3 = np.ones((3, 3), dtype=str)
print(array3)

# 0부터 9까지 랜덤하게 초기화된 배열 만들기
array4 = np.random.randint(0, 10, (3, 3))
print(array4)

# 평균이 0이고 표준편차가 1인 
array5 = np.random.normal(0, 1, (3, 3))

# 배열 형태 바꾸기
array6 = np.array([1, 2, 3, 4])
array7 = array6.reshape((2, 2))
print(array6.shape)

array = np.arange(8).reshape(2, 4)
left, right = np.split(array, [2], axis=1)
print(left.shape)
print(right.shape)
print(right[1][1])