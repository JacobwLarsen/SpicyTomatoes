import webbrowser


#create class: Movie
class Movie():


    """Documentation"""

    VALID_RATINGS=["G","PG","PG13","R"]

    #define the initializing constructor for class: Movie
    def __init__(self,movie_title,movie_storyline, poster_image, trailer_youtube):
        #print("Movie Constructor Called")
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url =trailer_youtube

    #open web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

