from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    with open('data.txt') as f:
        messages = f.read().splitlines()

    return render_template('index.html', messages=messages)


@app.route('/post_message', methods=['POST'])
def post_message():
    if request.method == 'POST':
        username = request.form['username']

        if username == '':
            username = '名無しさん'

        message = request.form['message']

        with open('data.txt', 'a') as f:
            f.write(f'{username}: {message}\n')

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
