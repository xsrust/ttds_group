import json
import os
import sys

import getSubtitles

# Start downloading from index provided in command line
start = int(sys.argv[1])

# Username passwords array
unames_pwds_idx = 0
unames_pwds = [("sera_maza@hotmail.com", "asdfg"), ("serafinmazadominguez@gmail.com", "asdfg"),
               ("sera_maza@icloud.com", "asdfg"), ("amjolao@gmail.com", "asdfg"), ("afghasdfh@gmail.com", "asdfg")]

# Load films json
with open('films.json') as file_:
    films_json = json.load(file_)

# Instantiate OpenSubtitles downloader from getSubtitles.py
downloader = getSubtitles.OpenSubs(unames_pwds[unames_pwds_idx][0], unames_pwds[unames_pwds_idx][1])

# Instantiate file for tracking missing subtitles
notFound = open('notFound.txt', 'w')

# Use json from provided index on
for idx, x in enumerate(films_json[start:]):
    print(start + idx, ': Downloading subtitles for', x['title'], 'with id', x['id'])

    # If error 404
    if (downloader.downloadSubtitles(x['id']) == 404):
        # Write in notFound file
        notFound.write(x['id'] + "\t" + x['title'] + "\t" + str(404) + "\n")

        # If there are available username-password pairs use a new one
        if(unames_pwds_idx < len(unames_pwds) - 1):
            unames_pwds_idx += 1
            print("Error 404, trying new username-password tuple: ", str(unames_pwds[unames_pwds_idx]))
            downloader = getSubtitles.OpenSubs(unames_pwds[unames_pwds_idx][0], unames_pwds[unames_pwds_idx][1])
        # Else finish
        else:
            print("Sorry, ran out of username-password tuples to use. You'll have to wait a few hours (or register some more emails...)")
            break

    # If subtitles not available in OpenSubtitles write to notFound and continue
    if (downloader.downloadSubtitles(x['id']) == -999):
        notFound.write(x['id'] + "\t" + x['title'] + "\t" + str(-999) + "\n")
        continue

    # Download actual subtitles
    downloader.downloadSubtitles(x['id'])

# Feedback and close file.
print("Processed", idx + 1, "films. Last film processed's index = ", start + idx)
print("Bye.")
notFound.close()
