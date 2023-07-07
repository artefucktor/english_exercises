import pandas as pd

from flask import Flask, request, redirect, url_for
from flask import render_template

from format_options import format_options

app = Flask(__name__)
df = pd.read_csv('static/bearskin_formatted.csv')
status = 'You can upload your own .csv file'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', status=status, sents=df)

@app.route('/uploader', methods=['POST'])
def uploader():
    global df, status
    try:
        file = request.files.get('file')
        df = pd.read_csv(file)
        mask = df.options.notna()
        df.loc[mask, 'options'] = df.loc[mask, 'options'].apply(eval)
        all_types = ['select_word', 'noun_phrases', 'select_sent', 'missing_word']
        df['formatted_options'] = df.apply(format_options, axis=1)
        df['transformed_sent'] = df.apply(lambda x: x['raw'].replace(x['object'], x['formatted_options'], 1)
                                          if x['type'] in all_types else x['raw'], axis=1)
        df = df.fillna(' ')
        status = 'Successfull upload ' + file.filename
    except:
        status = "File can't be uploaded"
    return redirect(url_for('index'))

