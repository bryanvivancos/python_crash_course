import plotly.express as px
from die.die import Die

die_1= Die()
die_2= Die()

results = [die_1.roll() + die_2.roll() for time in range(10000)]

#analyze the results

max_result = die_1.num_sides + die_2.num_sides 
possibilites = range(2, max_result + 1)

frequencies = [results.count(value) for value in possibilites]

title= "Whats happens when you roll three D6 dice"
labels= {'x':'Reults','y':'Frequency'}
fig = px.bar(x= possibilites,y= frequencies,title=title,labels=labels)
# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()