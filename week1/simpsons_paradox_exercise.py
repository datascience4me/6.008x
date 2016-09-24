# -*- coding: utf-8 -*-

from week1.simpsons_paradox_data import *

print("Joint probability table:\n" + str(joint_prob_table))
print(joint_prob_table[gender_mapping['female'], department_mapping['C'], admission_mapping['admitted']])
joint_prob_gender_admission = joint_prob_table.sum(axis=1)
print(joint_prob_gender_admission)
print(joint_prob_gender_admission[gender_mapping['female'], admission_mapping['admitted']])

# What is P(A=admitted|G=female)
female_only = joint_prob_gender_admission[gender_mapping['female']]
prob_admission_given_female = female_only / np.sum(female_only)
prob_admission_given_female_dict = dict(zip(admission_labels, prob_admission_given_female))
print('P(A|G=female) = ' + str(prob_admission_given_female_dict))

# What is P(A=admitted|G=male)
male_only = joint_prob_gender_admission[gender_mapping['male']]
prob_admission_given_male = male_only / np.sum(male_only)
prob_admission_given_male_dict = dict(zip(admission_labels, prob_admission_given_male))
print('P(A|G=male) = ' + str(prob_admission_given_male_dict))

# Let's investigate by looking at how things differ by each department.
admitted_only = joint_prob_gender_admission[:, admission_mapping['admitted']]
prob_gender_given_admitted = admitted_only / np.sum(admitted_only)
prob_gender_given_admitted_dict = dict(zip(gender_labels, prob_gender_given_admitted))
print(prob_gender_given_admitted_dict)


def prob_of_admission_conditioning(gen, dep):
    return str(joint_prob_table[
                   gender_mapping[gen], department_mapping[dep], admission_mapping['admitted']] / np.sum(
        joint_prob_table[gender_mapping[gen], department_mapping[dep]]))


# Now let's determine the probability of getting admitted given each gender and each department.
# Department A
print('===== Department A ======')
print('P(A=admitted|G=female,D=A) = ' + prob_of_admission_conditioning('female', 'A'))
print('P(A=admitted|G=male,D=A) = ' + prob_of_admission_conditioning('male', 'A'))

print('===== Department B ======')
print('P(A=admitted|G=female,D=B) = ' + prob_of_admission_conditioning('female', 'B'))
print('P(A=admitted|G=male,D=B) = ' + prob_of_admission_conditioning('male', 'B'))

print('===== Department C ======')
print('P(A=admitted|G=female,D=C) = ' + prob_of_admission_conditioning('female', 'C'))
print('P(A=admitted|G=male,D=C) = ' + prob_of_admission_conditioning('male', 'C'))

print('===== Department D ======')
print('P(A=admitted|G=female,D=D) = ' + prob_of_admission_conditioning('female', 'D'))
print('P(A=admitted|G=male,D=D) = ' + prob_of_admission_conditioning('male', 'D'))

print('===== Department E ======')
print('P(A=admitted|G=female,D=E) = ' + prob_of_admission_conditioning('female', 'E'))
print('P(A=admitted|G=male,D=E) = ' + prob_of_admission_conditioning('male', 'E'))

print('===== Department F ======')
print('P(A=admitted|G=female,D=F) = ' + prob_of_admission_conditioning('female', 'F'))
print('P(A=admitted|G=male,D=F) = ' + prob_of_admission_conditioning('male', 'F'))
