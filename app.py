<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

def load_words():
    with open('words.txt') as file:
        return file.read().splitlines()

words = load_words()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guesser')
def guesser():
    word = random.choice(words)
    return render_template('guesser.html', word=word)

@app.route('/clue_giver', methods=['GET', 'POST'])
def clue_giver():
    if request.method == 'POST':
        hint = request.form['hint']
        return redirect(url_for('clue_display', hint=hint))
    return render_template('clue_giver.html')

@app.route('/clue_display/<hint>')
def clue_display(hint):
    return render_template('clue_display.html', hint=hint)

if __name__ == '__main__':
    app.run(debug=True)
