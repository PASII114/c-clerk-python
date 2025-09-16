#Create 3 classes Cook Waiter and Singer | These classes should have a single method to perform their activities
#create robo class and inherit above classes

class Cook:

    def cooking(self):
        print("The chef is cooking")

class Waiter:

    def serving(self):
        print("The waiter is serving")

class Singer:

    def singing(self):
        print("The singer is singing")

class Robo(Cook, Waiter, Singer):
    pass

robo_obj = Robo()

robo_obj.cooking()
robo_obj.serving()
robo_obj.singing()