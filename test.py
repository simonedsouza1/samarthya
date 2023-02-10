class Car:
    def __init__(model,name,colour,price):
        model.colour = colour
        model.name=name
        model.price=price

    def myfunc(model):
        print(f"this is a {model.name}, colour: {model.colour}, price:{model.price}")
    def __str__(model):
        return "name: "+ model.name +", colour: "+str(model.colour),"price:"+(model.price)
c1= Car("volvo","black","70l")
c1.myfunc()
print(c1)






