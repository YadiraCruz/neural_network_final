import random
import math



def read_file(file):
    "Reads in knapsack test files"
    #10 269
    #profit of item i , weight of item i 
    #first line of file holds the weight and knapsack capacity

    infile = open(file)
    file_read = infile.readlines()
    input_list = []
    output_list = []
    counter = 0

    for element in range(len(file_read)):
        element = element.strip('\n')
        if element == 0:
            total_weight = element[0][1]
        else:-
            dictionary[tuple(element[0][0], element[0][1])] = 


    weight = weight_list()
    print(weight)
    empty_list = []
    #for j in range(5620):
    for i in range(10):
        empty_list.append(get_activation(input_list[0], i, weight))
    all_errors = find_error(empty_list, output_list[0])
    for n in range(10):
        print(back_propogation(input_list[0], weight, n, all_errors))


def split_test(test_num):
    """splits test files into 2 groups"""
    #split test into 2 groups 1/2 training 1/2 testing
    #10 examples of what we are running (files)
    split = int(10 * test_num)
    test_list_index = random.sample(range(10), split)
    new_set = set(test_list_index)
    second_set = set(range(10))
    final_set = second_set - new_set
    #returns a list of which ones are testing files and which ones aren't
    return test_list_index

def weight_list():
    weight_list = []
    #real nums
    for i in range(64):
        col = []
        #real values
        for j in range(10):
            col.append(random.uniform(-0.15, 0.15))
        weight_list.append(col)
    return weight_list

#
#
#STOPPED HERE 
#
#

def get_activation(input_list,index, weight_list):
    counter = 0.0
    example = input_list.split(" ")
    for num in range(64):
        counter += (float(example[num]) * weight_list[num][index])
    sigmond = 1/ (1 + math.exp(-counter))
    return sigmond
    #have to run this ten times in main function
   
    #sigmond of sum of the weights
   
def find_error(sigmond_list, output_List):
    " "
    output_example = output_List.split(" ")
    error_list = []
    for number in range(10):
        error = float(output_example[number]) - sigmond_list[number]
        error_list.append(error)
    return error_list

def back_propogation(input_list, weight_list, index, errors):
    sum_all = 0.0
    input_example = input_list.split(" ")
    for num in range(64):
        sum_all += (float(input_example[num]) * weight_list[num][index])
    sigmond_der = (1/ (1 + math.exp(-sum_all))) * ( 1 - (1/ (1 + math.exp(-sum_all))))
    for num in range(64):
        #print(float(input_example[num]))
        print("This is sig" + str(sigmond_der))
        weight_list[num][index] = weight_list[num][index] + (0.1 * float(input_example[num]) * errors[index] * sigmond_der)
    return weight_list

read_file("digit-examples-all.txt")