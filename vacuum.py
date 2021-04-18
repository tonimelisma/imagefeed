#!/usr/bin/python3

# this script downloads the list of latest posts and saves them in mongodb

from imgur_scraper import imgur_scraper
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from pymongo.operations import ReplaceOne
import pprint

client = MongoClient('mongodb://192.168.1.2:27017/')

imagefeed_db = client.imagefeed
posts = imagefeed_db.posts

mongodb_requests = []
for post in imgur_scraper.get_viral_posts_from(start_date="2021-01-08", end_date="2021-01-09"):
    mongodb_requests.append(ReplaceOne({'url': post["url"]}, post, upsert=True))

try:
    posts.bulk_write(mongodb_requests, ordered=False)
except BulkWriteError as bwe:
    pprint(bwe.details)
