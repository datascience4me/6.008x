# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:23:46 2016

@author: anton
"""

import comp_prob_inference


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


def approach_1():
    print("Approach 1")
    prob_space = {'sunny': 1 / 2, 'rainy': 1 / 6, 'snowy': 1 / 3}
    W_mapping = {'sunny': 'sunny', 'rainy': 'rainy', 'snowy': 'snowy'}
    I_mapping = {'sunny': 1, 'rainy': 0, 'snowy': 0}
    random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)
    W = W_mapping[random_outcome]
    I = I_mapping[random_outcome]

    print("Random variable W = " + W)
    print("Random variable I = " + str(I))


def approach_2():
    print("Approach 2")
    W_table = {'sunny': 1 / 2, 'rainy': 1 / 6, 'snowy': 1 / 3}
    I_table = {0: 1 / 2, 1: 1 / 2}
    W = comp_prob_inference.sample_from_finite_probability_space(W_table)
    I = comp_prob_inference.sample_from_finite_probability_space(I_table)
    print("Random variable W = " + W)
    print("Random variable I = " + str(I))


def exercise_probability_with_dice():
    print("Exercise: probability with dice")
    prob_space = {1: 1 / 6, 2: 1 / 6, 3: 1 / 6, 4: 1 / 6, 5: 1 / 6, 6: 1 / 6}
    prob_space_2 = {}
    for key1, value1 in prob_space.items():
        for key2, value2 in prob_space.items():
            key = key1 + key2
            if key in prob_space_2:
                prob_space_2[key] += 1 / 36
            else:
                prob_space_2[key] = 1 / 36
    print('Probability space is ' + str(len(prob_space_2)))
    print(prob_space_2)



def main():
    print('=====================================')
    first_look()
    print('=====================================')
    approach_1()
    print('=====================================')
    approach_2()
    print('=====================================')
    exercise_probability_with_dice()


if __name__ == "__main__":
    main()
