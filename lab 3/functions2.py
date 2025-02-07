movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def high_imdb(movie):
    return movie["imdb"] > 5.5

def highly_rated_movies(movie_list):
    return [movie for movie in movie_list if is_highly_rated(movie)]

filtered_movies = high_imdb(movies)
for movie in filtered_movies:
    print(movie["name"], movie["imdb"])
    
def movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"].lower() == category.lower()]

romance_movies = movies_by_category(movies, "Romance")
for movie in romance_movies:
    print(movie["name"], movie["category"])
    
def average_imdb(movie_list):
    if not movie_list:
        return 0
    return sum(movie["imdb"] for movie in movie_list) / len(movie_list) 

avg_rating = average_imdb(movies)
print(avg_rating)

def average_imdb_by_category(movie_list, category):
    filtered_movies = movies_by_category(movie_list, category)
    return average_imdb(filtered_movies)

avg_romance = average_imdb_by_category(movies, "Romance")
print(avg_romance)
    
