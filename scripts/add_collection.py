#!/usr/bin/env python

import boto3 as b3
from argparse import ArgumentParser
from time import gmtime, strftime

def get_client():
    return b3.client('rekognition')

def get_args():
    parser = ArgumentParser(description='Add aws collections')
    parser.add_argument('-n', '--name')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    
    client = get_client()

    print '[+] Adding a new collection to aws rekognition called %s...' % (args.name)
    response = client.create_collection(CollectionId=args.name)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        current = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        with open('collections.txt', 'a+') as file:
            file.write(('%s | %s') % (current, args.name))

        print '[+] Done!'
