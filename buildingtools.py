#always add imports at the top
import random
#random number generator, to be used as the function random.randint
import operator
import matplotlib.pyplot
import time
#plots the agents on a graph


#def defines our own functions and reuses them throughout the programme
def distance_between(agents_row_a, agents_row_b):
#two rows in the list and the value between them
    dist = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    return dist

random_seed = 1
random.seed(random_seed)
#this means the random is set, so won't get different answers each time

num_of_agents = 10
num_of_iterations = 100
agents = []
distances = []
#this is creating an empty list, to add to this we will need to use the append command later on

#range allows us to loop through a sequence of numbers
#for command is what makes the loop
#this below is making the agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
#this is adding data to the agents list we made above
#random.randint is the function we imported to generate a random number


# Move the agents with this code below
#i,j,k is like how x is used as an example letter
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
#% divides the number if over the range aka 100 (79 wouldn't be impacted but 100 would)
#79%100 would stay as 79
#100%100 would put this to 0 to ensure the dot isn't lost out of the world aka. bounces it back


#this section is just to produce the graph in the console
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

#distance = distance_between(agents[0], agents[1])
#print(distance)

start = time.clock()
#this starts the clock running as your code begins

for agents_row_a in agents:
    for agents_row_b in agents:
        if (agents_row_a > agents_row_b):
            #this optimises the loop so no repetitions
#this is a for loop in a loop so A will stay as 1 and B will go through to 10, and then A will move to 2 and keep going to find all distances
            distance = distance_between(agents_row_a, agents_row_b)
            distances.append (distance)
#for random agent 1(out of 10) and for agent 2 (out of 10) find the distance between them, and it will continue
        
end = time.clock()
#this ends the clock running time

print("time = " + str(end - start))

print(distances)

high = max(distances)
low = min(distances)
#high and low are assigned the highest and lowest variable in the distance list

print (high, low)
