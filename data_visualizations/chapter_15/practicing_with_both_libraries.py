#using matplotlib
import matplotlib.pyplot as plt
from die.die import Die

#using plotly
import plotly.express as px
from random_walks.random_walks import RandomWalk

"""Using matplotlib for roll a die"""

die_1= Die()
die_2= Die()

results = [die_1.roll() + die_2.roll() for time in range(10000)]

#analyze the results

max_result = die_1.num_sides + die_2.num_sides 
possibilites = range(2, max_result + 1)

frequencies = [results.count(value) for value in possibilites]

#plot with matplotlib
fig, ax = plt.subplots()

ax.bar(possibilites,frequencies,edgecolor = 'white',linewidth = 0.7)
ax.set_title("Whats happens when you roll three D6 dice",fontsize=10)
ax.set_xlabel('Reults',fontsize=10)
ax.set_ylabel('Frequency',fontsize=10)

ax.tick_params(labelsize=10)

plt.show()

"""Using plotly for molecular motion"""

#make a random walk
rw = RandomWalk()
rw.fill_walk()

#plotting the points
fig = px.scatter(x= rw.x_values,y= rw.y_values)
fig.show()