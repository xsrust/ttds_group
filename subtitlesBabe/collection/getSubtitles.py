import errno
import os
import urllib.request

# MAKE SURE YOU HAVE https://github.com/agonzalezro/python-opensubtitles INSTALLED
from pythonopensubtitles.opensubtitles import OpenSubtitles


class OpenSubs:
    def __init__(self, username, password):
        """Instantiate the shit out of this

        Arguments:
            - username (str): Your OpenSubtitles username
            - password (str): Your OpenSubtitles password

        Returns:
            - Nothing: Sets all parameters of the class.
        """
        self.username = username
        self.password = password
        self.opensubs = OpenSubtitles()
        self.token = self.opensubs.login(self.username, self.password)
        assert self.token != None, "Incorrect username/password (or something else went wrong when loging in...)"

    def subtitlesInfo(self, imdbID, language="eng"):
        """Get info from OpenSubtitles for a movie'

        Arguments:
            - imdbID (str): IMDB ID of the movie (with or without the "tt" prefix)
            - language (str): ISO 639-2 Code for the language you want the subtitles in (English by default)
                              Check http://www.loc.gov/standards/iso639-2/php/code_list.php for other language codes

        Returns:
            If subtitles found:
                - subtitlesInfo (dict): Dictionary containing information about the movie's subtitles, including download links.
            Otherwise:
                - None

        """

        # Process imdbID to remove TT
        if(imdbID.startswith("tt")):
            imdbID = imdbID[2:]

        # Create search parameters dict
        searchParams = {}
        searchParams["sublanguageid"] = language
        searchParams["imdbid"] = str(imdbID)

        # Make sure it downloaded something
        returnedDict = self.opensubs.search_subtitles([searchParams])
        assert returnedDict != None, "OpenSubtitles returned nothing, check that you input the correct IMDBid and you input the correct username and password when instantiating this object."

        # Check not null
        if not returnedDict:
            return

        # Index 0 for top result
        return returnedDict[0]

    def downloadSubtitles(self, imdbID, language="eng", outputFolder=None):
        """Download whatever "subtitlesInfo(self,imdbID, language)" outputs into outputFolder

        Arguments:
            - imdbID (str): IMDB ID of the movie (with or without the "tt" prefix)
            - language (str): ISO 639-2 Code for the language you want the subtitles in (English by default)
                              Check http://www.loc.gov/standards/iso639-2/php/code_list.php for other language codes
            - outputFolder (str): FULL path to folder where you want to download subtitles.
                                  * If (outputPath == None) then outputPath = currentWorkingDirectory/subtitles
                                  * If you specify outputFolder please make sure you're inputting the FULL (and not relative) path,
                                    as well as making sure the folder already exists

        Returns:
            If subtitles found:
                - Nothing: Downloads file that subtitlesInfo outputs into outputFolder/imdbID.sub (or whatever other format OpenSubtitles returns)
            Otherwise:
                If subtitles not available in OpenSubtitles.org return (int) -999
                If HTTP error (most likely you've reached your daily download limit return (int) HTTP error code)
        """

        # Output path shenanigans
        if outputFolder == None:
            outputFolder = os.getcwd() + "/subtitles"
            # Create subtitles folder if it doesn't exist
            try:
                os.makedirs(outputFolder)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        # Process imdbID to remove TT
        if(imdbID.startswith("tt")):
            imdbID = imdbID[2:]

        # Get subtitles info
        subtitlesInfo = self.subtitlesInfo(imdbID, language)

        # If no subtitles found print warning and return -999
        if not subtitlesInfo:
            print("No subtitles found for",imdbID)
            return -999

        # Generate filename and download
        isGZ = False
        isGZ_string = subtitlesInfo['SubDownloadLink'].split(".")[-1]
        if isGZ_string == "gz":
            isGZ = True
        filename = outputFolder + "/tt" + str(imdbID) + "." + subtitlesInfo['SubFormat']
        if isGZ:
            filename+=".gz"

        try:
            # Download
            urllib.request.urlretrieve(subtitlesInfo['SubDownloadLink'], filename)

        except Exception as e:
            # If HTTP error print error and return HTTP code (e.g. 404)
            print(e)
            return e.code
