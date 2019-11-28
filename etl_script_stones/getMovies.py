import tmdbsimple as tmdb
import csv
import os
from datetime import datetime 

#Defino a chave copiando da viariavel de ambiente
tmdb.API_KEY = os.environ.get('api_key')

def getNowplayingMovies():
    
    movies = tmdb.Movies()
    movies_now_playing = movies.now_playing(region='US')
    pages = movies_now_playing.get('total_pages')
    

    with open('data/movies_nowplaying.csv', 'w', newline='') as movies_csv, open('data/status_nowplaying.csv', 'w', newline='') as s_now_csv: 
        
        writer_movie = csv.DictWriter(movies_csv, fieldnames=['movie_id', 'title', 'original_language', 'populary', 'poster_path', 'adult', 'vote_average'])
        writer_status = csv.DictWriter(s_now_csv, fieldnames = ['movie_id', 'status', 'status_date'])
        
        writer_status.writeheader()
        writer_movie.writeheader()
        
        for page in range(1, pages +1):
            movies_now_playing = movies.now_playing(page = page, region='US')
            for movie in movies_now_playing.get('results'):
                writer_status.writerow({'movie_id': movie.get('id'), 'status': 'now playing', 'status_date': datetime.now().strftime("%Y-%m-%d")})
                writer_movie.writerow({'movie_id': movie.get('id'),
                                'title': movie.get('title'),
                                'original_language': movie.get('original_language'),
                                'populary': movie.get('populary'),
                                'poster_path': movie.get('poster_path'),
                                'adult': movie.get('adult'),
                                'vote_average': movie.get('vote_average')})


def getUpcomingMovies():
    
    movies = tmdb.Movies()
    movies_now_playing = movies.upcoming(region='US')
    pages = movies_now_playing.get('total_pages')
    

    with open('data/movies_upcoming.csv', 'w', newline='') as movies_csv, open('data/status_upcoming.csv', 'w', newline='') as s_up_csv: 
        
        writer_movie = csv.DictWriter(movies_csv, fieldnames=['movie_id', 'title', 'original_language', 'populary', 'poster_path', 'adult', 'vote_average'])
        writer_status = csv.DictWriter(s_up_csv, fieldnames = ['movie_id', 'status', 'status_date' ])
        
        writer_status.writeheader()
        writer_movie.writeheader()
       
        for page in range(1, pages +1):
            movies_now_playing = movies.now_playing(page = page, region='US')
            for movie in movies_now_playing.get('results'):
                writer_status.writerow({'movie_id': movie.get('id'), 'status': 'up coming', 'status_date': datetime.now().strftime("%Y-%m-%d")})
                writer_movie.writerow({'movie_id': movie.get('id'),
                                'title': movie.get('title'),
                                'original_language': movie.get('original_language'),
                                'populary': movie.get('populary'),
                                'poster_path': movie.get('poster_path'),
                                'adult': movie.get('adult'),
                                'vote_average': movie.get('vote_average')})

if __name__ == '__main__':
    getNowplayingMovies()
    getUpcomingMovies()
