# class Computer1:
#
#     def __init__(self):
#         self.price = 900
# 
#     def sell(self):
#         # print(f"selling price is {self.price}")
#         print("selling price is: {}" .format(self.price))
#
#     def setPrice(self, price):
#         self.price = price
#
# c = Computer1()
# c.sell()
#
# # change the price
# c.price = 1000
# c.sell()
#
# # using setter function
# c.setPrice(1000)
# c.sell()


# #
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()