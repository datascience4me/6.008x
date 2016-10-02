import numpy as np


def main():
    print('=====================================')
    print('Homework Problem: Ice Cream Sales in Inferenceville')
    prob_S_C = np.array([[0.4, 0.1], [0.25, 0.25]])
    prob_S = prob_S_C.sum(axis=1)
    prob_C = prob_S_C.sum(axis=0)
    print(np.outer(prob_S, prob_C))
    print(np.outer(prob_S, prob_C) == prob_S_C)

    prob_S_C_given_T_0 = np.array([[0.72, 0.08], [0.18, 0.02]])
    prob_S_C_given_T_1 = np.array([[0.08, 0.12], [0.32, 0.48]])

    prob_s_c_given_T = prob_S_C_given_T_0 * prob_S_C_given_T_1
    print(prob_s_c_given_T)

    t = {0: 0.5, 1: 0.5}
    print(t)


if __name__ == "__main__":
    main()
