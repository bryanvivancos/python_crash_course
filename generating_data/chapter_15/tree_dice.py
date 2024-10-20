import plotly.express as px
from die.die import Die

die_1= Die()
die_2= Die()
die_3= Die()

results = []
for time in range(10000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

#analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
possibilites = range(3, max_result + 1)

for value in possibilites:
    frecuency = results.count(value)
    frequencies.append(frecuency)


title= "Whats happens when you roll three D6 dice"
labels= {'x':'Reults','y':'Frequency'}
fig = px.bar(x= possibilites,y= frequencies,title=title,labels=labels)
# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()