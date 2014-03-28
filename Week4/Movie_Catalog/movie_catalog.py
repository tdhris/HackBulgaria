from sql_adapter import SQLAdapter
from command_parser import CommandParser
from movie import Movie
from actor import Actor
import sys


class MovieCatalog:
    def __init__(self):
        self.commandparser = CommandParser()
        self.adapter = SQLAdapter()
        self.movies = {}
        self.actors = {}

        self.initialize_functions()
        self.load_initial_state()
        self.program_loop()

    def add_movie(self, arguments):
        title = input("title> ")
        year = input("year> ")
        rating = input("rating> ")
        movie = Movie(title, year, rating)

        #add movie only if it's not already in the catalog
        for movie_in_catalog in self.movies.values():
            if movie_in_catalog == movie:
                print("{0} is already in your catalog!".format(movie))
                return False

        #when a movie is saved in the database, the adapter returns its id
        movie_id = self.adapter.save_movie(movie)
        self.movies[movie_id] = movie
        print("{0} was added to your catalog!".format(movie))
        return True

    def remove_movie(self, arguments):
        movie_id = int(arguments[0])
        del self.movies[movie_id]
        self.adapter.remove_movie(movie_id)

    def add_actor(self, arguments):
        movie_id = int(arguments[0])
        #if no actor id is given then the actor hasn't been added to the db
        #in which case we need to add him/her and get the actor_id
        if len(arguments) == 1:
            name = input("name> ")
            actor = Actor(name)
            actor_id = self.adapter.save_actor(actor)
            self.actors[actor_id] = actor
        else:
            actor_id = int(arguments[1])
            actor = self.adapter.get_actor(actor_id)

        #add the movie_id<->actor_id relation to the relation table
        self.adapter.add_actor_to_movie(movie_id, actor_id)
        #add the actor to the cast in the movie dictionary of the catalog
        self.movies[movie_id].cast[actor_id] = actor
        print("{0} was added to the list of actors of {1}".format(
              actor, self.movies[movie_id]))

    def list_movies(self, arguments):
        for movie_id, movie in self.movies.items():
            print("[{0}] {1}".format(movie_id, movie))

    def list_actors(self, arguments):
        for actor_id, actor in self.actors.items():
            print("[{0}] {1}".format(actor_id, actor))

    def movie_info(self, arguments):
        movie_id = int(arguments[0])
        movie = self.movies[movie_id]
        print("Title: {0}".format(movie.get_title()))
        print("Year: {0}".format(movie.get_year()))
        cast = [actor.get_name() for actor in movie.cast.values()]
        print("Cast: {0}".format(', '.join(cast).rstrip(', ')))
        print("Rating: {0}".format(movie.get_rating()))

    def actor_info(self, arguments):
        actor_id = int(arguments[0])
        actor = self.actors[actor_id]
        print("{0} stars in:".format(actor,))
        for movie_id, movie in self.movies.items():
            if actor_id in movie.cast:
                print("[{0}] {1}".format(movie_id, movie))

    def find_movies(self, arguments):
        rating = int(arguments[0])
        found_movies = False
        print("Movies with {0} stars:".format(str(rating)))
        for movie_id, movie in self.movies.items():
            if movie.get_rating() == rating:
                found_movies = True
                print("[{0}] {1}".format(movie_id, movie))
        if not found_movies:
            print("-- there are no movies with {0} stars --".format(str(rating)))

    def rate_movie(self, arguments):
        movie_id = int(arguments[0])
        rating = input("rating> ")

        self.movies[movie_id].change_rating(rating)
        self.adapter.update_rating(movie_id, rating)

    def exit(self, arguments):
        sys.exit(0)

    def load_initial_state(self):
        self.movies = self.adapter.load_movies()
        self.actors = self.adapter.load_actors()

    def initialize_functions(self):
        #add functions to the dictionary of functions the parser recognizes
        self.commandparser.on("add_movie", self.add_movie)
        self.commandparser.on("add_actor", self.add_actor)
        self.commandparser.on("list_movies", self.list_movies)
        self.commandparser.on("list_actors", self.list_actors)
        self.commandparser.on("rate_movie", self.rate_movie)
        self.commandparser.on("find_movies", self.find_movies)
        self.commandparser.on("movie_info", self.movie_info)
        self.commandparser.on("actor_info", self.actor_info)
        self.commandparser.on("remove_movie", self.remove_movie)
        self.commandparser.on("exit", self.exit)

    def program_loop(self):
        while True:
            command = input("> ")
            self.commandparser.take_command(command)

if __name__ == '__main__':
    MovieCatalog()
