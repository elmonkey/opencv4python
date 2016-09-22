'''
Created on May 23, 2013
ref: http://www.cs.washington.edu/education/courses/cse599j/12sp/final_projects/Dave_Lattanzi/video_writer.py 
    
@author: carlos
'''
import cv2, cv
import numpy as np
# import cv2.cv as cv

path = '../img/rgbFrame.jpg'
nf = 90 # number of frames for video

fps = 24
cap = cv2.VideoCapture(0)
f   = 0
# video writer
width  = np.uint8(cap.get(cv.CV_CAP_PROP_FRAME_WIDTH))
height = np.uint8(cap.get(cv.CV_CAP_PROP_FRAME_HEIGHT))
# fps    = np.uint8(cap.get(cv.CV_CAP_PROP_FPS))
# print fps

fourcc = cv.CV_FOURCC('D','I','V','X') # codec
# # uncompressed YUV 4:2:0 chroma subsampled
#fourcc = cv.CV_FOURCC('I','4','2','0')
vidname= "../video/test.avi"
writer = cv2.VideoWriter(vidname, fourcc, fps, (width, height), 1)
print "Press 'spacebar' to start recording avi or 'esc' to terminate"

done = False

while not done:
    k = cv2.waitKey(10)
    flag, frame = cap.read()
    print flag
#     if flag:
    cv2.imshow("live", frame)
    writer.write(frame)
    f+=1
    print "frame No.",f
    if f == nf:
        done = True
    if k == 27: #esc
        done = True

<<<<<<< HEAD
# release resources and destoy windows
cap.release()
vidout.release()
=======
>>>>>>> 73c14692c3ff5f55fe33f217887c3d627a3d0e20
cv2.destroyAllWindows()