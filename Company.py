# Author: Mandeep Singh
# Contact: msingh98@uw.edu
# Developed for: ServiceNow

# The company class stores the required information for a particular
# company, it's products and their cost, and the total cost of all
# products

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

    # The function adds the name of a product and it's cost to the dict
    # of products for the company.
    #   name: The name of the product
    #   cost: The cost of the product
    def add_product(self, name, cost):
        self.__total_cost = cost + self.__total_cost
        if name not in self.__products.keys():
            self.__products[name] = cost
        else:
            self.__products[name] = self.__products[name] + cost

    # This function prints the information stored in the Class in a two-level
    # tree format. The products are printed in alphabetically ascending order.
    # The costs are formatted with commas.
    def print_cost(self):
        print(self.__name + " ${:,}".format(self.__total_cost))
        for x in sorted(self.__products.keys()):
            print("  " + x + " ${:,}".format(self.__products[x]))
