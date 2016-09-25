print('Exercise: Bayes\' Theorem and Total Probability')
P_T_S = 0.99
P_nT_nS = 0.99
P_S = 0.001
P_nS = 0.999
P_T_nS = 0.01

P_S_T = (P_T_S * P_S) / (P_T_S * P_S + P_T_nS * P_nS)

print(
    'The probability that given a randomly selected person has a positive test result, '
    'she or he has the infection is' + str(P_S_T))
