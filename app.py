from flask import Flask, render_template, request, redirect, url_for
from movie_storage import load_data, save_data
from movie_api import fetch_movie_data

app = Flask(__name__)

@app.route('/')
def index():
    movies = load_data()
    return render_template('index.html', movies=movies)

@app.route('/add', methods=['GET', 'POST'])
@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        rating = request.form['rating']
        year = request.form['year']
        genre = request.form['genre']
        movie_data = {
            'title': title,
            'rating': rating,
            'year': year,
            'genre': genre
        }
        movies = load_data()
        movies[title] = movie_data
        save_data(movies)
        return redirect(url_for('index'))
    return render_template('add_movie.html')

if __name__ == '__main__':
    app.run(debug=True)