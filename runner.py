from flask import Flask, request, render_template, jsonify, send_file
from flask_cors import CORS
# import imgtopdf
app = Flask(__name__)
CORS(app)

@app.route("/", methods= ['GET', 'POST'])
def slash():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == "POST":
    #    imgtopdf.pdfmaker('allinone')
        pass
    
    print("IYA!")
    print(request.files)
    return "sdsd"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)