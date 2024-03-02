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
    measurement_id = os.getenv('GTAG', 'None')
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
    with open('static/text/rules1.txt', 'r') as file:
        rules1 = file.read()
    return render_template('rules.html', rules1=rules1)

@app.route('/slide/<num>')
def slide(num):
    if num == 0:
        with open('static/text/rules1.txt', 'r') as file:
            rules = file.read()
    elif num == 8:
        with open('static/text/rules2.txt', 'r') as file:
            rules = file.read()
    else:
        rules = None
    
    slide_num = str(int(num))
    next_slide_num = str(int(num) + 1) if int(num) < 8 else None
    return render_template('slide_template.html', slide_num=slide_num, next_slide_num=next_slide_num, rules=rules)

if __name__ == '__main__':
    app.run(debug=True)
