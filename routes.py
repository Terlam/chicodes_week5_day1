# Import the app variable from the init
from top_five_app import app

# Import specific packages from flask
from flask import render_template
    
# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/artist')
def artistRoute():
    names = ['SevenSixSupah', 'Jamila Woods', 'Mitratinta', "Len'i", 'Kidda The Great']
    return render_template('artists.html',list_names = names)

@app.route('/influencer')
def influencerRoute():
    names = ['Lenora Porter', 'Crisdelahozmar', 'Unbreakable Kicks', "ErickThomas", 'Alexandria Ocasio-Cortez']
    return render_template('influencers.html',list_names = names)

@app.route('/athlete')
def athleteRoute():
    names = ['Zion Williams', 'Bron Bron', 'Bolt', "Jordan", 'Kobe']
    return render_template('athletes.html',list_names = names)
