import webbrowser  # import webbrowser module to launch youtube


class Movie(object):  # create class for Movie instances
    '''A class for containing movie data'''

    def __init__(self, movie_title, movie_storyline,
                    poster_image, trailer_youtube):  # constructor for Movie
        self.title = movie_title  # movie attribute
        self.storyline = movie_storyline  # movie attribute
        self.poster_image_url = poster_image  # movie attribute
        self.trailer_youtube_url = trailer_youtube  # movie attribute

    def show_trailer(self):  # method for launching youtube trailer
        webbrowser.open(self.trailer_youtube)
        #  something with the request library
