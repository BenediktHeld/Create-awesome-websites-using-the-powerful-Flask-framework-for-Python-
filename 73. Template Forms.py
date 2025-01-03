# Importiere die Flask-Klasse und benötigte Module
from flask import Flask, render_template, request

# Erstelle ein Flask-Anwendungsobjekt
app = Flask(__name__)

@app.route('/')
def index():
    # Rendere die Startseite
    return render_template('index.html')

@app.route('/signup_form')
def signup_form():
    # Rendere das Anmeldeformular
    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    # Greife die Informationen aus der Anfrage ab
    first = request.args.get('first')  # Erhalte den Vornamen
    last = request.args.get('last')    # Erhalte den Nachnamen
    # Rendere die Dankeschön-Seite und übergebe die Namen
    return render_template('thankyou.html', first=first, last=last)

if __name__ == '__main__':
    app.run(debug=True)  # Starte die Anwendung im Debug-Modus

'''<!DOCTYPE html>
<html>
    <head> 
        <title></title>
        <!-- Bootstrap CSS und JS -->
        <!-- Bootstrap 5 CSS Link: Bietet die grundlegenden Stile für responsives Design -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <!-- Link zur Startseite, der die Funktion url_for verwendet -->
            <a class="navbar-brand" href="{{ url_for('index') }}">Home Page</a>
        </nav>
    </body>

    {% block content %}
    <!-- Hier wird der spezifische Inhalt der abgeleiteten Vorlagen eingefügt -->
    {% endblock %}
</html>



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

{% extends "base.html" %}

{% block content %}
    <div class="jumbotron">
        <p>Welcome to Puppy Rock!</p>
        <p>Wanna sign up for our puppy band?</p>
        <!-- Link zur Anmeldeseite, der die Funktion url_for verwendet -->
        <a href="{{ url_for('signup_form') }}">Sign Up</a>
    </div>
{% endblock %}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

{% extends "base.html" %}

{% block content %}
    <div class="jumbotron">
        <h1>Welcome to the sign up page!</h1>
        <p>Fill out the form. Notice we don't save any info!</p>
        <!-- Formular zur Eingabe von Vor- und Nachnamen -->
        <form action="{{ url_for('thank_you') }}">
            <label for="first">First Name:</label>
            <input type="text" name="first">
            <label for="last">Last Name:</label>
            <input type="text" name="last">
            <input type="submit" value="submit">
        </form>
    </div>
{% endblock %}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


{% extends "base.html" %}

{% block content %}
    <div class="jumbotron">
        <h1>Thanks for signing up! {{ first }} {{ last }}</h1>
        <!-- Zeigt den Dankestext mit den übergebenen Namen an -->
    </div>
{% endblock %}
'''
