import media
import fresh_tomatoes

# To create an instance of class Movie by calling init function in media.py
# Finding Dory movie: title, poster image url, trailer youtube url
finding_dory = media.Movie(
    "Finding Dory",
    "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",  # NOQA
    "https://www.youtube.com/watch?v=JhvrQeY3doI")

# Zootopia movie: title, poster image url, trailer youtube url
zootopia = media.Movie(
    "Zootopia",
    "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",  # NOQA
    "https://www.youtube.com/watch?v=CzvH6_e2a-U")

# Trainwreck movie: title, poster image url, trailer youtube url
trainwreck = media.Movie(
    "Trainwreck",
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c5/Trainwreck_poster.jpg/220px-Trainwreck_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=2MxnhBPoIx4")

# The Good Dinosaur movie: title, poster image url, trailer youtube url
the_good_dinosaur = media.Movie(
    "The Good Dinosaur",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/The_Good_Dinosaur_poster.jpg/220px-The_Good_Dinosaur_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=O-RgquKVTPE")

# Gone Girl movie: title, poster image url, trailer youtube url
gone_girl = media.Movie(
    "Gone Girl",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=2-_-1nJf8Vg")

# Her movie: title, poster image url, trailer youtube url
her = media.Movie(
    "Her",
    "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=dJTU48_yghs&t=7s")

# Set the movies list that will be passed to the media file
movies = [
    finding_dory,
    zootopia,
    trainwreck,
    the_good_dinosaur,
    gone_girl, her
    ]

# Open the HTML file in a webbrowser via fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
