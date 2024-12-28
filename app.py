from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file', 400

    # Read the image file
    input_image = file.read()

    # Process the image using rembg
    output_image = remove(input_image)

    # Convert the output image to a byte stream
    output_stream = io.BytesIO(output_image)

    # Send the output image back as a response
    return send_file(output_stream, mimetype='image/png', as_attachment=True, download_name='output.png')

if __name__ == '__main__':
    app.run(debug=True)
