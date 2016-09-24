# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:23:46 2016

@author: anton
"""

import comp_prob_inference
import numpy as np


def approach_0():
    print('Approach 0')
    prob_table = {('sunny', 'hot'): 3 / 10,
                  ('sunny', 'cold'): 1 / 5,
                  ('rainy', 'hot'): 1 / 30,
                  ('rainy', 'cold'): 2 / 15,
                  ('snowy', 'hot'): 0,
                  ('snowy', 'cold'): 1 / 3}
    prob = prob_table[('rainy', 'cold')]
    print(prob)


def approach_1():
    print('Approach 1')
    prob_W_T_dict = {}
    for w in {'sunny', 'rainy', 'snowy'}:
        prob_W_T_dict[w] = {}
    prob_W_T_dict['sunny']['hot'] = 3 / 10
    prob_W_T_dict['sunny']['cold'] = 1 / 5
    prob_W_T_dict['rainy']['hot'] = 1 / 30
    prob_W_T_dict['rainy']['cold'] = 2 / 15
    prob_W_T_dict['snowy']['hot'] = 0
    prob_W_T_dict['snowy']['cold'] = 1 / 3

    comp_prob_inference.print_joint_prob_table_dict(prob_W_T_dict)
    print(prob_W_T_dict['rainy']['cold'])


def approach_2():
    print('Approach 2')
    prob_W_T_rows = ['sunny', 'rainy', 'snowy']
    prob_W_T_cols = ['hot', 'cold']
    prob_W_T_array = np.array([[3 / 10, 1 / 5], [1 / 30, 2 / 15], [0, 1 / 3]])
    comp_prob_inference.print_joint_prob_table_array(prob_W_T_array, prob_W_T_rows, prob_W_T_cols)
    print(prob_W_T_array[prob_W_T_rows.index('rainy'), prob_W_T_cols.index('cold')])


def approach_3():
    print('Approach 3 : an optimization for Numpy index')
    prob_W_T_rows = ['sunny', 'rainy', 'snowy']
    prob_W_T_cols = ['hot', 'cold']
    prob_W_T_row_mapping = {label: index for index, label in enumerate(prob_W_T_rows)}
    prob_W_T_col_mapping = {label: index for index, label in enumerate(prob_W_T_cols)}
    prob_W_T_array = np.array([[3 / 10, 1 / 5], [1 / 30, 2 / 15], [0, 1 / 3]])
    comp_prob_inference.print_joint_prob_table_array(prob_W_T_array, prob_W_T_rows, prob_W_T_cols)
    print(prob_W_T_array[prob_W_T_row_mapping['sunny'], prob_W_T_col_mapping['hot']])


def main():
    print('Jointly Distributed Random Variables')
    print('=====================================')
    approach_0()
    print('=====================================')
    approach_1()
    print('=====================================')
    approach_2()
    print('=====================================')
    approach_3()


if __name__ == "__main__":
    main()
