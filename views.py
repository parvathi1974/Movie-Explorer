import requests
from django.shortcuts import render
from django.conf import settings  #access OMDB_API_KEY

def home(request):

    url = f"http://www.omdbapi.com/?s=movie&apikey={settings.OMDB_API_KEY}"  
    
    response = requests.get(url)
    data = response.json()

    # Check if the response is valid and contains movies
    if data.get('Response') == 'True':
        trending_movies = data.get('Search', [])
    else:
        trending_movies = []

    return render(request, 'movies/home.html', {'movies': trending_movies})

def search(request):
    query = request.GET.get('q', '')  # Ensure an empty string is returned if no query
    if query:
        url = f"http://www.omdbapi.com/?s={query}&apikey={settings.OMDB_API_KEY}"
        response = requests.get(url)
        data = response.json()

        # Check if the response is valid and contains movies
        if data.get('Response') == 'True':
            movies = data.get('Search', [])
        else:
            movies = []
    else:
        movies = []  # If there's no query, return an empty list

    return render(request, 'movies/search.html', {'movies': movies})

def movie_details(request, imdb_id):
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={settings.OMDB_API_KEY}"
    response = requests.get(url)
    movie = response.json()
    return render(request, 'movies/details.html', {'movie': movie})
