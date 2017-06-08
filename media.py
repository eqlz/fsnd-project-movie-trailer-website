import webbrowser

class Movie():
    """This a class is used to store movie information"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Assign movie related information to an instance of Movie.

        Args:
           title: A string of a movie title.
           poster_image_url: A string of a URL directing to the poster of a movie.
           trailer_youtube_url: A string of a URL directing to the trailer of a movie.
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Open a link of a movie trailer in a new tab.
        """
        webbrowser.open(self.trailer_youtube_url)
    
