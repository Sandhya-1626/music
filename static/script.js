/**
 * Mood-Based Song Recommender - Frontend JavaScript
 * Handles user interactions and API communication
 */

// State management
let selectedMood = null;
let selectedIntensity = null;

// DOM Elements
const moodSection = document.getElementById('moodSection');
const intensitySection = document.getElementById('intensitySection');
const resultsSection = document.getElementById('resultsSection');
const happySongsSection = document.getElementById('happySongsSection');
const thankYouSection = document.getElementById('thankYouSection');

const moodCards = document.querySelectorAll('.mood-card');
const intensityButtons = document.querySelectorAll('.intensity-btn');
const btnYes = document.getElementById('btnYes');
const btnNo = document.getElementById('btnNo');
const btnRestart = document.getElementById('btnRestart');
const btnRestart2 = document.getElementById('btnRestart2');

// Mood Selection Handler
moodCards.forEach(card => {
    card.addEventListener('click', () => {
        // Remove previous selection
        moodCards.forEach(c => c.classList.remove('selected'));
        
        // Add selection to clicked card
        card.classList.add('selected');
        
        // Store selected mood
        selectedMood = card.dataset.mood;
        
        // Show intensity section with smooth scroll
        setTimeout(() => {
            intensitySection.classList.remove('hidden');
            intensitySection.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }, 300);
    });
});

// Intensity Selection Handler
intensityButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove previous selection
        intensityButtons.forEach(b => b.classList.remove('selected'));
        
        // Add selection to clicked button
        button.classList.add('selected');
        
        // Store selected intensity
        selectedIntensity = button.dataset.intensity;
        
        // Get recommendations
        getRecommendations();
    });
});

// Get Recommendations from Backend
async function getRecommendations() {
    try {
        const response = await fetch('/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                mood: selectedMood,
                intensity: selectedIntensity
            })
        });
        
        if (!response.ok) {
            throw new Error('Failed to get recommendations');
        }
        
        const data = await response.json();
        displayResults(data);
        
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to get recommendations. Please try again.');
    }
}

// Display Results
function displayResults(data) {
    // Update selected mood text
    document.getElementById('selectedMoodText').textContent = 
        `${data.mood} Mood - ${data.intensity} Intensity`;
    
    // Display song list
    const songList = document.getElementById('songList');
    songList.innerHTML = '';
    data.songs.forEach(song => {
        const li = document.createElement('li');
        li.textContent = song;
        songList.appendChild(li);
    });
    
    // Display surprise song
    document.getElementById('surpriseSongName').textContent = data.surprise_song;
    
    // Display quote
    document.getElementById('quoteText').textContent = data.quote;
    
    // Hide previous sections and show results
    moodSection.classList.add('hidden');
    intensitySection.classList.add('hidden');
    resultsSection.classList.remove('hidden');
    
    // Smooth scroll to results
    setTimeout(() => {
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
}

// Mood Change - Yes Button
btnYes.addEventListener('click', async () => {
    try {
        const response = await fetch('/change-mood', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) {
            throw new Error('Failed to get happy songs');
        }
        
        const data = await response.json();
        displayHappySongs(data);
        
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to get happy songs. Please try again.');
    }
});

// Display Happy Songs
function displayHappySongs(data) {
    // Display happy song list
    const happySongList = document.getElementById('happySongList');
    happySongList.innerHTML = '';
    data.songs.forEach(song => {
        const li = document.createElement('li');
        li.textContent = song;
        happySongList.appendChild(li);
    });
    
    // Display happy quote
    document.getElementById('happyQuoteText').textContent = data.quote;
    
    // Hide results and show happy songs
    resultsSection.classList.add('hidden');
    happySongsSection.classList.remove('hidden');
    
    // Smooth scroll to happy songs
    setTimeout(() => {
        happySongsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
}

// Mood Change - No Button
btnNo.addEventListener('click', () => {
    // Hide results and show thank you
    resultsSection.classList.add('hidden');
    thankYouSection.classList.remove('hidden');
    
    // Smooth scroll to thank you
    setTimeout(() => {
        thankYouSection.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }, 100);
});

// Restart Button Handlers
function restartApp() {
    // Reset state
    selectedMood = null;
    selectedIntensity = null;
    
    // Remove all selections
    moodCards.forEach(c => c.classList.remove('selected'));
    intensityButtons.forEach(b => b.classList.remove('selected'));
    
    // Hide all sections except mood selection
    intensitySection.classList.add('hidden');
    resultsSection.classList.add('hidden');
    happySongsSection.classList.add('hidden');
    thankYouSection.classList.add('hidden');
    moodSection.classList.remove('hidden');
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

btnRestart.addEventListener('click', restartApp);
btnRestart2.addEventListener('click', restartApp);

// Add smooth scroll behavior for better UX
document.documentElement.style.scrollBehavior = 'smooth';
