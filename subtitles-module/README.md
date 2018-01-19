This module contains the code we used for the data collectiona dn adata processing part of our project.

Inside the [```collection```](https://github.com/xsrust/ttds_group/tree/master/subtitles-module/collection) submodule we can find the file [```getSubtitle.py```](https://github.com/xsrust/ttds_group/blob/master/subtitles-module/collection/getSubtitles.py) which contains a custom class for OpenSubtitles ```OpenSubs``` which makes use of the [python-opensubtitles](https://github.com/agonzalezro/python-opensubtitles) module. The class has two functions that can retrieve subtitle information from OpenSubtitles and download the actual subtitles.

The files [```script-downloadAll.py```]() [```script-reDownload.py```]() are the scripts we used to download the subtitles form the film jsons (see [```jsons```](https://github.com/xsrust/ttds_group/tree/master/jsons) folder).
