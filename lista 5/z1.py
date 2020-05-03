import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def gen_x(m, filtered_ratings, ratings):
    res = []
    for user_id in filtered_ratings.userId:
        user_ratings = ratings.loc[
            (ratings.userId == user_id) & (ratings.movieId > 1) & (
                    ratings.movieId <= m),
            ["movieId", "rating"]].to_numpy()
        sorted_user_ratings = np.zeros(m)
        for movieId, rating in user_ratings:
            sorted_user_ratings[int(movieId) - 2] = rating
        res.append(sorted_user_ratings)
    return np.array(res)


def gen_y(filtered_ratings):
    return [[rating] for rating in filtered_ratings["rating"]]


def plot_differences(data, real_values, plot):
    model = LinearRegression().fit(data, real_values)
    predicted = plot.scatter(np.arange(215), model.predict(data), alpha=0.75)
    real = plot.scatter(np.arange(215), real_values, alpha=0.75, c="y")
    plot.legend((predicted, real), ("Predicted", "Real"))
    plot.set_title(
        f"m = ${len(data[0])}, Score = ${model.score(data, real_values)}")


def predict_last_15(data, real_values):
    model = LinearRegression().fit(data[:-15], real_values[:-15])
    predictions = model.predict(data[-15:])
    print("Last 15 predictions for m = ", len(data[0]), " (Score: ",
          model.score(data[:-15], real_values[:-15]), ")",
          sep="")
    for j in range(15):
        print("\tPredicted: ", predictions[j], " Real: ", real_values[200 + j])
    print()


def main():
    ratings = pd.read_csv("./ml-latest-small/ratings.csv")
    filtered_ratings = ratings[ratings["movieId"] == 1]
    xs = [gen_x(m, filtered_ratings, ratings) for m in
          [10, 100, 200, 500, 1000, 10000]]
    xs_2 = [xs[0], xs[4], xs[5]]
    y = gen_y(filtered_ratings)

    fig, plots = plt.subplots(1, 3)
    for i in range(3):
        plot_differences(xs_2[i], y, plots[i])
    plt.show()

    for x in xs:
        predict_last_15(x, y)


if __name__ == "__main__":
    main()
