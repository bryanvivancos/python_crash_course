from random import choice

class RandomWalk:
    #clase que define una caminata random
    def __init__(self,num_points=5_000):
        self.num_points = num_points
        
        #starts
        self.x_values = [0]
        self.y_values = [0]
        
    def get_step(self):
        #making the direction and distance for each step 
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        step = direction * distance
        
        return step
        
    def fill_walk(self):
        #randon walk
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            
            if x_step == 0 and y_step == 0:
                continue
            
            #calculate new position from the last point (x_value or y_value)
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)