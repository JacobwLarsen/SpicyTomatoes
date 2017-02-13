import webbrowser


class Movie():
    
    """Initializes the class "Movie"with a title, storyline, poster image, and playable trailer"""
    
    VALID_RATINGS = ["G","PG","PG13","R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """define the initializing constructor"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url =trailer_youtube

    def show_trailer(self):
        """open web browser to play trailer from youtube url"""
        webbrowser.open(self.trailer_youtube_url)

