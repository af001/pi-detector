# pi-detector
> Raspberry Pi Facial Recognition using AWS Rekognition and Pi-Timolo

![License][license-image]
![Python][python-version]

## Description
Pi-detector is used with [Pi-Timolo](https://github.com/pageauc/) to search motion generated images for face matches by leveraging AWS Rekognition. In its current state, matches are wrote to event.log. With some additional creativity and work, you could send out a notification or allow/deny access to a room with minimal changes. The install script will place the appropriate files in /etc/rc.local to start on boot.  

## Build Requirements
* Raspberry Pi (Tested with Rpi 3)
* Picamera
* AWS Rekognition Access (Free tier options available)

As an alternative, this set of scripts can be modified to watch any directory that contains images. For example, if you collect still images from another camera and save them to disk, you can alter the image path to run facial recognition against any new photo that is created.

## Install
Setup a Raspberry Pi with [Raspbian Jessie](https://www.raspberrypi.org/downloads/raspbian/), then clone this repo and run the install script: 
```sh
git clone https://github.com/af001/pi-detector.git
cd pi-detector/scripts
sudo chmod +x install.sh
sudo ./install.sh
```

## Getting started

First, you need to create a new collection on AWS Rekognition. The following will create a 'home' collection on Rekognition:

```sh
cd pi-detector/scripts
python add_collection.py -n 'home' 
```

Add your images to the *pi-detector/faces* folder. The more images of a person you have the better results you will get for detection. I would recommend several different poses in different lighting. The following command will take an image named *image.jpg* with a label of *Tom* and add it to the *home* collection.

```sh
cd pi-detector/faces 
python ../scripts/add_image.py -i 'image.jpg' -c 'home' -l 'Tom' 
```

I found the best results by taking a photo with the picam in the same area that the camera will be placed. If you want to do this, I created a small python script to take a photo with a 10 second delay and then puts it into the *pi-detector/faces* folder. To use it:

```sh
cd pi-detector/scripts 
python take_selfie.py 
```

Once complete, you can go back and rename the file and repeat the steps above to add your images to AWS Rekognition. Once you create a new collection, or add a new image, two reference files will be created. These are useful if you plan on deleting images or collections in the future.

To delete a face from your collection, use the following:
```sh
cd pi-detector/scripts 
python del_faces.py -i '000-000-000-000' -c 'home' 
```

If you need to find the image id or a collection name, reference your *faces.txt* and *collections.txt* files.

To remove a collection:
```sh
cd pi-detector/scripts 
python del_collections.py -c 'home' 
```

Note that the above will also delete all the faces you have stored in AWS. 

The last script is *facematch.py*. If you have images updated and just want to test static photos against the faces you have stored on AWS, do the following:

```sh
cd pi-detector/scripts 
python facematch.py -i 'tom.jpg' -c 'home' 
```

The results will be printed to screen, to include the percentage of similarity and confidence. 

<!-- Markdown link & img dfn's -->
[license-image]: https://img.shields.io/badge/license-MIT-green
[python-version]: https://img.shields.io/badge/Python-2-green
