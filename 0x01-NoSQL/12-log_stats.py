#!/usr/bin/env python3
"""Task 12's module.
"""
from pymongo import MongoClient


def printer(nginx_collector):
    """Prints stats about Nginx requests logs
    """
    print('{} logs'.format(nginx_collector.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collector.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collector.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    """provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    printer(client.logs.nginx)


if __name__ == '__main__':
    run()
