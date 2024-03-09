from flask import Flask, render_template, request, jsonify
from servo import rotate_servo, init_servo, stop_servo
app = Flask(__name__)

init_servo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()
    
    rotate_servo(data['angle'])
    
    return jsonify({'message' : 'Success'})

if __name__ == '__main__':
    app.run(debug=True)
    stop_servo()