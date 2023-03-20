from dotenv import load_dotenv
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from classify import load_csv, str_column_to_float, str_column_to_int, predict_classification, str_to_float
from config import Config
from evaluate import get_grade

load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
import models

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def index():
    return "hello, world"


@app.route('/api/getAllRanks', methods=['GET'])
def get():
    ranks = models.Rating.query.all()
    return jsonify(ranks)


@app.route('/api/evaluate', methods=['POST'])
def get_rank():
    user_input = request.get_json()
    row = []
    row_str = []
    for item in user_input["form"].values():
        row.append(str_to_float(item))

    for item in user_input["form"].values():
        row_str.append(item)

    filename = 'cv_dataset.csv'
    dataset = load_csv(filename)
    for i in range(len(dataset[0]) - 1):
        str_column_to_float(dataset, i)
    # convert class column to integers
    classification_labels = str_column_to_int(dataset, len(dataset[0]) - 1)

    # define amount of neighbours to pick
    num_neighbors = 5
    # predict the label
    label = predict_classification(dataset, row, num_neighbors)
    predicted = list(classification_labels.keys())[list(classification_labels.values()).index(label)]
    print('Data=%s, Predicted: %s' % (
        row, predicted))

    task = models.Rating(
        name=user_input["name"],
        estimated_class=predicted,
        rank=get_grade(row_str)[1]
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task)


@app.route('/api/interview/<int:id>', methods=['POST'])
def rank_interview(id):
    user_input = request.get_json()
    candidate = models.Rating.query.get(id)
    row = [get_grade(user_input["grade"])[1], candidate.rank]
    candidate.rank = sum(row)
    if user_input["type"] == "hr":
        if not candidate.hr_interviewed:
            candidate.hr_interviewed = True
            db.session.commit()
        return jsonify("HR interview has already been conducted")
    return jsonify(str(sum(row)))


if __name__ == '__main__':
    app.run(debug=True)
