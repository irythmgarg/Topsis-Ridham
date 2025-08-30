import numpy as np

class Topsis:
    def __init__(self, data, weights, impacts):
        self.data = np.array(data, dtype=float)
        self.weights = np.array(weights, dtype=float)
        self.impacts = impacts

        if self.data.shape[1] != len(self.weights) or len(self.weights) != len(self.impacts):
            raise ValueError("Number of weights, impacts, and columns in data must be same.")

    def normalize(self):
        norm = np.sqrt((self.data ** 2).sum(axis=0))
        self.data = self.data / norm

    def apply_weights(self):
        self.data = self.data * self.weights

    def ideal_best_worst(self):
        ideal_best, ideal_worst = [], []
        for j in range(len(self.impacts)):
            if self.impacts[j] == '+':
                ideal_best.append(self.data[:, j].max())
                ideal_worst.append(self.data[:, j].min())
            else:
                ideal_best.append(self.data[:, j].min())
                ideal_worst.append(self.data[:, j].max())
        return np.array(ideal_best), np.array(ideal_worst)

    def calculate_scores(self):
        self.normalize()
        self.apply_weights()
        ideal_best, ideal_worst = self.ideal_best_worst()

        dist_best = np.sqrt(((self.data - ideal_best) ** 2).sum(axis=1))
        dist_worst = np.sqrt(((self.data - ideal_worst) ** 2).sum(axis=1))

        scores = dist_worst / (dist_best + dist_worst)
        return scores

    def rank(self):
        scores = self.calculate_scores()
        return np.argsort(-scores) + 1, scores  # ranks, scores
