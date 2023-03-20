import numpy as np
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from sqlalchemy import update, true

from classify import load_csv, str_column_to_float, str_column_to_int, predict_classification, str_to_float, \
    normalize_dataset, dataset_minmax

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

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


# @app.route('/api/getBrands', methods=['GET'])
# def get_brands():
#     brands = models.Brand.query.all()
#     return jsonify(brands)


@app.route('/api/evaluate', methods=['POST'])
def get_rank():
    user_input = request.get_json()
    # car_condition = carEvaluation(int(user_input["age"]), int(user_input["mileage"]), int(user_input["repairments"]),fuzzy_model[0],fuzzy_model[1], fuzzy_model[2])
    # est_price = user_input["selectedCarObj"]["price"] * car_condition[0]*0.1
    # if str(user_input["areDocsInOrder"]) != 'True':
    #     est_price *= 0.2
    #
    # response = {"price": est_price}
    # task = models.Task(
    #     age=user_input["age"],
    #     mileage=user_input["mileage"],
    #     repairments=user_input["repairments"],
    #     brand=user_input["selectedCarObj"]["brand"],
    #     name=user_input["selectedCarObj"]["name"],
    #     documents=user_input["areDocsInOrder"],
    #     est_price=response["price"])
    # db.session.add(task)
    # db.session.commit()
    # return jsonify(response)
    # row = ["Somewhat high", "Very high", "Very high", "Very low", "Moderately high", "Very high", "Moderately low", "Somewhat high", "More or less low", "Somewhat high", "High", "Extremely low"]

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
