from flask import Flask, render_template
app = Flask(__name__)

post=[
    {
        'Author': 'Chirchir',
        'Title': 'blog post 1',
        'contents': 'first blog post 1',
        'date': 'first April 2017'
    },
    {
        'Author': 'Chelangat',
        'Title': 'blog post 2',
        'contents': 'first blog post 2',
        'date': 'first April 2017'
    }

]


@app.route("/")
def hello():
    return render_template('home.html', posts=post)


@app.route('/home')
def home():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
