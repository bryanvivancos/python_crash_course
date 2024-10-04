def makeCar(manufacturer, model_name, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model_name'] = model_name
    
    return kwargs

car = makeCar('subaru','outback',color='blue',tow_package = True)
print(car)    