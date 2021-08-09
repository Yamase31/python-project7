"""
File: marketModel.py
Author: Harry Pinkerton, James Lawson
Project: 7

Models multiple cashiers.
"""

from cashier import Cashier
from customer import Customer
import random

class MarketModel(object):

    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival, numCashiers):
        self._probabilityOfNewArrival = probabilityOfNewArrival
        self._lengthOfSimulation = lengthOfSimulation
        self._averageTimePerCus = averageTimePerCus
        self._cashiers = []
        for i in range(numCashiers):
            self._cashiers.append(Cashier(i + 1))
   
    def runSimulation(self):
        """Run the clock for n ticks."""
        for currentTime in range(self._lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                self._probabilityOfNewArrival,
                currentTime,
                self._averageTimePerCus)
            
            # if successfully generated, send a customer to a cashier
            if customer != None:
                Min = 999
                
                for i in range(len(self._cashiers)):
                    if self._cashiers[i].customersInLine() < Min:
                        Min = self._cashiers[i].customersInLine()
                        self._cashiers[i].addCustomer(customer)

            # Tell all cashiers to provide another unit of service            
            for cashiers in self._cashiers:
                cashiers.serveCustomers(currentTime)

    def __str__(self):
        """Returns the string rep of the results of the simulation."""
        return  "CASHIER CUSTOMERS   AVERAGE     LEFT IN\n" + \
               "        PROCESSED   WAIT TIME   LINE\n" + \
               "\n".join(map(str, self._cashiers))
