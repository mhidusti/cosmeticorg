class Movie:
    def __init__(self, title, date, quality, movie_id):
        self.title = title
        self.date = date
        self.quality = quality
        self.movie_id = movie_id
        self.actors = []

    def add_actor(self, actor):
        self.actors.append(actor)

    def remove_actor(self, actor):
        self.actors.remove(actor)


class Actor:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def remove_movie(self, movie):
        self.movies.remove(movie)


class MovieSite:
    def __init__(self):
        self.movies = {}
        self.actors = {}

    def add_movie(self, title, date, quality):
        if len(title) > 20:
            print("invalid title")
            return
        if not (1888 <= date <= 2024):
            print("invalid date")
            return
        if quality not in ["720p", "1080p", "4K"]:
            print("invalid quality")
            return
        
        movie_id = len(self.movies)
        movie = Movie(title, date, quality, movie_id)
        self.movies[movie_id] = movie
        print(f"added successfully {movie_id}")

    def add_actor(self, name):
        actor = Actor(name)
        self.actors[name] = actor

    def assign_actor_to_movie(self, actor_name, movie_id):
        if actor_name not in self.actors:
            print("Actor not found!")
            return
        if movie_id not in self.movies:
            print("Movie not found!")
            return
        
        actor = self.actors[actor_name]
        movie = self.movies[movie_id]
        actor.add_movie(movie)
        movie.add_actor(actor)

    def remove_movie(self, movie_id):
        if movie_id not in self.movies:
            print("Movie not found!")
            return
        
        del self.movies[movie_id]
        print(f"Movie {movie_id} removed successfully")

    def remove_actor(self, actor_name):
        if actor_name not in self.actors:
            print("Actor not found!")
            return
        
        del self.actors[actor_name]
        print(f"Actor {actor_name} removed successfully")


# نمونه استفاده از کلاس‌ها
site = MovieSite()

site.add_movie("Inception", 2010, "1080p")
site.add_movie("The Shawshank Redemption", 1994, "720p")
site.add_actor("Leonardo DiCaprio")
site.add_actor("Morgan Freeman")

site.assign_actor_to_movie("Leonardo DiCaprio", 0)
site.assign_actor_to_movie("Morgan Freeman", 1)

site.remove_movie(1)
site.remove_actor("Morgan Freeman")
