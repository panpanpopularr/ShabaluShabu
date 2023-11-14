from flask import Flask, request, render_template, jsonify, send_file
from flask_cors import CORS
import realpdf
from io import BytesIO
app = Flask(__name__)
CORS(app)

@app.route("/", methods= ['GET', 'POST'])
def slash():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == "POST":
        print(request.form.get('filetype'))
        print(request.files)
        filetype = request.form.get('filetype')
        result = realpdf.pdftime(filetype, request.files)
        print('images.zip' if filetype == "onetoone" else 'images.pdf')
    return send_file(BytesIO(result), download_name='images.zip' if filetype == "onetoone" else 'images.pdf', as_attachment=True)
    print("IYA!")
    
    return "sdsd"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)