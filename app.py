from flask import Flask,request, jsonify
import os
from main import detect
import base64
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    data = request.get_json(force=True)
    image=data['image']
    with open("demo.png", "wb") as fh:
        fh.write(base64.decodebytes(image.encode()))
    boxes,text,scores= detect('demo.png')
  return jsonify({'class': str(text), 'score': str(scores), 'boxes': str(boxes)})
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5032)