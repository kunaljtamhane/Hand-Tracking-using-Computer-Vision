import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# FPS
pTime = 0
cTime = 0


while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting the image from BGR to RGB as hands module only support RGB

    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)


# Checking for multiple hands and extracting them
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # We will get the ID number and Hand Landmark information
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm) # gives a corresponding X,Y and Z co-ordinate of the hand movement we are going to use the x and y coordinate to find the information of the hand
                h, w, c = img.shape # height, width and channels of the image
                cx, cy = int(lm.x*w), int(lm.y*h) # position of the center
                print(id, cx, cy)
                if id==0:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

# To Calculate the frames per second
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
# Displaying FPS in the video (put on image, convert to string, cast from integer, position, font, scale, color, font thickness)
    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)