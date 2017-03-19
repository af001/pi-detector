[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-green.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

# pi-detector
Raspberry Pi Facial Recognition using AWS Rekognition and Pi-Timolo

### Description
Pi-detector is used with [Pi-Timolo](https://github.com/pageauc/) to search motion generated images for face matches by leveraging AWS Rekognition. In its current state, matches are wrote to event.log. With some additional creativity and work, you could send out a notification or allow/deny access to a room with minimal changes. The install script will place the appropriate files in /etc/rc.local to start on boot.  

### Build Requirements
Raspberry Pi (Tested with Rpi 3) <br />
Picamera <br />
AWS Rekognition Access (Free tier options available) <br />

As an alternative, this set of scripts can be modified to watch any directory that contains images. For example, if you collect still images from another camera and save them to disk, you can alter the image path to run facial recognition against any new photo that is created.

### Install
Setup a Raspberry Pi with Raspbian Jessie <br />
https://www.raspberrypi.org/downloads/raspbian/ <br />

Clone this repo and install:<br />
git clone https://github.com/af001/pi-detector.git<br />
cd pi-detector/scripts<br />
sudo chmod +x install.sh<br />
sudo ./install<br />

### Getting started

First, you need to create a new collection on AWS Rekognition. Creating a 'home' collection would look like:

cd pi-detector/scripts<br />
python add_collection.py -n 'home'<br />

Next, add your images to the pi-detector/faces folder. The more images of a person the better results you will get for detection. I would recommend several different poses in different lighting.

cd pi-detector/faces<br />
python ../scripts/add_image.py -i 'image.jpg' -c 'home' -l 'Tom'<br />

I found the best results by taking a photo in the same area that the camera will be placed, and by using the picam. If you want to do this, I created a small python script to take a photo with a 10 second delay and then puts it into the pi-detector/faces folder. To use it:

cd pi-detector/scripts<br />
python take_selfie.py<br />

Once complete, you can go back and rename the file and repeat the steps above to add your images to AWS Rekognition. Once you create a new collection, or add a new image, two reference files will be created as a future reference. These are useful if you plan on deleting images or collections in the future.

To delete a face from your collection, use the following:

cd pi-detector/scripts<br />
python del_faces.py -i '000-000-000-000' -c 'home'<br />

If you need to find the image id or a collection name, reference your faces.txt and collections.txt files.

To remove a collection:

cd pi-detector/scripts<br />
python del_collections.py -c 'home'<br />

Note that the above will also delete all the faces you have stored in AWS. 

The last script is facematch.py. If you have images updated and just want to test static photos against the faces you have stored on AWS, do the following:

cd pi-detector/scripts<br />
python facematch.py -i 'tom.jpg' -c 'home'<br />

The results will be printed to screen, to include the percentage of similarity and confidence. 
