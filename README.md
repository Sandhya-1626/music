# 🎵 Mood-Based Song Recommender System

A beginner-friendly Python mini project that recommends songs based on your current mood and intensity level. Features both a console application and a modern web interface.

## ✨ Features

- **4 Mood Categories**: Happy 😊, Sad 😢, Romantic 💕, Energetic ⚡
- **3 Intensity Levels**: Low, Medium, High
- **120 Songs**: 10 songs per mood-intensity combination
- **Surprise Song**: Random song highlighted from recommendations
- **Motivational Quotes**: Mood-based inspirational quotes
- **Mood Change Feature**: Option to get happy songs to lift your spirits
- **Dual Interface**: Console app and premium web UI

## 🚀 Quick Start

### Web Version (Recommended)

1. **Install Dependencies:**
   ```bash
   pip install Flask
   ```

2. **Run the Application:**
   ```bash
   python app.py
   ```

3. **Access in Browser:**
   - Automatically opens at `http://127.0.0.1:5000/`
   - Or manually navigate to the URL

### Console Version

```bash
python console_app.py
```

## 📁 Project Structure

```
music/
├── songs_data.py          # Song database with 120 songs
├── console_app.py         # Console application
├── app.py                 # Flask web server
├── requirements.txt       # Dependencies
├── static/
│   ├── style.css         # Premium dark theme
│   └── script.js         # Frontend logic
└── templates/
    └── index.html        # Web interface
```

## 🎨 Web Interface Features

- **Premium Dark Theme**: Modern gradient backgrounds
- **Glassmorphism Effects**: Frosted glass card designs
- **Smooth Animations**: Fade-in, slide-in, bounce, and pulse effects
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Interactive Elements**: Hover effects and visual feedback
- **Google Fonts**: Professional typography (Inter & Outfit)

## 💻 Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Data Storage**: Python dictionaries (no database needed)
- **No Internet Required**: All data stored locally

## 🎯 How It Works

1. **Select Your Mood**: Choose from Happy, Sad, Romantic, or Energetic
2. **Choose Intensity**: Pick Low, Medium, or High intensity level
3. **Get Recommendations**: View 10 personalized song suggestions
4. **Surprise Song**: One song is randomly highlighted
5. **Read Quote**: Get a motivational quote for your mood
6. **Change Mood**: Option to get happy songs to improve your mood

## 📝 Code Highlights

### Beginner-Friendly
- Simple Python concepts (dictionaries, lists, if-else)
- Well-commented code
- Clean, readable structure
- No complex algorithms

### Song Database Example
```python
SONGS_DATABASE = {
    "Happy": {
        "Low": ["Don't Worry Be Happy - Bobby McFerrin", ...],
        "Medium": ["Happy - Pharrell Williams", ...],
        "High": ["September - Earth, Wind & Fire", ...]
    },
    # ... more moods
}
```

## 🌟 Screenshots

### Web Interface
- Modern dark theme with vibrant gradients
- Interactive mood selection cards
- Smooth animations and transitions
- Beautiful song list display
- Highlighted surprise song
- Motivational quote section

### Console Interface
- Clean text-based menu
- Formatted song lists
- Emoji decorations
- User-friendly prompts

## 📚 Requirements

- Python 3.7+
- Flask 3.1.2

## 🎓 Perfect For

- Python beginners learning dictionaries and functions
- College mini projects
- Learning Flask basics
- Understanding frontend-backend communication
- Practicing web design with CSS animations

## 🤝 Contributing

This is a beginner-friendly educational project. Feel free to:
- Add more songs to the database
- Create new mood categories
- Enhance the UI design
- Add new features

## 📄 License

Free to use for educational purposes.

## 🎉 Enjoy!

Discover the perfect songs for your mood and let the music lift your spirits! 🎵✨
