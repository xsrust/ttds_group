# Subtitles Module
This module contains the code we used for the data collectiona and data processing part of our project.

## Collections Submodule
Inside the [```collection```](https://github.com/xsrust/ttds_group/tree/master/subtitles-module/collection) submodule we can find the file [```getSubtitle.py```](https://github.com/xsrust/ttds_group/blob/master/subtitles-module/collection/getSubtitles.py) which contains a custom class for OpenSubtitles ```OpenSubs``` which makes use of the [python-opensubtitles](https://github.com/agonzalezro/python-opensubtitles) module. The class has two functions that can retrieve subtitle information from OpenSubtitles and download the actual subtitles.

The files [```script-downloadAll.py```](https://github.com/xsrust/ttds_group/blob/master/subtitles-module/collection/script-downloadAll.py) [```script-reDownload.py```](https://github.com/xsrust/ttds_group/blob/master/subtitles-module/collection/script-reDownload.py) are the scripts we used to download the subtitles form the film jsons (see [```jsons```](https://github.com/xsrust/ttds_group/tree/master/jsons) folder).

## Processing Submodule
Inside the [```processing```](https://github.com/xsrust/ttds_group/tree/master/subtitles-module/processing) submodule we can find the [```readSubtitles.py```](https://github.com/xsrust/ttds_group/blob/master/subtitles-module/processing/readSubtitles.py) which contains a custom class ```superSubtitle``` that can read subtitles in .srt (with the help of [pysrt](https://github.com/byroot/pysrt)), .sub, .txt, .tmp, .ssa, and .smi and return a string with all the text from such subtitles.

The file [```script-trec.py```](https://github.com/xsrust/ttds_group/blob/master/subtitles-module/processing/script-trec.py) is a script we used to create [TREC](http://trec.nist.gov)-like XML collections for our dataset.
