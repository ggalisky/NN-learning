#5.28.2023 ggalisky

"""
Suppose we take all the weights and biases in a network of perceptrons, and multiply them by a positive constant, c>0
. Show that the behaviour of the network doesn't change.

----
going to have 3 inputs, middle layer will have 2 perceptrons (A and B). Final layer will have 1 perceptron (C) and will be the output stage

"""

import math

#CONSTANTS
x1 = 1
x2 = 0
x3 = 1

x_list = [x1,x2,x3]

A_weights = [0.5,0.3,0.2]
B_weights = [0.5,0.4,0.4]
C_weights = [0.6,0.9]

A_bias = -3
B_bias = 2
C_bias = -2

mult_contstant = 6

def sum_with_bias(input_list,weight_list, bias):

    input_list_index = 0

    sum = 0

    for item in weight_list:

        sum = item*input_list[input_list_index] + sum

        input_list_index+=1

    sum = sum + bias

    if(sum <= 0):
        return 0
    

    return 1

def sum_with_bias_sigmoid(input_list,weight_list, bias):

    input_list_index = 0

    sum = 0

    for item in weight_list:

        sum = item*input_list[input_list_index] + sum

        input_list_index+=1

    sum = 1/(1+math.exp(-(sum + bias)))

    return sum

def multiply_list(list, mult):
    return [i * mult for i in list]

if __name__ == '__main__':
    
    print("alive")

    A = sum_with_bias(x_list, A_weights, A_bias)
    B = sum_with_bias(x_list, B_weights, B_bias)

    AB_list = [A,B]

    C = sum_with_bias(AB_list,C_weights, C_bias)

    print("give inputs: ", x_list)
    print("the output from our perceptrons is:", C)

    A = sum_with_bias(x_list, multiply_list(A_weights,mult_contstant), A_bias*mult_contstant)
    B = sum_with_bias(x_list, multiply_list(B_weights,mult_contstant), B_bias*mult_contstant)

    AB_list = [A,B]

    C = sum_with_bias(AB_list,multiply_list(C_weights, mult_contstant), C_bias*mult_contstant)

    print("give inputs: ", x_list)
    print("and constant:", mult_contstant)
    print("the output from our perceptrons is:", C)

    print("alive")

    A = sum_with_bias_sigmoid(x_list, A_weights, A_bias)
    B = sum_with_bias_sigmoid(x_list, B_weights, B_bias)

    AB_list = [A,B]

    C = sum_with_bias_sigmoid(AB_list,C_weights, C_bias)

    print("give inputs: ", x_list)
    print("the output from our sigmoid neurons is:", C)


    A = sum_with_bias_sigmoid(x_list, multiply_list(A_weights,mult_contstant), A_bias*mult_contstant)
    B = sum_with_bias_sigmoid(x_list, multiply_list(B_weights,mult_contstant), B_bias*mult_contstant)

    AB_list = [A,B]

    C = sum_with_bias_sigmoid(AB_list,multiply_list(C_weights, mult_contstant), C_bias*mult_contstant)

    print("give inputs: ", x_list)
    print("and constant:", mult_contstant)
    print("the output from our sigmoid neurons is:", C)


     

    

   