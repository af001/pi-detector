#!/usr/bin/env python

from argparse import ArgumentParser
import boto3
from time import gmtime, strftime
import simplejson as json
import os

def get_client():
    client = boto3.client('rekognition')
    return client

def get_args():
    parser = ArgumentParser(description='Call index faces')
    parser.add_argument('-i', '--image')
    parser.add_argument('-c', '--collection')
    parser.add_argument('-l', '--label')
    return parser.parse_args()

def init_file():
    if (not os.path.isfile('faces.txt')):
        with open('faces.txt', 'w') as init_file:
	    init_file.write('Date | Label | Collection | FaceId | ImageId\n')             

if __name__ == '__main__':
    args = get_args()
    client = get_client()

    init_file()

    with open(args.image, 'rb') as image:
        response = client.index_faces(Image={'Bytes': image.read()}, CollectionId=args.collection, ExternalImageId=args.label, DetectionAttributes=['ALL'])

        with open('faces.txt', 'a') as file:
            current = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            file.write(('%s | %s | %s | %s | %s\n') % (current, args.label, args.collection, response['FaceRecords'][0]['Face']['FaceId'], response['FaceRecords'][0]['Face']['ImageId']))
