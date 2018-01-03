import json
import os
import sys

import getSubtitles

# Start downloading from index provided in command line
start = int(sys.argv[1])
output_folder = str(sys.argv[2])

# Username passwords array
unames_pwds_idx = 0
unames_pwds = [("Stiliyan", "SubPassword"), ("sera_maza@hotmail.com", "asdfg"), ("serafinmazadominguez@gmail.com", "asdfg"),
               ("sera_maza@icloud.com", "asdfg"), ("amjolao@gmail.com", "asdfg"), ("afghasdfh@gmail.com", "asdfg")]

# Load films json
with open('films.json') as file_:
    films_json = json.load(file_)

# Instantiate OpenSubtitles downloader from getSubtitles.py
downloader = getSubtitles.OpenSubs(unames_pwds[unames_pwds_idx][0], unames_pwds[unames_pwds_idx][1])
print("Logging in with first username-password tuple: ", str(unames_pwds[unames_pwds_idx]))

# Instantiate file for tracking missing subtitles
not_found = open(output_folder + '/not_found.txt', 'w')

# Use json from provided index on
for idx, x in enumerate(films_json[start:]):
    print(str(start + idx) + ': Downloading subtitles for ' + str(x['title']) + ' with id ' + str(x['id']))

    download = downloader.downloadSubtitles(x['id'], output_folder)
    # If error 404
    if (download == 404):
        # If there are available username-password pairs use a new one
        if(unames_pwds_idx < len(unames_pwds) - 1):
            print("Error 404, trying one more time...")
            download_2 = downloader.downloadSubtitles(x['id'], output_folder)
            if (download_2 == 404):
                unames_pwds_idx += 1
                print("Error 404 persists, switching username-password tuple: ", str(unames_pwds[unames_pwds_idx]))
                downloader = getSubtitles.OpenSubs(unames_pwds[unames_pwds_idx][0], unames_pwds[unames_pwds_idx][1])
                not_found.write(x['id'] + "\t" + x['title'] + "\t" + str(404) + "\n")

        # Else finish
        else:
            not_found.write(x['id'] + "\t" + x['title'] + "\t" + str(404) + "\n")
            print("Sorry, ran out of username-password tuples to use. You'll have to wait a few hours (or register some more emails...)")
            break

    # If subtitles not available in OpenSubtitles write to not_found and continue
    if (download == -999):
        not_found.write(x['id'] + "\t" + x['title'] + "\t" + str(-999) + "\n")
        continue


# Feedback and close file.
print("Processed", idx + 1, "films. Last film processed's index = ", start + idx)
print("Bye.")
not_found.close()
