import media
import fresh_tomatoes

finding_dory = media.Movie("Finding Dory",
                           "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
                           "https://www.youtube.com/watch?v=JhvrQeY3doI")

zootopia = media.Movie("Zootopia",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=CzvH6_e2a-U")

trainwreck = media.Movie("Trainwreck",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/c/c5/Trainwreck_poster.jpg/220px-Trainwreck_poster.jpg",
                         "https://www.youtube.com/watch?v=2MxnhBPoIx4")

the_good_dinosaur = media.Movie("The Good Dinosaur",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/The_Good_Dinosaur_poster.jpg/220px-The_Good_Dinosaur_poster.jpg",
                                "https://www.youtube.com/watch?v=O-RgquKVTPE")

gone_girl = media.Movie("Gone Girl",
                        "https://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
                        "https://www.youtube.com/watch?v=2-_-1nJf8Vg")

her = media.Movie("Her",
                  "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
                  "https://www.youtube.com/watch?v=dJTU48_yghs&t=7s")



movies = [finding_dory, zootopia, trainwreck, the_good_dinosaur, gone_girl, her]

fresh_tomatoes.open_movies_page(movies)
