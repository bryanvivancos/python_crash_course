import plotly.express as px

from die.die import Die

die_1 = Die(8)
die_2 = Die(8)

#make rolls and store results in a list
results = []
for time in range(10000):
    result_1 = die_1.roll()
    result_2 = die_2.roll()
    result = result_1 + result_2
    results.append(result)

#analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_res = range(2,max_result + 1)

for value in poss_res:
    frecuency = results.count(value)
    frequencies.append(frecuency)

print(frequencies)

#visualize the results
title = "Results of Rolling two D8 1,000 times"
labels = {'x':'Result','y':'Frequency of Result'}
fig = px.bar(x= poss_res,y= frequencies,title= title, labels= labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()