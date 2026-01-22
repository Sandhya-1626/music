"""
Mood-Based Song Recommender System - Console Version
A simple Python program that recommends songs based on your mood and intensity level
"""

import random
from songs_data import SONGS_DATABASE, MOOD_QUOTES


def display_menu():
    """Display the mood selection menu"""
    print("\n" + "="*60)
    print("🎵  MOOD-BASED SONG RECOMMENDER SYSTEM  🎵")
    print("="*60)
    print("\nSelect your current mood:")
    print("1. Happy 😊")
    print("2. Sad 😢")
    print("3. Romantic 💕")
    print("4. Energetic ⚡")
    print("="*60)


def get_mood_choice():
    """Get and validate mood choice from user"""
    mood_map = {
        "1": "Happy",
        "2": "Sad",
        "3": "Romantic",
        "4": "Energetic"
    }
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice in mood_map:
            return mood_map[choice]
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 4.")


def get_intensity_level():
    """Get and validate intensity level from user"""
    print("\n" + "-"*60)
    print("Select mood intensity level:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    print("-"*60)
    
    intensity_map = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }
    
    while True:
        choice = input("\nEnter intensity level (1-3): ").strip()
        if choice in intensity_map:
            return intensity_map[choice]
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 3.")


def display_recommendations(mood, intensity, songs):
    """Display the recommended songs"""
    print("\n" + "="*60)
    print(f"🎵  RECOMMENDED SONGS FOR {mood.upper()} MOOD ({intensity} Intensity)")
    print("="*60)
    
    # Display all recommended songs
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song}")
    
    print("="*60)


def display_surprise_song(songs):
    """Pick and display a random surprise song"""
    surprise_song = random.choice(songs)
    print("\n" + "🎁"*30)
    print(f"✨ SURPRISE SONG FOR YOU: {surprise_song} ✨")
    print("🎁"*30)


def display_quote(mood):
    """Display a motivational quote based on mood"""
    quote = random.choice(MOOD_QUOTES[mood])
    print("\n" + "💭"*30)
    print(f"Quote: {quote}")
    print("💭"*30)


def ask_mood_change():
    """Ask if user wants to change their mood"""
    print("\n" + "="*60)
    response = input("Do you want songs to change your mood? (yes/no): ").strip().lower()
    return response in ['yes', 'y']


def recommend_happy_songs():
    """Recommend happy songs to change mood"""
    print("\n" + "="*60)
    print("🌟  HERE ARE SOME HAPPY SONGS TO LIFT YOUR SPIRITS!  🌟")
    print("="*60)
    
    # Get all happy songs from all intensity levels
    all_happy_songs = []
    for intensity in ["Low", "Medium", "High"]:
        all_happy_songs.extend(SONGS_DATABASE["Happy"][intensity])
    
    # Display 10 random happy songs
    selected_songs = random.sample(all_happy_songs, min(10, len(all_happy_songs)))
    for i, song in enumerate(selected_songs, 1):
        print(f"{i}. {song}")
    
    print("="*60)
    
    # Display a happy quote
    happy_quote = random.choice(MOOD_QUOTES["Happy"])
    print(f"\n💭 {happy_quote}")
    print("="*60)


def main():
    """Main function to run the song recommender system"""
    
    # Display welcome menu
    display_menu()
    
    # Get user's mood choice
    mood = get_mood_choice()
    
    # Get intensity level
    intensity = get_intensity_level()
    
    # Get songs for selected mood and intensity
    recommended_songs = SONGS_DATABASE[mood][intensity]
    
    # Display recommendations
    display_recommendations(mood, intensity, recommended_songs)
    
    # Display surprise song
    display_surprise_song(recommended_songs)
    
    # Display motivational quote
    display_quote(mood)
    
    # Ask if user wants to change mood
    if ask_mood_change():
        recommend_happy_songs()
    else:
        print("\n" + "="*60)
        print("Thank you for using Mood-Based Song Recommender! 🎵")
        print("Keep listening and stay awesome! ✨")
        print("="*60)


# Run the program
if __name__ == "__main__":
    main()
