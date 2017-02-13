import media
import fresh_tomatoes

# create instance of class "Movie" for gladiator
gladiator = media.Movie("Gladiator",
                        "The story of a Roman general who becomes"
                            " a slave and defies an empire",
                        "https://upload.wikimedia.org/wikipedia"
                            "/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=ol67qo3WhJk")

# create instance of class "Movie" for braveheart
braveheart = media.Movie("Braveheart",
                         "The story of a man who loses everything,"
                             " but fights for Scottish independence nonetheless",
                         "https://upload.wikimedia.org/wikipedia/en"
                             "/5/55/Braveheart_imp.jpg",
                         "https://www.youtube.com/watch?v=wj0I8xVTV18")

# create instance of class "Movie" for avatar
avatar = media.Movie("Avatar",
                         "The story of a man who invades an alien colony,"
                             " but falls in love in the process",
                         "https://upload.wikimedia.org/wikipedia/en/b/b0"
                             "/Avatar-Teaser-Poster.jpg",
                         "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# create instance of class "Movie" for love_actually
love_actually = media.Movie("Love Actually",
                         "Love is in the air, everywhere I look around",
                         "https://upload.wikimedia.org/wikipedia/en/e/eb"
                            "/Love_Actually_movie.jpg",
                         "https://www.youtube.com/watch?v=KdzH6a-XEGM")

# create instance of class "Movie" for safety_not_guaranteed
safety_not_guaranteed = media.Movie("Safety Not Guaranteed",
                         "Because believing in the magic of others' dreams,"
                            " obtainable or not, creates a magic in itself",
                         "https://upload.wikimedia.org/wikipedia/en/3/3a/"
                            "SafetyNotGuaranteed.jpg",
                         "https://www.youtube.com/watch?v=73jSnAs7mq8")

# create instance of class "Movie" for guardians_of_the_galaxy
guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                         "A little music, a little action,"
                            " and a whole lot of craziness",
                         "https://upload.wikimedia.org/wikipedia"
                            "/en/8/8f/GOTG-poster.jpg",
                         "https://www.youtube.com/watch?v=d96cjJhvlMA&t=12s")

# create array of movie instances to be generated in fresh_tomatoes.py
movies_array=[gladiator,
              braveheart,
              avatar,
              love_actually,
              safety_not_guaranteed,
              guardians_of_the_galaxy]

# calling open_movies_page on the movie_array
fresh_tomatoes.open_movies_page(movies_array)
