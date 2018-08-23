from flask import Flask, render_template, request, escape
from vsearch import search4letters
import mysql.connector

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = {'host': '127.0.0.1', 'user': 'vsearch', 'password': 'vsearchpasswd', 'database': 'vsearchlogDB'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log (phrase, letters, ip, browser_string, results)
    values (%s,%s,%s,%s,%s)"""
    cursor.execute(_SQL, ("galaktyka", "tym", "127.0.0.1", "Opera", "{'t', 'y'}"))
    conn.commit()
    _SQL = '''select * from log'''
    cursor.execute(_SQL)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Oto Twoje wyniki: '
    results = str(search4letters(phrase.upper(), letters.upper()))
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title, the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Witamy na stronie internetowej search4letters!')

@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)
if __name__=='__main__':
    app.run(debug=True)
