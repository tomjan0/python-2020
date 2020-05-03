import numpy as np
import pandas as pd

np.seterr(divide='ignore', invalid='ignore')


def gen_recommendation(x, y):
    z = np.dot(
        np.nan_to_num(x / np.linalg.norm(x, axis=0)),
        np.nan_to_num(y / np.linalg.norm(y)),
    )

    x_norm = np.nan_to_num(x / np.linalg.norm(x, axis=0))
    z_norm = np.nan_to_num(z / np.linalg.norm(z))

    return np.dot(x_norm.T, z_norm)


def gen_ratings(filtered_ratings_data, max_uid, max_movie_id):
    ratings = np.zeros((max_uid + 1, max_movie_id + 1))
    for uid, movie_id, rating in filtered_ratings_data:
        ratings[int(uid), int(movie_id)] = rating
    return ratings


def main():
    ratings_data = pd.read_csv("./ml-latest-small/ratings.csv", sep=",")
    movies_data = pd.read_csv("./ml-latest-small/movies.csv", sep=",")

    filtered_ratings_data = ratings_data.loc[
        ratings_data["movieId"] < 10000, ["userId", "movieId",
                                          "rating"]].to_numpy()

    filtered_movies_data = movies_data.loc[
        movies_data["movieId"] < 10000, ["movieId", "title"]].to_numpy()

    max_uid = int(max([x[0] for x in filtered_ratings_data]))
    max_movie_id = int(max([x[1] for x in filtered_ratings_data]))

    ratings = gen_ratings(filtered_ratings_data, max_uid, max_movie_id)
    movies = {}
    for movie_id, title in filtered_movies_data:
        movies[movie_id] = title

    my_ratings = np.zeros((max_movie_id + 1, 1))
    my_ratings[2571] = 5
    my_ratings[32] = 4
    my_ratings[260] = 5
    my_ratings[1097] = 4

    recommendations = [(i, val) for i, val in
                       enumerate(np.ndarray.flatten(
                           gen_recommendation(ratings, my_ratings)))]

    recommendations.sort(key=lambda pair: -pair[1])

    print("20 best recommendations:")
    for i, (movie_id, match) in enumerate(recommendations[:20]):
        print("\t", i + 1, ") ", match, " - ", movies[movie_id],
              sep="")


if __name__ == "__main__":
    main()
