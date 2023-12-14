# from os.path import splitext
from os.path import basename
from glob import glob

from flask import Flask, render_template

app = Flask(__name__)


# @app.template_filter("splitext")
# def splitext_filter(s):
#     return splitext(s)[0]


@app.route("/")
def home():
    img_paths = glob("*.png", root_dir="static/images")
    img_names = [basename(img).removesuffix(".png") for img in img_paths]
    grid = {
        "A": ["" for _ in range(6)],
        "B": ["" for _ in range(6)],
        "C": ["" for _ in range(6)],
    }

    for img, path in zip(img_names, img_paths):
        grid[img[0]][int(img[1]) - 1] = path

    print(grid)

    return render_template("main.html", grid=grid)


@app.route("/buttons")
def buttons_testing():
    return render_template("buttons.html")


if __name__ == "__main__":
    app.run(debug=True)
