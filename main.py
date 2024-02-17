from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from color_palette_generator import get_most_common_colors
import os
import shutil

app = Flask(__name__)
bootstrap = Bootstrap(app)


# App route creation
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/cpg", methods=['GET', 'POST'])
def cpg():
    most_common_colors = None

    if request.method == 'POST':
        if 'imageUpload' in request.files:
            image_file = request.files['imageUpload']
            if image_file.filename != '':
                try:
                    # Create a temporary folder
                    temp_folder = 'static/temp_folder'
                    os.makedirs(temp_folder, exist_ok=True)

                    # Check if the file is allowed
                    allowed_extensions = {'png', 'jpg', 'jpeg'}
                    if ('.' in image_file.filename and image_file.filename.rsplit('.', 1)[1].lower()
                            in allowed_extensions):
                        # Save the uploaded file to the temporary folder
                        image_path = os.path.join(temp_folder, 'temp_image.jpg')
                        image_file.save(image_path)

                        # Get the number of colors from the form
                        num_colors = int(request.form.get('numColors', 5))

                        # Generate color palette
                        most_common_colors = get_most_common_colors(image_path, num_colors=num_colors)

                finally:
                    # Remove the temporary folder and its contents
                    shutil.rmtree(temp_folder, ignore_errors=True)

    return render_template("cpg.html", most_common_colors=most_common_colors)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
