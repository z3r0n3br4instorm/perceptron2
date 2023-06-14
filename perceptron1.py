import os
import time
import random
global w1,w2,w3,b,dataset
b = 0
dataset = []
count = []
loop_set = 0
neuron_correct = 0
#x1 = Color (0 if orange, 1 if red)
#x2 = Weight
#x3 = Diameter
def debug(print_data):
    print("[DEBUGGER] "+print_data)
def generate_data():
    debug("Range of weights for an apple 120-130, for orange <120, diameter for apple 10> for orange 10< and color")
    global w1,w2,w3, dataset
    w1 = random.random()
    w2 = random.random()
    w3 = random.random()
    #Generate Dataset
    for _ in range(1000):
        # Generate random weight for apples (120-130)
        weight_apple = random.uniform(120, 130)

        # Generate random weight for oranges (100-115)
        weight_orange = random.uniform(100, 115)

        # Generate random internal diameter for both fruits
        diameter = random.uniform(5, 10)

        # Generate random color: 0 for orange, 1 for red
        color = random.randint(0, 1)

        if color == 0:
            dataset.append((0, weight_orange, diameter, color))
        else:
            dataset.append((1, weight_apple, diameter, color))

def neuron_function(x1,x2,x3):
    global b
    #Activation Calculation Function
    fx = (w1*x1)+(w2*x2)+(w3*x3)-b
    return fx

def training_function():
    #Feed the data to the function and check the output
    global dataset,b,count, loop_set, neuron_correct
    for x in dataset:
        if (neuron_function(x[3],x[1],x[2])) > 0:
            count.append(1)
        else:
            count.append(0)
    #Comparing the Neuron output and true output
    while True:
        if dataset[loop_set][0] == count[loop_set]:
            # print("Outputs mached !")
            # print("True Output :",x[0],"\nNeuron Output :",count[loop_set])
            neuron_correct += 1
        else:
            # print("Outputs Missmatched !, Recalibrating...")
            # print("True Output :",x[0],"\nNeuron Output :",count[loop_set])
            b = round(b + 0.1, 4)
            loop_set = 0
            for i, x in enumerate(dataset):
                if (neuron_function(dataset[i][3], dataset[i][1], dataset[i][2])) > 0:
                    count[i] = 1
                else:
                    count[i] = 0
                # training_function()
        # time.sleep(1)
        #print(b)
        if neuron_correct >= 999:
            print("System Ready")
            print("Neuron Bias value :",b,"Number of loops ran :",neuron_correct)
            break
        loop_set+=1

def main():
    print("This is an artificial neuron that can say if a fruit is an orange or an apple if the weight, diameter and color is given")
    print("Starting Program")
    print("Generating Data...")
    generate_data()
    print("Running training function...")
    training_function()
    print("Training Complete !")
    while True:
        c = str(input("Enter the color :"))
        if c == "red":
            c = int(1)
        elif c == "orange":
            c = int(0)
        u = int(input("Enter the Weight :"))
        m = int(input("Enter the Diameter :"))
        if neuron_function(c,u,m) > 0:
            print("Apple")
        else:
            print("Orange")
main()
    