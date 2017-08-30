from media import Movie
import fresh_tomatoes

accountant = Movie("The Accountant",
                         "As a math savant uncooks the books for a new client, the Treasury Department closes in on his activities, and the body count starts to rise.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNDc5Mzg2NTYxNV5BMl5BanBnXkFtZTgwMjQ2ODAwOTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=fkPJ3aENjvM")

manchester = Movie("Manchester by the Sea",
                         "A depressed uncle is asked to take care of his teenage nephew after the boy's father dies.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxMjk0NDg4Ml5BMl5BanBnXkFtZTgwODcyNjA5OTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=gsVoD0pTge0")

beaty_and_beast = Movie("Beauty and the Beast",
                         "An adaptation of the fairy tale about a monstrous-looking prince and a young woman who fall in love.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUwNjUxMTM4NV5BMl5BanBnXkFtZTgwODExMDQzMTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=OvW_L8sTu5E")

bushwick = Movie("Bushwick",
                         "When a Texas military force invades their Brooklyn neighborhood, 20-year-old Lucy and war veteran Stupe must depend on each other to survive.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMGQ5Mjc1ZTUtYzVhOS00YWEwLThkYjItNmNhN2ViMDBlZGZlXkEyXkFqcGdeQXVyMzQwMTY2Nzk@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=jMi7A20TXoU")

death_wish = Movie("Death Wish",
                         "A mild-mannered father is transformed into a killing machine after his family is torn apart by a violent act.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNjUxNDcyMjgwOV5BMl5BanBnXkFtZTgwMzY5NjAxMzI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=HqOgkEZDSYc")

mine = Movie("Mine",
                         "After a failed assassination attempt, a soldier finds himself stranded in the desert. Exposed to the elements, he must survive the dangers of the desert and battle the psychological and physical tolls of the treacherous conditions.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNzVjZTdjMWYtZmFhNS00MDRmLTgyNDktYzQwM2M1ZDQyMTg3XkEyXkFqcGdeQXVyNDExMzMxNjE@._V1_SY1000_SX675_AL_.jpg",
                         "https://www.youtube.com/watch?v=KdB5iPt-G3w")

#print(accountant.storyline)

#movies = [accountant, manchester, beaty_and_beast, bushwick, death_wish, mine]

#fresh_tomatoes.open_movies_page(movies)

print(Movie.__module__)
