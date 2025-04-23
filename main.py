from flask import Flask, request, jsonify
from app.predicte import predict_spam 

app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict ():
    data = request.get_json()
    message = data.get('message' , '')
    prediction = predict_spam(message)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)




