#!/usr/bin/env python

import boto3 as b3
import os
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
    path = '../faces/'
    args = get_args()
    
    client = get_client()

    print '[+] Deleting face from colection %s...' % (args.collection)
    response = client.delete_faces(CollectionId=args.collection, FaceIds=[args.id])

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        print '[+] Removing entry from your faces.txt...'
        with open('%sfaces.txt' % path) as oldfile, open('%snewfile.txt' % path, 'w') as newfile:
            for line in oldfile:
                if not args.id in line:
                    newfile.write(line)
        os.rename('%snewfile.txt' % path, '%sfaces.txt' % path)
        print '[+] Done!'
