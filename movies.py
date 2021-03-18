import sqlite3


def create_db():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS MOVIES
                 ([ID] INTEGER PRIMARY KEY AUTOINCREMENT,[Title] text, [Ratings] text, [Homebox] real, [IMDB] real)''')
    conn.commit()


def select_all_movies(connector, cursor):
    conn = connector
    c = cursor
    c.execute("SELECT * FROM MOVIES")
    rows = c.fetchall()
    conn.commit()
    movie_list = []
    for row in rows:
        movie_list.append(row[1])
    return movie_list


def add_movie(connector, cursor, title, new_ratings, highest_gross, imdb_rating):
    conn = connector
    c = cursor
    query = "INSERT INTO MOVIES (Title, Ratings, Homebox, IMDB) VALUES (?,?,?,?)"
    c.execute(query, (title, new_ratings, highest_gross, imdb_rating))
    conn.commit()


def deleteRecord(movie, connector, cursor):
    conn = connector
    c = cursor
    sql_delete_query = """delete from MOVIES where Title = ?"""
    c.execute(sql_delete_query, [movie])
    conn.commit()
    print(f"{movie} deleted from database or not in database.")


def get_best(connector, cursor):
    conn = connector
    c = cursor
    sql_getbest_query = """SELECT Title, IMDB FROM MOVIES ORDER BY IMDB DESC LIMIT 1"""
    c.execute(sql_getbest_query)
    record = c.fetchall()
    conn.commit()
    title = record[0][0]
    imdb = record[0][1]
    best_movie = "'{0}' IMDB rating: {1}".format(title, imdb)
    print(best_movie)


def get_highest_gross(connector, cursor):
    conn = connector
    c = cursor
    sql_getbest_query = """SELECT Title, Homebox FROM MOVIES ORDER BY Homebox DESC LIMIT 1"""
    c.execute(sql_getbest_query)
    record = c.fetchall()
    conn.commit()
    title = record[0][0]
    imdb = int(record[0][1])
    highest_gross = "'{0}' Homebox: ${1}".format(title, imdb)
    print(highest_gross)


def get_average_rating(connector, cursor):
    conn = connector
    c = cursor
    sql_getbest_query = """SELECT AVG(IMDB) FROM MOVIES"""
    c.execute(sql_getbest_query)
    record = c.fetchall()
    conn.commit()
    avg = round(float(record[0][0]), 2)
    highest_gross = "Average of all saved movies is: {0}".format(avg)
    print(highest_gross)


def check_movie(movie, connector, cursor):
    conn = connector
    c = cursor
    sql_check_query = """SELECT Title FROM MOVIES"""
    c.execute(sql_check_query)
    rows = c.fetchall()
    conn.commit()
    should_continue = True
    for row in rows:
        if row[0] == movie:
            should_continue = False
    return should_continue
