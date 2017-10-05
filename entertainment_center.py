import media
import fresh_tomatoes


# Initialize movies to be listed on the webpage
john_wick = media.Movie(
    "John Wick",
    "https://upload.wikimedia.org/wikipedia/en/thumb/9/98/John_Wick_TeaserPoster.jpg/220px-John_Wick_TeaserPoster.jpg",  # NOQA
    "An ex-assassin seeks revenge for the death of his dog",
    "https://www.youtube.com/watch?v=RllJtOw0USI"
    )


the_expendables = media.Movie(
    "The Expendables",
    "https://upload.wikimedia.org/wikipedia/en/7/76/Expendablesposter.jpg",  # NOQA
    "An elite group of mercenaries carry out all sorts of missions",
    "https://www.youtube.com/watch?v=8KtYRALe-xo"
    )

it_movie = media.Movie(
    "IT",
    "https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg",  # NOQA
    "A strange town where a clown has an appetite for children",
    "https://www.youtube.com/watch?v=hAUTdjf9rko"
    )

kingsman_2 = media.Movie(
    "Kingsman: The Golden Circle",
    "https://upload.wikimedia.org/wikipedia/en/f/fb/Kingsman_The_Golden_Circle.png",  # NOQA
    "A British secret agent saves the world",
    "https://www.youtube.com/watch?v=0fvqnGmr9S8"
    )

american_made = media.Movie(
    "American Made",
    "https://upload.wikimedia.org/wikipedia/en/c/ca/American_Made_%28film%29.jpg",  # NOQA
    "A drug smuggler is hired by the CIA",
    "https://www.youtube.com/watch?v=AEBIJRAkujM"
    )

blade_runner_2049 = media.Movie(
    "Blade Runner 2049",
    "https://upload.wikimedia.org/wikipedia/en/2/27/Blade_Runner_2049_logo.png",  # NOQA
    "A detective is on the look out for replicated human beings",
    "https://www.youtube.com/watch?v=gCcx85zbxz4"
    )

# Set the movies that will be passed in to the media file
movies = [john_wick,
          the_expendables,
          it_movie,
          kingsman_2,
          american_made,
          blade_runner_2049
          ]

# Open HTML file in a web browswer via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
