"""
Mood-Based Song Recommender System - Song Database
This module contains all songs organized by mood and intensity level
"""

# Song Database: Dictionary structure
# Format: {mood: {intensity: [list of songs]}}
SONGS_DATABASE = {
    "Happy": {
        "Low": [
            "Don't Worry Be Happy - Bobby McFerrin",
            "Three Little Birds - Bob Marley",
            "Good Vibrations - The Beach Boys",
            "Walking on Sunshine - Katrina and The Waves",
            "Here Comes the Sun - The Beatles",
            "I'm Yours - Jason Mraz",
            "Best Day of My Life - American Authors",
            "Count on Me - Bruno Mars",
            "Lovely Day - Bill Withers",
            "Happy Together - The Turtles"
        ],
        "Medium": [
            "Happy - Pharrell Williams",
            "Can't Stop the Feeling - Justin Timberlake",
            "Shake It Off - Taylor Swift",
            "Good Time - Owl City & Carly Rae Jepsen",
            "On Top of the World - Imagine Dragons",
            "Send Me on My Way - Rusted Root",
            "I Gotta Feeling - Black Eyed Peas",
            "Dynamite - BTS",
            "Uptown Funk - Mark Ronson ft. Bruno Mars",
            "Shut Up and Dance - Walk the Moon"
        ],
        "High": [
            "September - Earth, Wind & Fire",
            "Mr. Blue Sky - Electric Light Orchestra",
            "Dancing Queen - ABBA",
            "Don't Stop Me Now - Queen",
            "I Want to Break Free - Queen",
            "Celebration - Kool & The Gang",
            "Footloose - Kenny Loggins",
            "Jump - Van Halen",
            "Livin' on a Prayer - Bon Jovi",
            "Party Rock Anthem - LMFAO"
        ]
    },
    "Sad": {
        "Low": [
            "The Night We Met - Lord Huron",
            "Skinny Love - Bon Iver",
            "Mad World - Gary Jules",
            "Hurt - Johnny Cash",
            "Tears in Heaven - Eric Clapton",
            "Yesterday - The Beatles",
            "Hallelujah - Jeff Buckley",
            "Fix You - Coldplay",
            "The Scientist - Coldplay",
            "Someone Like You - Adele"
        ],
        "Medium": [
            "Someone You Loved - Lewis Capaldi",
            "When I Was Your Man - Bruno Mars",
            "All I Want - Kodaline",
            "Say Something - A Great Big World",
            "Let Her Go - Passenger",
            "Photograph - Ed Sheeran",
            "Stay With Me - Sam Smith",
            "Grenade - Bruno Mars",
            "We Are Never Getting Back Together - Taylor Swift",
            "Breakeven - The Script"
        ],
        "High": [
            "Nothing Compares 2 U - Sinead O'Connor",
            "Back to Black - Amy Winehouse",
            "Creep - Radiohead",
            "Everybody Hurts - R.E.M.",
            "Tears Dry on Their Own - Amy Winehouse",
            "Bleeding Love - Leona Lewis",
            "Jar of Hearts - Christina Perri",
            "Wrecking Ball - Miley Cyrus",
            "Rolling in the Deep - Adele",
            "Cry Me a River - Justin Timberlake"
        ]
    },
    "Romantic": {
        "Low": [
            "Make You Feel My Love - Adele",
            "Thinking Out Loud - Ed Sheeran",
            "A Thousand Years - Christina Perri",
            "All of Me - John Legend",
            "Perfect - Ed Sheeran",
            "Marry You - Bruno Mars",
            "Lucky - Jason Mraz ft. Colbie Caillat",
            "Everything - Michael Bublé",
            "Just the Way You Are - Bruno Mars",
            "Your Song - Elton John"
        ],
        "Medium": [
            "Love Story - Taylor Swift",
            "Can't Help Falling in Love - Elvis Presley",
            "Endless Love - Lionel Richie & Diana Ross",
            "Unchained Melody - The Righteous Brothers",
            "At Last - Etta James",
            "Wonderful Tonight - Eric Clapton",
            "I Don't Want to Miss a Thing - Aerosmith",
            "You Are the Reason - Calum Scott",
            "Falling Like the Stars - James Arthur",
            "Beautiful in White - Shane Filan"
        ],
        "High": [
            "Crazy in Love - Beyoncé ft. Jay-Z",
            "I Wanna Dance with Somebody - Whitney Houston",
            "Kiss Me - Sixpence None the Richer",
            "Sugar - Maroon 5",
            "Treasure - Bruno Mars",
            "Love on Top - Beyoncé",
            "Shut Up and Kiss Me - Mary Chapin Carpenter",
            "Can't Take My Eyes Off You - Frankie Valli",
            "You Make My Dreams - Hall & Oates",
            "I'm a Believer - The Monkees"
        ]
    },
    "Energetic": {
        "Low": [
            "Radioactive - Imagine Dragons",
            "Believer - Imagine Dragons",
            "Thunder - Imagine Dragons",
            "Centuries - Fall Out Boy",
            "Hall of Fame - The Script ft. will.i.am",
            "Stronger - Kanye West",
            "Eye of the Tiger - Survivor",
            "We Will Rock You - Queen",
            "The Phoenix - Fall Out Boy",
            "Warriors - Imagine Dragons"
        ],
        "Medium": [
            "Titanium - David Guetta ft. Sia",
            "Roar - Katy Perry",
            "Firework - Katy Perry",
            "Stronger (What Doesn't Kill You) - Kelly Clarkson",
            "Fight Song - Rachel Platten",
            "Can't Hold Us - Macklemore & Ryan Lewis",
            "Pump It - Black Eyed Peas",
            "Run the World (Girls) - Beyoncé",
            "Lose Yourself - Eminem",
            "Remember the Name - Fort Minor"
        ],
        "High": [
            "Till I Collapse - Eminem",
            "Thunderstruck - AC/DC",
            "We Are the Champions - Queen",
            "Jump Around - House of Pain",
            "Welcome to the Jungle - Guns N' Roses",
            "Enter Sandman - Metallica",
            "Sabotage - Beastie Boys",
            "Killing in the Name - Rage Against the Machine",
            "Bulls on Parade - Rage Against the Machine",
            "X Gon' Give It to Ya - DMX"
        ]
    }
}

# Motivational Quotes for each mood
MOOD_QUOTES = {
    "Happy": [
        "Happiness is not by chance, but by choice. - Jim Rohn",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
        "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
        "Happiness is a warm puppy. - Charles M. Schulz"
    ],
    "Sad": [
        "Every storm runs out of rain. - Maya Angelou",
        "Tears are words that need to be written. - Paulo Coelho",
        "The way sadness works is one of the strange riddles of the world. - Lemony Snicket",
        "Behind every sweet smile, there is a bitter sadness that no one can see. - Tupac Shakur",
        "It's okay to not be okay. Just don't give up."
    ],
    "Romantic": [
        "Love is composed of a single soul inhabiting two bodies. - Aristotle",
        "The best thing to hold onto in life is each other. - Audrey Hepburn",
        "You know you're in love when you can't fall asleep because reality is finally better than your dreams. - Dr. Seuss",
        "Love is not about how many days, months, or years you have been together. It's about how much you love each other every single day.",
        "In all the world, there is no heart for me like yours. In all the world, there is no love for you like mine. - Maya Angelou"
    ],
    "Energetic": [
        "Energy and persistence conquer all things. - Benjamin Franklin",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
}

# Tamil Songs Database with YouTube Links
# Format: {mood: {intensity: [(song_name, youtube_link)]}}
TAMIL_SONGS_DATABASE = {
    "Happy": {
        "Low": [
            ("Kannamma - Kaala", "https://www.youtube.com/watch?v=bIcIeZDzqaM"),
            ("Vaathi Coming - Master", "https://www.youtube.com/watch?v=KVo4GAwCTr8"),
            ("Aalaporan Tamizhan - Mersal", "https://www.youtube.com/watch?v=3gLe-PG5Yfk"),
            ("Rowdy Baby - Maari 2", "https://www.youtube.com/watch?v=x6Q7c9RyMzk"),
            ("Sodakku - Thaanaa Serndha Koottam", "https://www.youtube.com/watch?v=Qn0av8N5gMc"),
            ("Simtaangaran - Sarkar", "https://www.youtube.com/watch?v=wuMhNLo-WBk"),
            ("Marana Mass - Petta", "https://www.youtube.com/watch?v=OjWLSBPJWMI"),
            ("Selfie Pulla - Kaththi", "https://www.youtube.com/watch?v=4-lYzNEn1Hs"),
            ("Surviva - Vivegam", "https://www.youtube.com/watch?v=NVRMdKJEgjg"),
            ("Verithanam - Bigil", "https://www.youtube.com/watch?v=3R1qJPUz4iw")
        ],
        "Medium": [
            ("Kutty Story - Master", "https://www.youtube.com/watch?v=Hn5YjNlXz3o"),
            ("Enjoy Enjaami - Dhee ft. Arivu", "https://www.youtube.com/watch?v=eYq7WapuDLU"),
            ("Arabic Kuthu - Beast", "https://www.youtube.com/watch?v=3B_y_29LWus"),
            ("Vaathi Raid - Master", "https://www.youtube.com/watch?v=gKVORnDNs7c"),
            ("Theri Theme - Theri", "https://www.youtube.com/watch?v=OwAGQwbNuCw"),
            ("Singappenney - Bigil", "https://www.youtube.com/watch?v=LJ-1xN_Sg4Y"),
            ("Aathichudi - Mersal", "https://www.youtube.com/watch?v=Ot_1_Fy7-Ks"),
            ("Petta Paraak - Petta", "https://www.youtube.com/watch?v=KJQ3pPBYJPI"),
            ("Kannaana Kanney - Viswasam", "https://www.youtube.com/watch?v=bnVEGoQC4ss"),
            ("Jolly O Gymkhana - Beast", "https://www.youtube.com/watch?v=1-AAyeNaVDY")
        ],
        "High": [
            ("Naatu Naatu - RRR", "https://www.youtube.com/watch?v=OsU0CGZoV8E"),
            ("Oo Antava - Pushpa", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Jimikki Kammal - Velipadinte Pusthakam", "https://www.youtube.com/watch?v=d0cqAycRwiI"),
            ("Buttabomma - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=JFcgOboQZ08"),
            ("Butta Bomma - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=JFcgOboQZ08"),
            ("Samajavaragamana - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=yWDtVb6BVxg"),
            ("Ramuloo Ramulaa - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=eJRd3LxmTNA"),
            ("Otha Sollaala - Asuran", "https://www.youtube.com/watch?v=Fy1YV4YAYFQ"),
            ("Vaa Vaathi - Master", "https://www.youtube.com/watch?v=KVo4GAwCTr8"),
            ("Kaavaalaa - Jailer", "https://www.youtube.com/watch?v=YR12Z8f1Dh8")
        ]
    },
    "Sad": {
        "Low": [
            ("Kannukul Kannai - Vinnaithaandi Varuvaayaa", "https://www.youtube.com/watch?v=cKWfBjHwOEI"),
            ("Ennodu Nee Irundhaal - I", "https://www.youtube.com/watch?v=RLlQFU-Pzxk"),
            ("Thalli Pogathey - Achcham Yenbadhu Madamaiyada", "https://www.youtube.com/watch?v=VwQJv5hMELY"),
            ("Nenjukkul Peidhidum - Vaaranam Aayiram", "https://www.youtube.com/watch?v=hs_YvDDU-1s"),
            ("Munbe Vaa - Sillunu Oru Kaadhal", "https://www.youtube.com/watch?v=fSCCYarJKkk"),
            ("Kadhal Rojave - Roja", "https://www.youtube.com/watch?v=Ey_2U8Vn3dQ"),
            ("Malare - Premam", "https://www.youtube.com/watch?v=Yh-9fDDLBdU"),
            ("Kaatru Veliyidai - Kaatru Veliyidai", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Vaseegara - Minnale", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Yennai Maatrum Kadhale - Kadhal Konden", "https://www.youtube.com/watch?v=Qv7-RrtH4LE")
        ],
        "Medium": [
            ("Nee Paartha Vizhigal - 3", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Uyire - Bombay", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Kadhal Sadugudu - Alaipayuthey", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Nenjukkule - Kadal", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Idhayathai Yedho Ondru - Yennai Arindhaal", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Pudhu Vellai Mazhai - Roja", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Nenjae Yezhu - Maryan", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Kannazhaga - 3", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Oru Naalil - Pudhupettai", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Nee Kavithaigala - Kannathil Muthamittal", "https://www.youtube.com/watch?v=Qv7-RrtH4LE")
        ],
        "High": [
            ("Venmathi Venmathiye - Minnale", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Oru Deivam Thantha Poove - Kannathil Muthamittal", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Kadhal Anukkal - Enthiran", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Vaaranam Aayiram - Vaaranam Aayiram", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Mounam Pesiyadhe - Vinnaithaandi Varuvaayaa", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Nenjukkul Peidhidum - Vaaranam Aayiram", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Anbil Avan - Vinnaithaandi Varuvaayaa", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Usure Pogudhey - Raavanan", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Adiye - Kadal", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Ennodu Nee Irundhaal - I", "https://www.youtube.com/watch?v=Qv7-RrtH4LE")
        ]
    },
    "Romantic": {
        "Low": [
            ("Tum Hi Ho (Tamil) - Aashiqui 2", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Nee Kavithaigala - Kannathil Muthamittal", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Mazhai Kuruvi - Chekka Chivantha Vaanam", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Vennilave - Minsara Kanavu", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Hosanna - Vinnaithaandi Varuvaayaa", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Omana Penne - Vinnaithaandi Varuvaayaa", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Anbil Avan - Vinnaithaandi Varuvaayaa", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Nenjukkul Peidhidum - Vaaranam Aayiram", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Munbe Vaa - Sillunu Oru Kaadhal", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Uyire - Bombay", "https://www.youtube.com/watch?v=Qv7-RrtH4LE")
        ],
        "Medium": [
            ("Kannukul Kannai - Vinnaithaandi Varuvaayaa", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Thalli Pogathey - Achcham Yenbadhu Madamaiyada", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Vaseegara - Minnale", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Ennodu Nee Irundhaal - I", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Malare - Premam", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Kadhal Rojave - Roja", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Pudhu Vellai Mazhai - Roja", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Nenjukkule - Kadal", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Idhayathai Yedho Ondru - Yennai Arindhaal", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Kaatru Veliyidai - Kaatru Veliyidai", "https://www.youtube.com/watch?v=Qv7-RrtH4LE")
        ],
        "High": [
            ("Rowdy Baby - Maari 2", "https://www.youtube.com/watch?v=x6Q7c9RyMzk"),
            ("Vaathi Coming - Master", "https://www.youtube.com/watch?v=KVo4GAwCTr8"),
            ("Arabic Kuthu - Beast", "https://www.youtube.com/watch?v=3B_y_29LWus"),
            ("Buttabomma - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=JFcgOboQZ08"),
            ("Samajavaragamana - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=yWDtVb6BVxg"),
            ("Kannaana Kanney - Viswasam", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Singappenney - Bigil", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Selfie Pulla - Kaththi", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Sodakku - Thaanaa Serndha Koottam", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Kaavaalaa - Jailer", "https://www.youtube.com/watch?v=YR12Z8f1Dh8")
        ]
    },
    "Energetic": {
        "Low": [
            ("Theri Theme - Theri", "https://www.youtube.com/watch?v=OwAGQwbNuCw"),
            ("Surviva - Vivegam", "https://www.youtube.com/watch?v=NVRMdKJEgjg"),
            ("Aalaporan Tamizhan - Mersal", "https://www.youtube.com/watch?v=3gLe-PG5Yfk"),
            ("Simtaangaran - Sarkar", "https://www.youtube.com/watch?v=wuMhNLo-WBk"),
            ("Marana Mass - Petta", "https://www.youtube.com/watch?v=OjWLSBPJWMI"),
            ("Verithanam - Bigil", "https://www.youtube.com/watch?v=3R1qJPUz4iw"),
            ("Vaathi Raid - Master", "https://www.youtube.com/watch?v=gKVORnDNs7c"),
            ("Petta Paraak - Petta", "https://www.youtube.com/watch?v=KJQ3pPBYJPI"),
            ("Aathichudi - Mersal", "https://www.youtube.com/watch?v=Ot_1_Fy7-Ks"),
            ("Otha Sollaala - Asuran", "https://www.youtube.com/watch?v=Fy1YV4YAYFQ")
        ],
        "Medium": [
            ("Vaathi Coming - Master", "https://www.youtube.com/watch?v=KVo4GAwCTr8"),
            ("Kutty Story - Master", "https://www.youtube.com/watch?v=Hn5YjNlXz3o"),
            ("Arabic Kuthu - Beast", "https://www.youtube.com/watch?v=3B_y_29LWus"),
            ("Jolly O Gymkhana - Beast", "https://www.youtube.com/watch?v=1-AAyeNaVDY"),
            ("Rowdy Baby - Maari 2", "https://www.youtube.com/watch?v=x6Q7c9RyMzk"),
            ("Enjoy Enjaami - Dhee ft. Arivu", "https://www.youtube.com/watch?v=eYq7WapuDLU"),
            ("Kaavaalaa - Jailer", "https://www.youtube.com/watch?v=YR12Z8f1Dh8"),
            ("Singappenney - Bigil", "https://www.youtube.com/watch?v=LJ-1xN_Sg4Y"),
            ("Selfie Pulla - Kaththi", "https://www.youtube.com/watch?v=4-lYzNEn1Hs"),
            ("Sodakku - Thaanaa Serndha Koottam", "https://www.youtube.com/watch?v=Qn0av8N5gMc")
        ],
        "High": [
            ("Naatu Naatu - RRR", "https://www.youtube.com/watch?v=OsU0CGZoV8E"),
            ("Oo Antava - Pushpa", "https://www.youtube.com/watch?v=Qv7-RrtH4LE"),
            ("Jimikki Kammal - Velipadinte Pusthakam", "https://www.youtube.com/watch?v=d0cqAycRwiI"),
            ("Buttabomma - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=JFcgOboQZ08"),
            ("Ramuloo Ramulaa - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=eJRd3LxmTNA"),
            ("Samajavaragamana - Ala Vaikunthapurramuloo", "https://www.youtube.com/watch?v=yWDtVb6BVxg"),
            ("Vaathi Coming - Master", "https://www.youtube.com/watch?v=KVo4GAwCTr8"),
            ("Arabic Kuthu - Beast", "https://www.youtube.com/watch?v=3B_y_29LWus"),
            ("Kaavaalaa - Jailer", "https://www.youtube.com/watch?v=YR12Z8f1Dh8"),
            ("Verithanam - Bigil", "https://www.youtube.com/watch?v=3R1qJPUz4iw")
        ]
    }
}

# Tamil Quotes for each mood
TAMIL_MOOD_QUOTES = {
    "Happy": [
        "மகிழ்ச்சி என்பது நம் தேர்வு, வாய்ப்பல்ல.",
        "வாழ்க்கையின் நோக்கம் மகிழ்ச்சியாக இருப்பதே.",
        "சிரிப்பு உலகின் சிறந்த மருந்து.",
        "மகிழ்ச்சி உள்ளத்தில் இருந்து வருகிறது.",
        "ஒவ்வொரு நாளும் ஒரு புதிய வாய்ப்பு."
    ],
    "Sad": [
        "ஒவ்வொரு புயலும் மழையை இழக்கிறது.",
        "கண்ணீர் எழுதப்பட வேண்டிய வார்த்தைகள்.",
        "துக்கம் நிரந்தரமானது அல்ல.",
        "இருளுக்குப் பிறகு வெளிச்சம் வரும்.",
        "சரியில்லாமல் இருப்பது சரி."
    ],
    "Romantic": [
        "காதல் என்பது இரண்டு உடல்களில் ஒரே ஆத்மா.",
        "வாழ்க்கையில் பிடித்துக் கொள்ள சிறந்தது ஒருவரையொருவர்.",
        "காதல் என்பது கனவுகளை விட அழகானது.",
        "உண்மையான காதல் என்றும் மறைவதில்லை.",
        "உலகில் உன்னைப் போல் என் இதயத்திற்கு வேறு யாரும் இல்லை."
    ],
    "Energetic": [
        "ஆற்றலும் விடாமுயற்சியும் எல்லாவற்றையும் வெல்லும்.",
        "நீங்கள் செய்வதை நேசித்தால் மட்டுமே சிறந்த வேலை செய்ய முடியும்.",
        "கடிகாரத்தைப் பார்க்காதே, அது செய்வதைச் செய். தொடர்ந்து செல்.",
        "வெற்றி இறுதியானது அல்ல, தோல்வி மரணமானது அல்ல.",
        "எதிர்காலம் தங்கள் கனவுகளின் அழகை நம்புபவர்களுக்கு சொந்தமானது."
    ]
}

