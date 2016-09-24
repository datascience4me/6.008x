# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:23:46 2016

@author: anton
"""

import comp_prob_inference


def main():
    first_look()


def first_look():
    prob_space = {'sunny': 1 / 2, 'rainy': 1 / 6, 'snowy': 1 / 3}
    random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)
    W = random_outcome
    if random_outcome == 'sunny':
        I = 1
    else:
        I = 0
    print("Random variable W = " + W)
    print("Random variable I = " + str(I))


if __name__ == "__main__":
    main()