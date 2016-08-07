import media
import fresh_tomatoes

marvelous_middos = media.Movie("Marvelous Middos Machine",
	"An inventer helps children improve charecter",
	"http://www.ibm.com/developerworks/data/library/techarticle/dm-0504stolze/test_1.jpg",
	"https://www.youtube.com/watch?v=gxitJO8-qQI")

atheist_convention = media.Movie("Athiest Convention in LA",
	"A group of athiests become religious when plane egine fails on their way a convention.",
	"http://gbaa.org/wp-content/uploads/2014/08/airplane.jpg",
	"https://www.youtube.com/watch?v=zdsD2pcGt8o")

sfashkenaz = media.Movie("Sfashkenaz",
	"A Chasid and Sephardic Jew become best friends",
	"http://www.linkorangutan.com/wp-content/themes/thesis_16/custom-sample/rotator/sample-4.jpg",
	"https://www.youtube.com/watch?v=kG1P3S6tyFE")

movies = [marvelous_middos, atheist_convention, sfashkenaz]
# This calls the final function in fresh_tomatoes that opens
# the browser with the movie website
fresh_tomatoes.open_movies_page(movies)

# I copied my code from the demonstrasion in the video.