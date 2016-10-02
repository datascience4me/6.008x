import math
import numpy as np


def ex_1():
    print('Exercise: Bernoulli and Binomial Random Variables')
    p = 0.6
    q = 1 - p
    prob = (p ** 4) * (q ** 6)
    print('prob(HTHTTTTTHH) = ' + str(prob))
    print('Ways to get 4 heads = ' + str(binomial_coefficient(4, 10)))
    print('prob(H=4) = ' + str(binomial(4, 10, p)))


def binomial(k, n, p):
    q = 1 - p
    return binomial_coefficient(k, n) * (p ** k) * (q ** (n - k))


def binomial_coefficient(k, n):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def ex_2():
    print('Exercise: The Soda Machine')
    p = 2 / 7  # 7 flavors
    print('P(all 14 sodas has only 2 flavors) = ' + str(p ** 14))
    p = 2 / 5  # 5 flavors
    print('P(all 14 sodas has only 2 flavors) = ' + str(p ** 14))
    p = 2 / 3  # 3 flavors
    print('P(all 14 sodas has only 2 flavors) = ' + str(p ** 14))


def ex_3():
    print('Exercise: Gambler\'s Fallacy')
    p = 1 / 27
    print(1 - binomial(100, 100, 1 - p))
    print(1 - binomial(99, 99, 1 - p))


def ex_4():
    print('Exercise: Independent Random Variables')
    prob_W_I = np.array([[1 / 2, 0], [0, 1 / 6], [0, 1 / 3]])
    prob_W = prob_W_I.sum(axis=1)
    prob_I = prob_W_I.sum(axis=0)
    print(np.outer(prob_W, prob_I))
    print(np.outer(prob_W, prob_I) == prob_W_I)
    prob_X_Y = np.array([[1 / 4, 1 / 4], [1 / 12, 1 / 12], [1 / 6, 1 / 6]])
    prob_X = prob_X_Y.sum(axis=1)
    prob_Y = prob_X_Y.sum(axis=0)
    print(np.outer(prob_X, prob_Y))
    print(np.outer(prob_X, prob_Y) == prob_X_Y)


def main():
    print('Inference with Bayes Theorem for Random Variables')
    print('=====================================')
    ex_1()
    print('=====================================')
    ex_2()
    print('=====================================')
    ex_3()
    print('=====================================')
    ex_4()


if __name__ == "__main__":
    main()
