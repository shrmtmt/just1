from flask import Flask, render_template, request, redirect, url_for
import random
import os

app = Flask(__name__)

def load_words():
    with open('words.txt') as file:
        return file.read().splitlines()

words = load_words()

@app.route('/')
def index():
    measurement_id = os.getenv('GTAG', 'G-LD9500Y7G4')
    return render_template('index.html', measurement_id=measurement_id)

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

@app.route('/rules')
def how_to_play():
    with open('rules.txt', 'r') as file:
        rules = file.read()
    return render_template('rules.html', rules=rules)

@app.route('/slide/<num>')
def slide(num):
    slide_num = int(num)
    next_slide_num = slide_num + 1 if slide_num < 7 else None
    return render_template('slide_template.html', slide_num=slide_num, next_slide_num=next_slide_num)

if __name__ == '__main__':
    app.run(debug=True)
