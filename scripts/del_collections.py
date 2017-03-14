#!/usr/bin/env python

import boto3 as b3
from argparse import ArgumentParser

def get_client():
    client = b3.client('rekognition')
    return client

def get_args():
    parser = ArgumentParser(description='Add aws collections')
    parser.add_argument('-c', '--collection')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    
    client = get_client()

    print '[+] Removing collection called %s from aws rekognition...' % args.collection
    response = client.delete_collection(CollectionId=args.collection)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
	print '[+] Please remove that entry from collections.txt!'
        print '[+] Done!'


