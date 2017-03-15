#!/usr/bin/env python

import sys
import os
import time
import boto3 as b3
from watchdog.observers import Observer  
from watchdog.events import FileSystemEventHandler, LoggingEventHandler

client = b3.client('rekognition')

class FileEventHandler(FileSystemEventHandler):
    
    def on_created(self, event):
	file = open(event.src_path, 'rb')
        image = file.read()

        response_check = client.detect_faces(Image={'Bytes': image})
        if (not response_check['FaceDetails']):
	    file.flush()
	    file.close()
            os.remove(event.src_path)
        else: 
            resp = client.search_faces_by_image(CollectionId='home', Image={'Bytes': image}, MaxFaces=1, FaceMatchThreshold=85)
	    with open('event.log', 'a+') as check:
                if (not resp['FaceMatches']):
                    check.write('%s | Unknown Person | %s\n' % (time.strftime('%Y-%m-%d %H:%M:%S'), event.src_path))
                else:
                    check.write('%s | %s | %s\n' % (time.strftime('%Y-%m-%d %H:%M:%S'), resp['FaceMatches'][0]['Face']['ExternalImageId'], event.src_path))
    	    file.flush()
	    file.close()

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, path)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    
if __name__ == '__main__':
    main()
