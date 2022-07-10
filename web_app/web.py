from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/prime', methods=['GET'])
def prime():
    n = request.args.get('n')
    if n is None:
        n = 1
    if int(n) <= 0:
        return render_template('prime.html', N="Число не является натуральным!", n=n)
    else:
        if int(n) == 1:
            return render_template('prime.html', N="True", n=n)
        else:
            d = 2
            while int(n) % d != 0:
                d += 1
            return render_template('prime.html', N=d == int(n), n=n)


if __name__ == '__main__':
    app.run(debug=True)
