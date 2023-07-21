
import datetime
import cv2
import numpy as np

capture = cv2.VideoCapture(2)

if capture.isOpened() == False :
	print('Unable to read camera feed')
else:
    fps = capture.get(cv2.CAP_PROP_FPS)
    print("FPS : ",capture.get(cv2.CAP_PROP_FPS))
    w = round(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("Width : ",w, "   Height : ", h)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # *'DIVX' == 'D','I','V','X'
    record = False

    while True: 
        ret, frame = capture.read()
        #print(np.shape(frame),(frame.shape[1],frame.shape[0]))
        cv2.imshow("VideoFrame", frame)
        now = datetime. datetime. now(). strftime( " %d _%H-%M-%S")
        
        #27 = ESC, 
        #26 = Ctrl + Z, 
        #24 = Ctrl + X, 
        #3 = Ctrl + C

        key = cv2.waitKey(1) 
        if key & 0xFF == ord('r'):
            print( "start")
            record = True
            video = cv2.VideoWriter("/home/kist/ouput_video/" + str(now) +"output1.avi", fourcc, fps, (w, h))
            #video = cv2.VideoWriter("asdf.avi", fourcc, 20.0, (frame.shape[0],frame.shape[1]))
            #video = cv2.VideoWriter("Video/" + str(now) + ".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
        elif key & 0xFF == ord('x'):
            print( "stop")
            record = False
            video.release()
            break

        if record == True:
            print( "recoding..")
            video.write(frame)
