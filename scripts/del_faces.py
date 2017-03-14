#!/usr/bin/env python

import boto3 as b3
from argparse import ArgumentParser
from time import gmtime, strftime

def get_client():
    return b3.client('rekognition')

def get_args():
    parser = ArgumentParser(description='Add aws collections')
    parser.add_argument('-i', '--id')
    parser.add_argument('-c', '--collection')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    
    client = get_client()

    print '[+] Deleting face from colection %s...' % (args.collection)
    response = client.delete_faces(CollectionId=args.collection, FaceIds=[args.id])

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
	print '[+] Please remove that entry from your faces.txt file!'
        print '[+] Done!'
