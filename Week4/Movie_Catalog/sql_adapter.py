import sqlite3
from movie import Movie
from actor import Actor


class SQLAdapter:
    def __init__(self):
        self.connection = sqlite3.connect("movie_catalog.db")
        self.cursor = self.connection.cursor()
        self.create_tables()

    def save_movie(self, movie):
        title = movie.get_title()
        year = movie.get_year()
        rating = movie.get_rating()

        self.cursor.execute("INSERT INTO movies(title, year, rating)\
                             VALUES (?, ?, ?)", (title, year, rating))

        self.connection.commit()
        return self.cursor.lastrowid

    def load_movies(self):
        self.cursor.execute("SELECT * FROM movies")
        unparsed_movies = self.cursor.fetchall()
        movies = {}
        if unparsed_movies:
            for unparsed_movie in unparsed_movies:
                #get info from database
                movie_id = unparsed_movie[0]
                title = unparsed_movie[1]
                year = unparsed_movie[2]
                rating = unparsed_movie[3]
                #create a new Movie object and add it to {movie_id: Movie}
                movie = Movie(title, year, rating)
                movie.cast = self.get_actors_in_movie(int(movie_id))
                movies[movie_id] = movie
        return movies

    def update_rating(self, movie_id, rating):
        self.cursor.execute("UPDATE movies SET rating = ?\
                             WHERE movie_id = ?", (rating, movie_id))
        self.connection.commit()

    def remove_movie(self, movie_id):
        self.cursor.execute("DELETE FROM movies WHERE movie_id = ?", (movie_id,))
        self.cursor.execute("DELETE FROM relation_table\
            WHERE movie_id = ?", (movie_id,))
        self.connection.commit()

    def save_actor(self, actor):
        name = actor.get_name()

        self.cursor.execute("INSERT INTO actors(name) VALUES (?)", (name,))
        self.connection.commit()
        return self.cursor.lastrowid

    def get_actor(self, actor_id):
        self.cursor.execute("SELECT name FROM actors WHERE actor_id = ?",
                           (int(actor_id),))
        name = self.cursor.fetchone()[0]
        actor = Actor(name)
        return actor

    def get_actors_in_movie(self, movie_id):
        self.cursor.execute("SELECT actor_id FROM relation_table\
                             WHERE movie_id = ?", (movie_id,))
        actor_ids = [actor_id[0] for actor_id in self.cursor.fetchall()]
        actors = {}
        for actor_id in actor_ids:
            self.cursor.execute("SELECT name FROM actors\
                                 WHERE actor_id = ?", (actor_id,))
            name = self.cursor.fetchone()[0]
            actor = Actor(name)
            actors[actor_id] = actor
        return actors

    def load_actors(self):
        self.cursor.execute("SELECT * FROM actors")
        unparsed_actors = self.cursor.fetchall()
        actors = {}
        if unparsed_actors:
            for unparsed_actor in unparsed_actors:
                #get actor info from database
                actor_id = unparsed_actor[0]
                name = unparsed_actor[1]
                #create an Actor instanse and add it to {actor_id: Actor}
                actor = Actor(name)
                actors[actor_id] = actor
        return actors

    def add_actor_to_movie(self, movie_id, actor_id):
        self.cursor.execute("INSERT INTO relation_table(movie_id, actor_id)\
                             VALUES (?, ?)", (movie_id, actor_id))
        self.connection.commit()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS movies
            (movie_id INTEGER PRIMARY KEY, title TEXT,
                year INTEGER, rating INTEGER)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS actors
            (actor_id INTEGER PRIMARY KEY, name TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS relation_table
                 (movie_id INTEGER, actor_id INTEGER)''')
