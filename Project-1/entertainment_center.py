"""
File:     entertainment_center.py
Course:   Udacity Full-Stack Developer Nanodegree
Project:  Movies Website
Author:   Dima K
Date:     Aug 2017
"""

# Import modules
from media import Movie
import fresh_tomatoes

print("Running..." + __doc__)

# Define 6 Oscars movies
oscars_movie_list = [
    Movie("Moonlight", "2017",
          "A chronicle of the childhood, adolescence and burgeoning adulthood of a young, African-American, gay man growing up in a rough neighborhood of Miami.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQxNTIyODAxMV5BMl5BanBnXkFtZTgwNzQyMDA3OTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=9NJj12tJzqc"),
    Movie("Spotlight", "2016",
          "The true story of how the Boston Globe uncovered the massive scandal of child molestation and cover-up within the local Catholic Archdiocese, shaking the entire Catholic Church to its core.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyOTM5OTIzNV5BMl5BanBnXkFtZTgwMDkzODE2NjE@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=EwdCIpbTN5g"),
    Movie("Birdman", "2015",
          "A washed-up actor, who once played a famous superhero, attempts to revive his career by writing and starring in a Broadway play.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BODAzNDMxMzAxOV5BMl5BanBnXkFtZTgwMDMxMjA4MjE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=uJfLoE6hanc"),
    Movie("12 Years a Slave", "2014",
          "In the antebellum United States, Solomon Northup, a free black man from upstate New York, is abducted and sold into slavery.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTEzODkyN15BMl5BanBnXkFtZTcwNTU4NTc4OQ@@._V1_.jpg",
          "https://www.youtube.com/watch?v=z02Ie8wKKRg"),
    Movie("Argo", "2013",
          "Acting under the cover of a Hollywood producer scouting a location for a science fiction film, a CIA agent launches a dangerous operation to rescue six Americans in Tehran during the U.S. hostage crisis in Iran in 1980.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc3MjI0MjM0NF5BMl5BanBnXkFtZTcwMTYxMTQ1OA@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=JW3WfSFgrVY"),
    Movie("The Artist", "2012",
          "A silent movie star meets a young dancer, but the arrival of talking pictures sends their careers in opposite directions.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMzk0NzQxMTM0OV5BMl5BanBnXkFtZTcwMzU4MDYyNQ@@._V1_.jpg",
          "https://www.youtube.com/watch?v=YB9Oq0hn5KY")
]

# Define 6 top Box Office movies
top_movies_list = [
    Movie("Avatar", "2009",
          "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
          "https://www.youtube.com/watch?v=5PSNL1qE6VY"),
    Movie("Titanic", "1997",
          "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SY1000_CR0,0,671,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=zCy5WQ9S4c0"),
    Movie("Star Wars: The Force Awakens", "2015",
          "Three decades after the Empire's defeat, a new threat arises in the militant First Order. Stormtrooper defector Finn and spare parts scavenger Rey are caught up in the Resistance's search for the missing Luke Skywalker.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=sGbxmsDFVnE"),
    Movie("Jurassic World", "2015",
          "A new theme park, built on the original site of Jurassic Park, creates a genetically modified hybrid dinosaur, which escapes containment and goes on a killing spree.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BNWEyNTE0YTEtY2FkMi00MmY3LTg4MWMtODdjYjRkNGM4ZTZhXkEyXkFqcGdeQXVyMzI0NDc4ODY@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=RFinNxS5KN4"),
    Movie("The Avengers", "2012",
          "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=eOrNdBpGMv8"),
    Movie("Furious 7", "2015",
          "Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQxOTA2NDUzOV5BMl5BanBnXkFtZTgwNzY2MTMxMzE@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=Skpu5HaVkOc")
]

# Define 6 other random movies
other_movies_list = [
    Movie("The Accountant", "2016",
          "As a math savant uncooks the books for a new client, the Treasury Department closes in on his activities, and the body count starts to rise.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BNDc5Mzg2NTYxNV5BMl5BanBnXkFtZTgwMjQ2ODAwOTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=fkPJ3aENjvM"),
    Movie("Manchester by the Sea", "2016",
          "A depressed uncle is asked to take care of his teenage nephew after the boy's father dies.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxMjk0NDg4Ml5BMl5BanBnXkFtZTgwODcyNjA5OTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=gsVoD0pTge0"),
    Movie("Beauty and the Beast", "2017",
          "An adaptation of the fairy tale about a monstrous-looking prince and a young woman who fall in love.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUwNjUxMTM4NV5BMl5BanBnXkFtZTgwODExMDQzMTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=OvW_L8sTu5E"),
    Movie("Bushwick", "2017",
          "When a Texas military force invades their Brooklyn neighborhood, 20-year-old Lucy and war veteran Stupe must depend on each other to survive.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BMGQ5Mjc1ZTUtYzVhOS00YWEwLThkYjItNmNhN2ViMDBlZGZlXkEyXkFqcGdeQXVyMzQwMTY2Nzk@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=jMi7A20TXoU"),
    Movie("Death Wish", "2017",
          "A mild-mannered father is transformed into a killing machine after his family is torn apart by a violent act.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BNjUxNDcyMjgwOV5BMl5BanBnXkFtZTgwMzY5NjAxMzI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
          "https://www.youtube.com/watch?v=HqOgkEZDSYc"),
    Movie("Mine", "2016",
          "After a failed assassination attempt, a soldier finds himself stranded in the desert. Exposed to the elements, he must survive the dangers of the desert and battle the psychological and physical tolls of the treacherous conditions.",
          "https://images-na.ssl-images-amazon.com/images/M/MV5BNzVjZTdjMWYtZmFhNS00MDRmLTgyNDktYzQwM2M1ZDQyMTg3XkEyXkFqcGdeQXVyNDExMzMxNjE@._V1_SY1000_SX675_AL_.jpg",
          "https://www.youtube.com/watch?v=KdB5iPt-G3w")
]

# Open movies web page
fresh_tomatoes.open_movies_page(
    oscars_movie_list, top_movies_list, other_movies_list)
