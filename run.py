from flask import Flask, jsonify, abort, request
from models import Diary
app = Flask(__name__)


@app.route('/')
def hello_world():
   return jsonify({"message": "user registered"})

#  route for signup  
@app.route('/api/v1/signup', methods=['POST'])
def signup():
   return jsonify({"message": "user registered"})

        
# route for login
@app.route('/api/v1/login', methods=['POST'])
def login():
    return jsonify({"message": "user registered"})

# route for getting all
@app.route('/api/v1/diaries/all', methods=['GET'])
def get_all():
    return jsonify({"message": "retrieve all entry"})

# route for getting each
@app.route('/api/v1/diaries/<int:id>', methods=['GET'])
def get_each(id):
    return jsonify({"message": "retrieved each"})

# route for posting an entry 
@app.route('/api/v1/diaries/', methods=['POST'])
def post_entry(id):
    return jsonify({"message": "Entry posted succesfully"})


# route for modifying entry
@app.route('/api/v1/diaries/<int:id>', methods=['PUT'])
def edit_entry(id):
    return jsonify({"message": "Entry edited succesfully"})

# route for deleting entry
@app.route('/api/v1/diaries/<int:id>', methods=['DELETE'])
def delete_entry(id):
    return jsonify({"message": "Entry deleted succesfully"})


if __name__ == '__main__':
   app.run()
