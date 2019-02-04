class Company:
    def __init__(self, name):
        self.__name = name
        self.__total_cost = 0
        self.__products = {}

    @property
    def name(self):
        return self.__name

    @property
    def total_cost(self):
        return self.__total_cost

    @property
    def products(self):
        return self.__products

    def add_product(self, name, cost):
        self.__total_cost = cost + self.__total_cost
        self.__products[name] = cost

    def print_cost(self):
        print(self.__name + " ${:,}".format(self.__total_cost))
        for x in sorted(self.__products.keys()):
            print("  " + x + " ${:,}".format(self.__products[x]))
