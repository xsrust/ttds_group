import pysrt
import os
import sys
import re

class superSubtitle:
    def __init__(self,path,encoding=None,verbose=False):
        """Instantiate
        Arguments:
            path (str)          - Path to subtitle file
            encoding (str=None) - Encoding to use when oepning the file.
        """
        self.name = path.split("/")[-1][:-4]
        self.extension = path.split("/")[-1][-3:]
        # Set encoding to UTF-8 unless otherwise specified
        self.encoding = encoding if encoding else 'utf-8'

        try:
            if self.extension == "srt":
                self.subtitle = pysrt.open(path,encoding=self.encoding)
                assert self.subtitle, "Subtitle loaded but it appears to be empty. Wrong encoding selected (maybe?)"
            else:
                self.subtitle = open(path,encoding=self.encoding).read()

            if verbose:
                print("Subtitles file successfully loaded with encoding \'" + self.encoding + "\'.")
        except UnicodeDecodeError as e:
            if verbose:
                print(e)
                print("Error interpreting the subtitles as "+ self.encoding+". Are these subtitles in English? Try selecting a different encoding using the 'encoding' argument.")
            try:
                if self.extension == 'srt':
                    self.subtitle = pysrt.open(path,encoding='latin-1')
                    assert self.subtitle, "Subtitle loaded but it appears to be empty. Wrong encoding selected (maybe?)"
                else:
                    self.subtitle = open(path,encoding='latin-1').read()

                if verbose:
                    print("Subtitles file successfully loaded with encoding \'" + 'latin-1' + "\'.")
            except UnicodeDecodeError as e:
                if verbose:
                    print(e)
                    print("Error interpreting the subtitles as "+ 'latin-1'+". Are these subtitles in English? Try selecting a different encoding using the 'encoding' argument.")
                print('Error loading subtitle' + self.name + self.extension)

    def toText(self):
        """Return string containing all the captions from the file"""
        text = ""

        if(self.extension == 'srt'):
            return self.subtitle.text

        elif(self.extension == 'sub'):
            for x in self.subtitle.split("\n"):
                match = re.findall(r"{\d*}{\d*}(.*)",x)
                if match:
                    text += match[0] +"\n"
            return text

        elif(self.extension == 'txt'):
            for x in self.subtitle.split("\n"):
                if x.startswith('[') or re.match(r'^\d\d:\d\d:\d\d.\d\d,\d\d:\d\d:\d\d.\d\d', x):
                    continue
                else:
                    text += x+'\n'
            return text

        elif(self.extension == 'smi'):
            started = False
            for x in self.subtitle.split("\n"):
                if not started:
                    if x.startswith('<SYNC'):
                        started = True
                elif not x.startswith('<'):
                    text += x+"\n"
            return text

        elif(self.extension == 'ssa'):
            started = False
            for x in self.subtitle.split("\n"):
                if not started:
                    if x.startswith('[Events]'):
                        started = True
                elif not x.startswith('Format:'):
                    match = re.findall(r".*:.*,.*,.*,.*,.*,.*,.*,.*,(.*)",x)
                    if match:
                        text += match[0]+"\n"
            return text

        elif(self.extension == 'tmp'):
            for x in self.subtitle.split("\n"):
                match = re.findall(r"\d\d:\d\d:\d\d:(.*)",x)
                if match:
                    text += match[0] + "\n"
            return text
