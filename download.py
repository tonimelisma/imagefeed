#!/usr/bin/python3

from tinydb import TinyDB, Query
import metadata_parser
import urllib3
import shutil
import os.path
import pprint

db = TinyDB("/Users/tonimelisma/Development/imagefeed/pictures.json")
http = urllib3.PoolManager()

for pic in db.all():
    page = metadata_parser.MetadataParser(url=pic['url'])

    file_url = ''
    if "video" in page.metadata['og']:
        file_url = page.metadata['og']['video']
    else:
        file_url = page.metadata['twitter']['image']

    filename = os.path.basename(file_url)
    print("downloading ", file_url, " to ", filename)

    with http.request("GET", file_url, preload_content=False) as r, open("scrape/" + filename, "wb") as out_file:
        shutil.copyfileobj(r, out_file)