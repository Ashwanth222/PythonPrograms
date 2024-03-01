class Animal:

    def eat(self):
        print("it can eat")

    def sleep(self):
        print("it can sleep")

class Dog(Animal):

    def run(self):
        print("it can run")

dog = Dog()

dog.eat()
dog.run()
dog.sleep()
