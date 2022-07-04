
import Caption_it
from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def marks():
    if request.method == 'POST':

#         f = request.files['userfile']
#         print(f)
#         path = "./static/{}".format(f.filename)
#         f.save(path)

#         caption = Caption_it.caption_this_image(path)
#         print(caption)

    return render_template("ind.html", cap=caption)


if __name__ == '__main__':
    app.run(debug=True)
