class Movie:
    def __init__(self, movie_title, year, rating):
        self._movie_title = movie_title
        self._movie_year = year
        self._rating = rating
        self.cast = {}

    def __repr__(self):
        return '"{0}" ({1})'.format(self._movie_title, self._movie_year)

    def __eq__(self, other):
        return str(self) == str(other)

    def get_title(self):
        return self._movie_title

    def get_year(self):
        return self._movie_year

    def get_rating(self):
        return self._rating

    def change_rating(self, rating):
        self._rating = rating

    def add_actor(self, actor, actor_id):
        self.cast[actor_id] = actor
        return True
