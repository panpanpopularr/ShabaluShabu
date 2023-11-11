from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/", methods= ['GET', 'POST'])
def slash():
    if request.method == 'GET':
        print("AYA")
        return render_template('index.html')
    
if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)