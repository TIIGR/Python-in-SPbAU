from flask import Flask, render_template, request
from sqlite3 import connect

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/db')
def db_editor():
    lst = request.args.get('command', '').split()
    con = connect('base.db')
    cur = con.cursor()
    if len(lst) != 3 or len(lst[2]) != 1 or lst[0] not in ['A', 'B', 'C', 'D']:
        items = cur.execute('SELECT * FROM students').fetchall()
        cur.close()
        con.close()
        return render_template('db_web.html', items=items)
    elif lst[0] == 'A':
        cur.execute('UPDATE students SET A = ? WHERE Z = ?', (lst[2], lst[1]))
    elif lst[0] == 'B':
        cur.execute('UPDATE students SET B = ? WHERE Z = ?', (lst[2], lst[1]))
    elif lst[0] == 'C':
        cur.execute('UPDATE students SET C = ? WHERE Z = ?', (lst[2], lst[1]))
    elif lst[0] == 'D':
        cur.execute('UPDATE students SET D = ? WHERE Z = ?', (lst[2], lst[1]))
    con.commit()
    items = cur.execute('SELECT * FROM students').fetchall()
    cur.close()
    con.close()
    return render_template('db_web.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
