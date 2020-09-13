"""
- Enter 'a' to add a movie , 'l' to see your movies ,'f' to find a movie ,'q' to quit

- Add a movie 
- See movies
- Find a movie
- Stop running the program



[] : Decide where to store a movie 
[] : What is the format of a movie
[] : Show the user the main interface to get their input
[] : Allow users to add movies 
[] : Show all their movies
[] : Find a movie
[] : Stop running a program when they type 'q'

"""
movies =[]

""" 
format for movies
movie = {
name : string
director : string
year : int
}

"""
def add_movie():
    # movie = {}
    # movie["name"] = input('Enter the name of the movie : ')
    # movie["director"] = input('Enter the name of the director : ')
    # movie["year"] = int(input('Enter the year of release date : '))
    # movies.append(movie)
    name = input('Enter the name of the movie : ')
    director = input('Enter the director of the movie : ')
    year = int(input('Enter the movie release year : '))
    print()
    movies.append({'name':name,
                   'director':director,
                   'year':year})

def show_movies():
    for movie in movies:
        show_movie_detail(movie)
        # print(f"name = {movie['name']}")
        # print(f"director = {movie['director']}")
        # print(f"year = {movie['year']}")

def show_movie_detail(movie):
        print(f"Movie name = {movie['name']}")
        print(f"Director = {movie['director']}")
        print(f"Year = {movie['year']}\n")

def find_movie():
    value = input('Enter 1 : Find movie by name\
    \nEnter 2 : Find movie by director\
    \nEnter 3 : Find movie by year\n')
    
    if value == '1':
        name = input('Enter movie name : ')
        print()
        for movie in movies:
            if movie['name'] == name:
                show_movie_detail(movie)
    
    elif value == '2':
        director = input('Enter director name : ')
        print()
        for movie in movies:
            if movie['director'] == director:
                show_movie_detail(movie)
    elif value == '3':
        year = int(input('Enter year : '))
        print()
        for movie in movies:
            if movie['year'] == year:
                show_movie_detail(movie)

def menu():
    
    user_input = input("Enter 'a' to add a movie\n  \
    'l' to see your movies\n  \
    'f' to find a movie\n  \
    'q' to quit\n")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()

        elif user_input == 'l':
            show_movies()

        elif user_input == 'f':
            find_movie()

        else:
            print('Please try again')
        # elif user_input == 'q':
        #     print('Stopping Program...')

        user_input = input("Enter\n'a' to add a movie\
        \n'l' to see your movies\
        \n'f' to find a movie\
        \n'q' to quit\n")
    print('Exiting')



menu()
