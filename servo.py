#----------------------------------------------------------------------------------------------------------------------------
# Veliboina Manish Kumar # @ gmail - manishkumarveliboina@gmail.com # @ linkedin - Manish Kumar Veliboina 
#----------------------------------------------------------------------------------------------------------------------------
import cv2
import numpy as np
import serial
import time

# Open serial port to communicate with Arduino
ser = serial.Serial('COM5', 9600)  # Replace 'COM10' with your Arduino's serial port

cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 320)

x_medium = None

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low_red = np.array([135, 41, 94])
    high_red = np.array([238, 203, 236])
    
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)

    # Finding contours (endges of group of certain ( red ) color pixels)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        x_medium = int((x + x + w) / 2)
        cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
        break
    
    if x_medium is not None:
        if x_medium < 26:
            command = 'a'  # 'a' command: move to position for letter A
        elif x_medium < 52:
            command = 'b'  # 'b' command: move to position for letter B
        elif x_medium < 78:
            command = 'c'  # 'c' command: move to position for letter C
        elif x_medium < 104:
            command = 'd'  # 'd' command: move to position for letter D
        elif x_medium < 130:
            command = 'e'  # 'e' command: move to position for letter E
        elif x_medium < 156:
            command = 'f'  # 'f' command: move to position for letter F
        elif x_medium < 182:
            command = 'g'  # 'g' command: move to position for letter G
        elif x_medium < 208:
            command = 'h'  # 'h' command: move to position for letter H
        elif x_medium < 234:
            command = 'i'  # 'i' command: move to position for letter I
        elif x_medium < 260:
            command = 'j'  # 'j' command: move to position for letter J
        elif x_medium < 286:
            command = 'k'  # 'k' command: move to position for letter K
        elif x_medium < 312:
            command = 'l'  # 'l' command: move to position for letter L
        elif x_medium < 338:
            command = 'm'  # 'm' command: move to position for letter M
        elif x_medium < 364:
            command = 'n'  # 'n' command: move to position for letter N
        elif x_medium < 390:
            command = 'o'  # 'o' command: move to position for letter O
        elif x_medium < 416:
            command = 'p'  # 'p' command: move to position for letter P
        elif x_medium < 442:
            command = 'q'  # 'q' command: move to position for letter Q
        elif x_medium < 468:
            command = 'r'  # 'r' command: move to position for letter R
        else:
            command = 's'  # 's' command: stop
        
        # Send command to Arduino
        ser.write(command.encode()) 
        print("Command sent:", command)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
    time.sleep(0.1)  # Add a small delay to reduce CPU usage

cap.release()
cv2.destroyAllWindows()
