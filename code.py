import cv2
import numpy as np

##read video
cap = cv2.VideoCapture ('HowPeopleWalk.mp4')

ret , frame1 = cap.read()
ret , frame2 = cap.read()

##open the video and read it all
while cap.isOpened():
	#extract the difference between the first and second frame
	diff = cv2.absdiff(frame1,frame2)
	#look for contours
	gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5,5), 0)
	#_ because we don't need the second variable
	_,thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
	dilated = cv2.dilate(thresh, None, iterations=3)
	contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	#draw the contours
	#cv2.drawContours(frame1,contours, -1, (0,255,0), 2)
	for contour in contours:
		#save the cordinate of all contours
		(x,y,w,h) = cv2.boundingRect(contour)

		if cv2.contourArea(contour) < 50000:
			# do nothing because it's not the right object
			continue
		#draw the rectangle
		cv2.rectangle(frame1, (x,y), (x+w, y+h), (227,119,135), 2)
		cv2.putText(frame1, "Status: {}".format('Movement'),(10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (192,192,192), 3)

	cv2.imshow("feed",frame1)

	frame1 = frame2
	ret,frame2 = cap.read()
	#waitkey take the vitess as parameters
	if cv2.waitKey(50) == 27:
		#press esc to stop
		break
cv2.destroyAllWindows()
cap.release()