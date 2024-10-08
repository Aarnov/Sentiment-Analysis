from flask import Flask, render_template
from app.firebase_utils import get_all_movies,get_movie_by_id,get_reviews_by_movie_id

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    movies = get_all_movies()
    return render_template('index.html',movies=movies)


@app.route('/movies')
def moviegrid_page():
    movies = get_all_movies()  # Fetch all movies from Firebase
    return render_template('moviegrid.html', movies=movies)


@app.route('/moviesingle/<id>')
def moviesingle_page(id):

    # Fetch movie details and reviews
    movie = get_movie_by_id(id)
    reviews = get_reviews_by_movie_id(id)


    if movie:
        return render_template('moviesingle.html', movie=movie,reviews=reviews)
    else:
        return render_template('404.html')  # Show 404 page if movie not found


@app.route('/404.html')
def error404():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
