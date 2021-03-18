import requests
from movies import select_all_movies, deleteRecord, add_movie, get_best, get_highest_gross, get_average_rating, \
    check_movie

API_KEY = 'PASTE YOUR API KEY HERE'  # Write here your API KEY
URL = f'http://www.omdbapi.com/?apikey={API_KEY}'


class MovieService:

    def __init__(self, connector, cursor):
        self.movie_list = select_all_movies(connector=connector, cursor=cursor)

    def add_movie(self, movie, connector, cursor):
        conn = connector
        c = cursor
        param = {"t": movie.title()}
        response = requests.get(URL, params=param)
        try:
            movie_data = response.json()
            title = movie_data['Title']
        except KeyError:
            print("There's no such movie")
        else:
            check = check_movie(connector=conn, cursor=c, movie=title)
            if check:
                ratings = movie_data['Ratings']
                imdb_rating = ''
                for item in ratings:
                    if item['Source'] == 'Internet Movie Database':
                        imdb_rating = item['Value']
                new_ratings = str(ratings)
                try:
                    imdb_rating = float(imdb_rating[0:3])
                except ValueError:
                    imdb_rating = None
                    print('No IMDB value.')
                else:
                    try:
                        highest_gross = float(movie_data['BoxOffice'].replace('$', '').replace(',', ''))
                    except (ValueError, KeyError):
                        highest_gross = None
                        print('No information about Homebox')
                    add_movie(connector=conn, cursor=c, title=title, new_ratings=new_ratings, highest_gross=highest_gross,
                              imdb_rating=imdb_rating)
                    print(f"{movie} added")
            else:
                print('Movie already in database.')

    def remove_movie(self, movie, connector, cursor):
        deleteRecord(movie, connector=connector, cursor=cursor)

    def show_best(self, connector, cursor):
        get_best(connector, cursor)

    def show_high_gross(self, connector, cursor):
        get_highest_gross(connector, cursor)

    def show_average_rating(self, connector, cursor):
        get_average_rating(connector, cursor)
