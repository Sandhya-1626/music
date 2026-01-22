"""
Mood-Based Song Recommender System - Flask Backend
Web server that provides song recommendations via API
"""

from flask import Flask, render_template, request, jsonify
import random
import webbrowser
from threading import Timer
from songs_data import SONGS_DATABASE, MOOD_QUOTES

app = Flask(__name__)


@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    """
    API endpoint to get song recommendations
    Expects JSON: {"mood": "Happy", "intensity": "Medium"}
    Returns: {"songs": [...], "surprise_song": "...", "quote": "..."}
    """
    try:
        data = request.get_json()
        mood = data.get('mood')
        intensity = data.get('intensity')
        
        # Validate input
        if mood not in SONGS_DATABASE:
            return jsonify({"error": "Invalid mood"}), 400
        
        if intensity not in SONGS_DATABASE[mood]:
            return jsonify({"error": "Invalid intensity"}), 400
        
        # Get songs for the selected mood and intensity
        songs = SONGS_DATABASE[mood][intensity]
        
        # Pick a random surprise song
        surprise_song = random.choice(songs)
        
        # Pick a random quote
        quote = random.choice(MOOD_QUOTES[mood])
        
        # Return recommendations
        return jsonify({
            "mood": mood,
            "intensity": intensity,
            "songs": songs,
            "surprise_song": surprise_song,
            "quote": quote
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/change-mood', methods=['POST'])
def change_mood():
    """
    API endpoint to get happy songs for mood change
    Returns: {"songs": [...], "quote": "..."}
    """
    try:
        # Get all happy songs from all intensity levels
        all_happy_songs = []
        for intensity in ["Low", "Medium", "High"]:
            all_happy_songs.extend(SONGS_DATABASE["Happy"][intensity])
        
        # Select 10 random happy songs
        selected_songs = random.sample(all_happy_songs, min(10, len(all_happy_songs)))
        
        # Pick a random happy quote
        quote = random.choice(MOOD_QUOTES["Happy"])
        
        return jsonify({
            "songs": selected_songs,
            "quote": quote
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def open_browser():
    """Open the web browser after a short delay"""
    webbrowser.open('http://127.0.0.1:5000/')


if __name__ == '__main__':
    # Open browser automatically after 1.5 seconds
    Timer(1.5, open_browser).start()
    
    # Run Flask app
    print("Starting Mood-Based Song Recommender System...")
    print("Opening browser at http://127.0.0.1:5000/")
    app.run(debug=True, use_reloader=False)
