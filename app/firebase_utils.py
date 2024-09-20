import firebase_admin
from firebase_admin import credentials, firestore,auth

# Firebase setup (already existing in your project)
cred = credentials.Certificate("app/firebase/firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_all_movies():
    """Fetch all movies from the 'Movies' collection in Firestore."""
    movies_ref = db.collection('Movies')
    movies = []
    for doc in movies_ref.stream():
        movie = doc.to_dict()
        movie['id'] = doc.id  # Include document ID for links
        movies.append(movie)
    print(movies)
    return movies



def get_movie_by_id(movie_id):
    """Fetch a specific movie's details from Firestore using the movie ID."""
    try:
        movie_ref = db.collection('Movies').document(movie_id)
        movie = movie_ref.get()
        if movie.exists:
            return movie.to_dict()
        else:
            print(f"No movie found with ID: {movie_id}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_reviews_by_movie_id(movie_id):
    # Fetch all reviews for a specific movie
    reviews_ref = db.collection('Movies').document(movie_id).collection('reviews')
    docs = reviews_ref.stream()
    return [doc.to_dict() for doc in docs]