#!/usr/bin/env python

from picamera import PiCamera
import time

count = 10
camera = PiCamera()

print '[+] A photo will be taken in 10 seconds...'

for i in range(count):
    print (count - i)
    time.sleep(1)

milli = int(round(time.time() * 1000))
image = '/home/pi/pi-detector/faces/image_%r.jpg' % milli
camera.capture(image)
print 'Your image was saved to %s' % image
