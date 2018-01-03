import pysrt

class SRTSubtitle:
    """Class encapsulation for SRT subtitle."""

    def __init__(self,path,encoding=None):
        """Instantiate
        Arguments:
            path (str) - Path to str file
            encoding_ (str: 'utf-8') - encoding to use when oepning the file.
        """

        self.name = path.split("/")[-1][:-4]

        # Set encoding to 'utf-8' unless specified in the instantiation
        self.encoding = 'utf-8'
        if encoding:
            self.encoding = encoding

        # Open subtitles file
        try:
            self.subtitle = pysrt.open(path)
            print("Subtitles file successfully loaded with encoding \'" + self.encoding + "\'.")
        except UnicodeDecodeError:
            print("Error interpreting the subtitles as "+ self.encoding+". Are these subtitles in English? Try selecting a different encoding using the 'encoding' argument.")

        assert self.subtitle, "Subtitle loaded but it appears to be empty. Wrong encoding selected (maybe?)"


    def toText(self):
        """Return string containing all the captions from the file"""
        self.subtitle.text
