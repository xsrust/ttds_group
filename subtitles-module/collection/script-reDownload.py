import os
import sys
import re

import getSubtitles
start = int(sys.argv[1])
not_found_file_path = str(sys.argv[2])
output_folder = str(sys.argv[3])


# Username passwords array
unames_pwds_idx = 0
unames_pwds = [("Stiliyan", "SubPassword"), ("sera_maza@hotmail.com", "asdfg"), ("serafinmazadominguez@gmail.com", "asdfg"),
               ("sera_maza@icloud.com", "asdfg"), ("amjolao@gmail.com", "asdfg"), ("afghasdfh@gmail.com", "asdfg")]

# Load not_found.txt file
not_found_films = open(not_found_file_path, 'r',encoding="utf-8")
# Skip first 3 lines
for _ in range(3):
    next(not_found_films)

for _ in range(start):
    next(not_found_films)

# Instantiate file for tracking missing subtitles
definitely_not_found = open(output_folder + '/definitely_not_found.txt', 'w', encoding = 'utf-8')

# Instantiate OpenSubtitles downloader from getSubtitles.py
downloader = getSubtitles.OpenSubs(unames_pwds[unames_pwds_idx][0], unames_pwds[unames_pwds_idx][1])
print("Logging in with first username-password tuple: ", str(unames_pwds[unames_pwds_idx]))

assert downloader != None, ('Error logging in?!? '+ str(unames_pwds[unames_pwds_idx]))
downloaded = 0


for idx,film in enumerate(not_found_films):

    match = re.findall(r'(tt\d+)\t(.*)\t(-?\d+)',film)

    if bool(match) and len(match[0]) == 3:
        imdb_id = str(match[0][0])
        title = str(match[0][1])
        error_code = int(match[0][2])

        print(str(idx)+': Downloading film '+ title + ' with ID '+ imdb_id + ' which gave error '+ str(error_code) + ' previously' )
        download = downloader.downloadSubtitles(imdb_id, output_folder)

        if (download == 404):
            print('Error 404 while downloading '+ imdb_id)
            definitely_not_found.write(imdb_id + "\t"+title + "\t" +str(404))
            print('Trying '+ imdb_id + ' one last time...')
            download_2 = downloader.downloadSubtitles(imdb_id, output_folder)
            if (download_2 == 404):
                # Rotate between unames-pwds
                if (unames_pwds_idx < len(unames_pwds)):
                    unames_pwds_idx+=1
                else:
                    unames_pwds_idx=0
                print('Error 404 happened twice on '+ imdb_id)
                print('Switching username-password tuple: ' + str(unames_pwds[unames_pwds_idx]))
                downloader = getSubtitles.OpenSubs(unames_pwds[unames_pwds_idx][0], unames_pwds[unames_pwds_idx][1])
                continue

            if(download_2 == -999):
                print("PANIC ERROR -999?!?!?!?")
                break

            downloaded +=1

        if (download == -999):
            print('Error -999 (movie did not return any subtitles) while downloading ' + imdb_id)
            definitely_not_found.write(imdb_id + "\t"+title + "\t" +str(-999))
            continue

        downloaded +=1

print("Processed " + str(idx) + " previously-not-found films of which " + str(downloaded) + " were succesfully downloaded.")
