# TTDS Group Project

Text Technologies for Data Science Group Project

## Module contains:

- ```films.json``` contains all the movies with their genre and IMDB id.

- ```subtitlesBabe.collection``` submodule:
  - ```getSubtitles``` contains a Class with useful functions for downloading the subtitles.
  - ```downloadAll``` is a script to loop over the films.json and download the subtitles (outputs subtitles into a 'subtitles' folder and a 'notFound.txt' for the movies that didn't have subtitles available or OpenSubtitles denied access to because of the daily download limit).
  - ```subtitlesBabe.collection.reDownload``` script to loop over not_found.txt and try redownload subtitles.

- ```subtitlesBabe.processing``` submodule:
  - ```readSubtitles``` contains classes to read different subtitle formats.


#### Make sure to install python-opensubtitles inside the folder where the getSubtitles.py file is
Link: https://github.com/agonzalezro/python-opensubtitles
```
pip install -e git+https://github.com/agonzalezro/python-opensubtitles#egg=python-opensubtitles
```

for ```subtitlesBabe.processing.readSubtitles``` please intall ```pysrt``` with 
```
pip install pysrt
```

