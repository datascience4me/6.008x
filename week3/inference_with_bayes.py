import numpy as np

prob_Y_cond_X = np.matrix([[0.01, 0.99], [0.99, 0.01]])
prob_X = np.array([0.999, 0.001])


def ex_1():
    print('Exercise: The Product Rule for Random Variables - Medical Diagnosis Revisited')
    print('prob_X = ' + str(prob_X))
    print('prob_X|Y = \n' + str(prob_Y_cond_X))
    print('p(healthy, positive) = ' + str(prob_X[0] * prob_Y_cond_X[0, 0]))
    print('p(healthy, negative) = ' + str(prob_X[0] * prob_Y_cond_X[0, 1]))
    print('p(infected, positive) = ' + str(prob_X[1] * prob_Y_cond_X[1, 0]))
    print('p(infected, negative) = ' + str(prob_X[1] * prob_Y_cond_X[1, 1]))


def ex_2():
    print('Exercise: Bayes Theorem for Random Variables - Medical Diagnosis, Continued')
    print('prob_X = ' + str(prob_X))
    print('prob_X|Y = \n' + str(prob_Y_cond_X))
    p_healthy_c_positive = (prob_X[0] * prob_Y_cond_X[0, 0]) / np.sum(prob_X * prob_Y_cond_X[:, 0])
    print('p(healthy | positive) = ' + str(p_healthy_c_positive))
    p_healthy_c_negative = (prob_X[0] * prob_Y_cond_X[0, 1]) / np.sum(prob_X * prob_Y_cond_X[:, 1])
    print('p(healthy | negative) = ' + str(p_healthy_c_negative))


def main():
    print('Inference with Bayes Theorem for Random Variables')
    print('=====================================')
    ex_1()
    print('=====================================')
    ex_2()


if __name__ == "__main__":
    main()
