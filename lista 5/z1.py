import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# movies = pd.read_csv("./ml-latest-small/movies.csv")
ratings = pd.read_csv("./ml-latest-small/ratings.csv.")
toy_story_ratings = ratings[ratings["movieId"] == 1]


def generateXY(m: int):
    y = [[rating] for rating in toy_story_ratings["rating"]]
    # y = [[row["rating"]] for _, row in toy_story_ratings.iterrows()]

    x = []
    for user_id in toy_story_ratings.userId:
        user_ratings = ratings[ratings.userId == user_id]
        x_i = []
        for j in range(2, m + 2):
            j_rating = user_ratings[user_ratings.movieId == j]
            x_i.append(float(j_rating.rating) if not j_rating.empty else 0)
        x.append(x_i)

    return np.array(x), np.array(y)

for size in [500,1000]:
    print('Size: ', size)
    x2, y2 = generateXY(size)
    x_sliced = x2[0:200]
    y_sliced = y2[0:200]
    model = LinearRegression().fit(x_sliced, y_sliced)
    print('\tModel score against training set', model.score(x_sliced, y_sliced))
    print('\tModel score against test set', model.score(x2[200:215], y2[200:215]))
    print('\tModel score against all data', model.score(x2, y2))

    predictions = model.predict(x2[200:215])
    print('\tPredicting last 15')
    for i in range(15):
        print('\t\tPrediction: ', predictions[i], ' Real: ', y2[200 + i])

