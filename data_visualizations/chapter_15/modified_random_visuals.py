import matplotlib.pyplot as plt

from random_walks.modified_random_walks import RandomWalk

while True: 
    #make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    #plotting the points
    plt.style.use('classic')
    #fig, ax = plt.subplots(figsize=(15,9),dpi=128)
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values,rw.y_values,linewidth=2)
    ax.set_aspect('equal') #set equal aspect of ticks for each axis
    
    #emphasize the first and last points
    ax.plot(0,0,c='green',linewidth=100)
    ax.plot(rw.x_values[-1],rw.y_values[-1],c='blue',linewidth=100)
    
    #removing the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    keep_running = input('Make anothe plot? (y/n): ')
    if keep_running == 'n':
        break