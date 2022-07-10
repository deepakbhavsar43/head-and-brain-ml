import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt


class HeadBrain:

    def load_data(self):
        dataset = pd.read_csv("Dataset/HeadBrain.csv")
        self.X = dataset["Head Size(cm^3)"]
        self.Y = dataset["Brain Weight(grams)"]

    def Calculate_Mean(self):
        self.xMean = np.mean(self.X)
        self.yMean = np.mean(self.Y)

    def Calculate_coef(self):
        self.dataset_length = len(self.X)
        self.m, numerator, denominator = 0, 0, 0
        for i in range(0, self.dataset_length):
            numerator += (self.X[i] - self.xMean) * (self.Y[i] - self.yMean)
            denominator += (self.X[i] - self.xMean) ** 2
        self.m = numerator / denominator
        self.c = self.yMean - self.m * self.xMean

    def Calculate_R2Score(self):
        yp, yo = 0, 0
        predictions = []
        for i in range(0, self.dataset_length):
            y_p = self.c + self.m * self.X[i]
            predictions.append(y_p)
            yp += (self.Y[i] - y_p) ** 2
            yo += (self.Y[i] - self.yMean) ** 2
        r_score = 1 - (yp / yo)
        print(predictions)
        print("R2 Score : ", r_score)

    def plot_graph(self):
        max_x = np.max(self.X)
        min_x = np.min(self.X)

        x = np.linspace(min_x, max_x)
        y = self.c + self.m * x

        plt.plot(x, y, color="#ef5423", label="Regression")
        plt.scatter(self.X, self.Y, label="Scatter Plot")
        plt.xlabel("Head Size(cm^3)")
        plt.ylabel("Brain Weight(grams)")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    obj1 = HeadBrain()
    obj1.load_data()
    obj1.Calculate_Mean()
    obj1.Calculate_coef()
    obj1.Calculate_R2Score()
    obj1.plot_graph()