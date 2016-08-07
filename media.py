import webbrowser


class Movie():
	def __init__(
		self, movie_title,
		""" This function assigns the necessary arguments to the instance
		of this class that will be used.
		"""
		movie_storyline, poster_image,
		trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		""" This function actualy opens the appropriate video in youtube."""
		webbrowser.open(self.trailer_youtube_url)

# I copied my code from the demonstration in the video.
