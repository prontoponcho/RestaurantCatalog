from catalog import app
from flask import send_from_directory


# how to serve css from:
# http://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)
