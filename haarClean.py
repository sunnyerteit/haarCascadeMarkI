# python can't refer to default-site packages folder. It's possible to edit ~/.bashrc to have a default workaround.
#
# here is workaround from stackoverflow, this is better if you use pyCharm:
# Try to add the following line in ~/.bashrc
# export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
#
# this is what i do:
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np

# these are the Haar cascade files openCV employs to find the desired objects
# krone_cascade.xml     -> 1 NOK coin
# tier_cascade.xml      -> 10 NOK coin
# toHundre_cascade.xml  -> 200 NOK bill
krone_cascade = cv2.CascadeClassifier('krone_cascade.xml')
tier_cascade = cv2.CascadeClassifier('tier_cascade.xml')
toHundre_cascade = cv2.CascadeClassifier('toHundre_cascade.xml')

# import video input. If you wish the video input to be a live feed from your webcamera, you can try this:
# cap = cv2.VideoCapture(0)
# instead
cap = cv2.VideoCapture(0)

# this while
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # toHundre = toHundre_cascade.detectMultiScale(gray, 3, 3)
    # tier = tier_cascade.detectMultiScale(gray, 2, 2)
    krone = krone_cascade.detectMultiScale(gray, 5, 5)
    x = 0
    for (x, y, w, h) in krone:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        x += 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'You have'+str(x), (10, 10), font, 0.5, (11, 255, 255), 2, cv2.LINE_AA)
    # for (x, y, w, h) in tier:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
    # for (x, y, w, h) in toHundre:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
