#!/usr/bin/env python
# coding: utf-8

# # opencv project:- hands finger count 

# In[1]:


import cv2
import mediapipe as mp


# In[2]:


cap = cv2.VideoCapture(0)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils
finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_Coord = (4,2)


# In[ ]:


while True:
    success, image = cap.read()
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_image)
    multiLandMarks = results.multi_hand_landmarks
    # drawing landmarks
    # nested for loop to enable us to work on one hand at a time 
    # and draw the hand landmarks present on each hand
    if multiLandMarks:
        handList = []
        for handLms in multiLandMarks:
            mpDraw.draw_landmarks(image, handLms, mp_Hands.HAND_CONNECTIONS)
            for idx, lm in enumerate(handLms.landmark):
                # Changing the hand points coordinates into image pixels
                h, w, c = image.shape # get the height, width, and color channel
                # get the x and y coordinates of each hand point
                cx, cy = int(lm.x * w), int(lm.y * h)
                # save these hand points in the list
                handList.append((cx, cy))
            # circle each hand point to ensure correct handpoints
            for point in handList:
                cv2.circle(image, point, 10, (255, 255, 0), cv2.FILLED)
            # Checking whether a finger is open or closed
            upCount = 0
            for coordinate in finger_Coord:
                if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                    upCount += 1
            if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
                upCount += 1
            # displaying the output
            cv2.putText(image, str(upCount), (150,150), cv2.FONT_HERSHEY_PLAIN, 12, (0,255,0), 12)

    cv2.imshow("Counting number of fingers", image)
    k = cv2.waitKey(1)& 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()


# # conclusion:- in this project we count the finger, the number of finger are shown by using opencv 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


while True:
    sucess,img=cap.read()
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=hand.process(rgb)
    multilandmark=result.multi_hand_landmarks
    print(multilandmark)
    if multilandmark:
        for handlm in multilandmark:
            mpdraw.draw_landmarks(img,handlm,mpHands.HAND_CONNECTIONS)
            for idx,lm in enumerate(handlm.landmark):
                print(idx,lm)
    cv2.imshow('frame',img)
    


# In[2]:


cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hand=mpHands.Hands()
mpdraw=mp.solutions.drawing_utils


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


import cv2
import mediapipe as mp


# In[3]:


cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpdraw=mp.solutions.drawing_utils


# In[ ]:


while True:
    sucess,img=cap.read()
    rgd=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=hands.process(rgd)
    multilandmark=result.multi_hand_landmarks
    if multilandmark:
        for handlm in multilandmark:
            mpdraw.draw_landmarks(img,handlm,mpHands.HAND_CONNECTIONS)
    cv2.imshow('frame',img)
    if cv2.waitKey()== ord('q'):
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


"hello"


# # hello

# # govind

# # govind
# ## govind
# ### govind

# In[ ]:




