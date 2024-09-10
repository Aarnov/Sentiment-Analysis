from flask import Flask, render_template, request, redirect, url_for
from app.firebase_utils import get_all_movies,get_movie_by_id

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movies')
def moviegrid_page():
    movies = get_all_movies()  # Fetch all movies from Firebase
    return render_template('moviegrid.html', movies=movies)


@app.route('/moviesingle.html')
def movie_single():
    movie_id = request.args.get('id')  # Get movie ID from URL parameters
    movie = get_movie_by_id(movie_id)  # Fetch movie details from Firebase
    if movie:
        return render_template('moviesingle.html', movie=movie)
    else:
        return render_template('404.html')  # Show 404 page if movie not found

if __name__ == '__main__':
    app.run(debug=True)
