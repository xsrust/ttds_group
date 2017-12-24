# TTDS Group Project

Text Technologies for Data Science Group Project

#### Make sure to install python-opensubtitles inside the folder where the getSubtitles.py file is
Link: https://github.com/agonzalezro/python-opensubtitles

Command for the lazy ones:
```
pip install -e git+https://github.com/agonzalezro/python-opensubtitles#egg=python-opensubtitles
```

- ```films.json``` contains all the movies with their genre and IMDB id.
- ```getSubtitles.py``` contains a Class with useful functions for downloading the subtitles.
- ```downloadAll.py``` is a script to loop over the films.json and download the subtitles (outputs subtitles into a 'subtitles' folder and a 'notFound.txt' for the movies that didn't have subtitles available or OpenSubtitles denied access to because of the daily download limit).
