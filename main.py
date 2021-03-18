from application import MovieService
from art import text2art
import sqlite3
from movies import create_db

create_db()
print(text2art("MovieService"))

run = True
while run:
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    movie_service = MovieService(connector=conn, cursor=c)
    command = input("What would you like to do? Write 'help' to get list of commands. ")
    if command.lower() == 'help':
        print("""
        add - Add movie
        rem - Remove movie.
        all - List all saved movies.
        best - Display the top rated saved IMDB movie.
        hmb - Display the highest-grossing movie.
        avg - Display the average rating of saved movies.
        exit - Exit script
        """)

    elif command.lower().strip() == 'add':
        movie = input("Write name of movie you want to save: ")
        movie_service.add_movie(movie, connector=conn, cursor=c)

    elif command.lower().strip() == 'rem':
        movie = input("Write name of movie you want to remove: ")
        movie_service.remove_movie(movie, connector=conn, cursor=c)

    elif command.lower().strip() == 'all':
        print(movie_service.movie_list)

    elif command.lower().strip() == 'best':
        movie_service.show_best(connector=conn, cursor=c)

    elif command.lower().strip() == 'hmb':
        movie_service.show_high_gross(connector=conn, cursor=c)

    elif command.lower().strip() == 'avg':
        movie_service.show_average_rating(connector=conn, cursor=c)

    elif command.lower().strip() == 'exit':
        run = False

    conn.commit()
