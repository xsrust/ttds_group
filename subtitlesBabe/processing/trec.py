import os
import re
import sys
import xml
import json

import readSubtitles as rs

def first_true(iterable, default=False, pred=None):
    """Returns the first true value in the iterable.

    FROM: https://stackoverflow.com/a/48140611

    If no true value is found, returns *default*

    If *pred* is not None, returns the first item
    for which pred(item) is true.

    """
    # first_true([a,b,c], x) --> a or b or c or x
    # first_true([a,b], x, f) --> a if f(a) else b if f(b) else x
    return next(filter(pred, iterable), default)



input_path = sys.argv[1]
output_path = sys.argv[2]

not_processed = []

output_file = open(output_path, 'w')


# Load films json
with open('newfilms.json') as file_:
    newfilms_json = json.load(file_)

with open('films.json') as file_:
    films_json = json.load(file_)

count = 0
for subtitle_path in os.listdir(input_path):

    subtitle = rs.superSubtitle(input_path + "/" + subtitle_path)
    if subtitle.extension not in ['srt','sub','txt','tmp','smi','ssa']:
        continue

    count+=1
    print(str(count)+ ":\t"+str(subtitle_path))


    subtitle_code = subtitle_path.split("/")[-1][:-4]
    subtitle_text = subtitle.toText()

    json_entry = first_true(films_json,None, lambda x: x['id'] == subtitle.name)
    if not json_entry:
        json_entry = first_true(newfilms_json,None, lambda x: x['id'] == subtitle.name)
        assert json_entry, ("No entry found for movie " + subtitle.name)
    movie_title=json_entry['title']
    movie_genres = json_entry['genres']

    output_file.write("<DOC>\n<DOCNO>" + str(subtitle_code) +
                      "</DOCNO>\n<TITLE>"+movie_title+"</TITLE>\n<GENRE>"+movie_genres+"</GENRE>\n<TEXT>\n" + str(subtitle_text) + "\n</TEXT>\n</DOC>\n")

output_file.close()
