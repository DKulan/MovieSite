import webbrowser


# Create class that stores movie information for a specific movie
class Movie():
    """Stores all relevant information for movies"""
    def __init__(self, title, poster_image_url,
                 movie_desc, trailer_youtube_url):
                self.title = title
                self.poster_image_url = poster_image_url
                self.moviedesc = movie_desc
                self.trailer_youtube_url = trailer_youtube_url

        # Method that uses the web browser to show movie trailers via YouTube
    def show_trailer(self):
                webbrowser.open(self.movietrailer)
