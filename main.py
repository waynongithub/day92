# Python Flask Upload and Display Image | Flask tutorial
# https://www.youtube.com/watch?v=dP-2NVUgh50
from flask import Flask, render_template, send_from_directory, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import FileField, SubmitField
from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

# from wtforms.validators import FileAllowed,

app = Flask(__name__)
app.config['SECRET_KEY'] = "skdfjafjoefnouefoehqownlkajdf2ofFWRfwaef"
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

# IMAGES is a list of file extensions, photos is the name for the uploadset
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


def get_palette(filename):
    """NeuralNine: Extracting Dominant Colors From Images in Python (https://www.youtube.com/watch?v=nEYap1mupUQ) """
    ct = ColorThief(f"uploads/{filename}")
    dominant_color = ct.get_color(quality=1)

    # plt.imshow([[dominant_color]])
    # plt.show()

    palette = ct.get_palette(color_count=5)
    # plt.imshow([[palette[i] for i in range(5)]])
    # plt.show()
    colors = []
    for color in palette:
        # print(color)
        print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
        colors.append(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
        # print(colorsys.rgb_to_hsv(*color))
        # print(colorsys.rgb_to_hls(*color))
    return colors

def Gget_palette(filename):
    colors = ['#948689' , '#3d3d3b', '#e2d7d8', '#563634', '#60473a']
    return colors


@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.route("/", methods=["GET", "POST"])
def index():
    form = UploadForm()
    colors = []
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
        colors = get_palette(filename)
    else:
        file_url = None
    return render_template("index.html", form=form, file_url=file_url, colors=colors)


class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File field should not be empty')
        ]
    )
    submit = SubmitField('upload')


if __name__ == '__main__':
    app.run(debug=True)