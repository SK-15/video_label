import cv2

video = cv2.VideoCapture('video.mp4')

fps = video.get(cv2.CAP_PROP_FPS)
print('frames per second =',fps)

minutes = 0
seconds = 28
frame_id = int(fps*(minutes*60 + seconds))
print('frame id =',frame_id)

video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
ret, frame = video.read()

t_msec = 1000*(minutes*60 + seconds)
video.set(cv2.CAP_PROP_POS_MSEC, t_msec)
ret, frame = video.read()

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.imwrite('my_video_frame.png', frame)


import cv2
 
capture = cv2.VideoCapture('video.mp4')
 
frameNr = 0
 
while (True):
 
    success, frame = capture.read()
 
    if success:
        cv2.imwrite(f'output/frame_{frameNr}.jpg', frame)
 
    else:
        break
 
    frameNr = frameNr+1
 
capture.release()