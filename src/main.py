#!/usr/bin/env python3
from google.cloud import storage
from os import environ

if __name__ == '__main__':
    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)
    print(environ.get('TARGET_LANG', 'sa marche pa'))
    print("y se passe rien ici dans le fond...")
