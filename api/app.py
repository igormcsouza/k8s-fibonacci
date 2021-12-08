from flask import Flask, request
from flask.blueprints import Blueprint
from flask.json import jsonify


app = Flask(__name__)

@app.route("/api/get-fibonacci")
def get_fibonacci():
    number = request.args.get('number', None)

    if not number:
        return jsonify(
            {'details': 'Query Argument "number" was not set.'}), 422

    number = int(number)

    if number < 2:
        return jsonify(
            {'details': 'Number must be grater than 2'}), 422
    
    accum = [1, 1]

    for i in range(number-2):
        accum.append(accum[-1] + accum[-2])

    return jsonify({'sequence': accum}), 200
