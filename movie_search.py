import psycopg2
import csv

conn = psycopg2.connect("dbname=movie_match user=mattjoyce host=/tmp/")

cur = conn.cursor()

search = input("""What movie info would you like to see?
\n Enter t for title
\n Enter y for the year it was released
\n Enter d for directors
\n press enter to add a film to the list\n """)

# if search == 't':
#     title = input('What movie title would you like? ')
#
#
#     cur.execute
#
# if search == 'y':
#     rd = input('What year would you like? ')
#
#     cur.execute
#
#
# if search == 'd':
#     director = input("Which director would you like? ")
#
#     cur.execute


if search == '':
    title = input('What is the movie\'s title? ')
    rd = input('What year was the movie released? ')
    genre = input('What type of movie is it? ')
    director = input('Who made the movie? ')
    budget = input('How much was the movie made for? ')
    gross = input('How much did the movie make? ')

    cur.execute("INSERT INTO Movies (Title, ReleaseYear, Genre, Director, Budget, Gross) VALUES (%s %s %s %s %s %s)", (title, rd, genre, director, budget, gross))
    cur.execute("SELECT * from Movies WHERE title = '{}';".format(title))
    abcd = cur.fetchall()
    print(abcd)
