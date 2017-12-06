from pythonopensubtitles.opensubtitles import OpenSubtitles

class OpenSubs:
    def __init__(self, username,password):
        """Instantiate the shit out of this

        Arguments:
            - username (str): Your OpenSubtitles username
            - password (str): Your OpenSubtitles password

        Returns:
            - Sets all parameters of the class.
        """
        self.username = username
        self.password = password
        self.opensubs = OpenSubtitles()
        self.token = self.opensubs.login(self.username,self.password)
        assert self.token != None, "Incorrect username/password (or something else went wrong when loging in...)"

    def subtitlesLink(self,imdbID, language="eng"):
        """Get download link for a movie's subtitles

        Arguments:
            - imdbID (str): IMDB ID of the movie (with or without the "tt" prefix)
            - language (str): ISO 639-2 Code for the language you want the subtitles in (English by default)
                              Check http://www.loc.gov/standards/iso639-2/php/code_list.php for other language codes

        Returns:
            - subtitlesLink (str): Link to the subtitles file
        """

        # Process imdbID
        if(imdbID.startswith("tt")):
            imdbID = imdbID[2:]

        # Create search parameters dict
        searchParams = {}
        searchParams["sublanguageid"] = language
        searchParams["imdbid"] = str(imdbID)

        # Make sure it downloaded something
        returnedDict = self.opensubs.search_subtitles([searchParams])
        assert returnedDict != None, "OpenSubtitles returned nothing, check that you input the correct IMDBid and you input the correct username and password when instantiating this object."

        # Index 0 for top result
        return returnedDict[0]['SubDownloadLink']
