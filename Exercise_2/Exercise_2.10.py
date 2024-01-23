#File name: Exercise_2.10
#Author: Henry Våg
#Description: Exercise 2.10

class Movie:

    def __init__(self, name, director, genre, year):

        self.name = name
        self.director = director
        self.genre = genre
        self.year = year



def movies_of_genre(movies: list, genre: str):
    
    filtered_movies = [movie for movie in movies if movie.genre == genre]
    return filtered_movies
    


john_woo = Movie("A Better Tomorrow", "John Woo", "action", 1986)
kungfu = Movie("Chinese Odyssey","Stephen Chow","comedy",1993)
jet_li = Movie("The Legend","Corey Yuen","comedy",1993)
movies=[john_woo,kungfu,jet_li, Movie("Hero","Yimou Zhang","action",2002)]


for movie in movies_of_genre(movies,"action"):
    print(f"{movie.director}: {movie.name}")