import webbrowser


# create class: Movie
class Movie():


    """Initializes the class "Movie" to create movie objects
       that have a title, storyline, poster image, and playable trailer"""
    
    # Valid ratings to be given to Movies (currently unused)
    VALID_RATINGS=["G","PG","PG13","R"]

    # define the initializing constructor for class: Movie
    def __init__(self,movie_title,movie_storyline, poster_image, trailer_youtube):
        # initilizing instance variables with passed parameters from entertainment.py
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url =trailer_youtube

    # open web browser to play trailer from youtube url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

