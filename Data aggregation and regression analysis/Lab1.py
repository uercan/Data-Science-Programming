import numpy as np
import random


class dataset:  # we declare the parent class which will receive a filename as an argument
    def __init__(self,
                 filename):  # with this init we will not only initialize the dataset, but will get an overview of it and some calculations
        self.f = open(filename)
        self.workingdata = []  # we create two empty lists, one for storing all the data from the dataset and other for storing the ten rows that we will work with
        self.aux = []
        for line in self.f.readlines():  # we read the file in the aux list and we put the header in a separate list
            self.val = line.split(",")
            self.aux.append(self.val)
        self.listheader = self.aux[0].copy()
        self.listheader[-1] = self.listheader[-1].rstrip()
        del self.aux[0]
        print("printing the dataset: ", filename, "\n\n", self.listheader)
        for i in range(0, 10):  # here we put ten random rows in the working data
            self.workingdata.append(self.aux[random.randint(0, len(self.aux))])
            print(self.workingdata[i])
        for i in range(len(self.workingdata[
                               0])):  # after we have printed the dataset, for the numeric values we print mean, standard deviation, variation, and max and min values
            if self.is_number(self.workingdata[0][i]):
                for j in range(10):
                    self.workingdata[j][i] = float(self.workingdata[j][i])
                print("the mean of the row:", self.listheader[i], "is:", self.mean(self.listheader[i]))
                print("the standard deviation of the row:", self.listheader[i], "is:", self.std(self.listheader[i]))
                print("the variation of the row:", self.listheader[i], "is:", self.var(self.listheader[i]))
                print("the maximum value of the row:", self.listheader[i], "is:", self.max(self.listheader[i]))
                print("the minimum value of the row:", self.listheader[i], "is:", self.min(self.listheader[i]))
                print("\n")

    def is_number(self, s):  # helper method to check if an element of the list is a numeric value
        try:
            float(s)
            return True
        except ValueError:
            return False

    def mean(self, row):  # helper function to calculate mean
        self.index = self.listheader.index(row)
        if isinstance(self.workingdata[0][self.index], float):
            self.auxarray = []
            for i in range(0, 10):
                self.auxarray.append(self.workingdata[i][self.index])
            return np.mean(self.auxarray)
            self.auxarray.clear()
        else:
            print("not a numeric value")

    def std(self, row):  # helper function to calculate standard deviation
        self.index = self.listheader.index(row)
        if isinstance(self.workingdata[0][self.index], float):
            self.auxarray = []
            for i in range(0, 10):
                self.auxarray.append(self.workingdata[i][self.index])
            return np.std(self.auxarray)
            self.auxarray.clear()
        else:
            print("not a numeric value")

    def var(self, row):  # helper function to calculate variation
        self.index = self.listheader.index(row)
        if isinstance(self.workingdata[0][self.index], float):
            self.auxarray = []
            for i in range(0, 10):
                self.auxarray.append(self.workingdata[i][self.index])
            return np.var(self.auxarray)
            self.auxarray.clear()
        else:
            print("not a numeric value")

    def max(self, row):  # helper function to calculate max value
        self.index = self.listheader.index(row)
        if isinstance(self.workingdata[0][self.index], float):
            self.auxarray = []
            for i in range(0, 10):
                self.auxarray.append(self.workingdata[i][self.index])
            return np.max(self.auxarray)
            self.auxarray.clear()
        else:
            print("not a numeric value")

    def min(self, row):  # helper function to calculate min value
        self.index = self.listheader.index(row)
        if isinstance(self.workingdata[0][self.index], float):
            self.auxarray = []
            for i in range(0, 10):
                self.auxarray.append(self.workingdata[i][self.index])
            return np.min(self.auxarray)
            self.auxarray.clear()
        else:
            print("not a numeric value")


# we declare 2 child classes here using inheritance, one for the covid dataset, and the other for the happiness dataset
class covid(dataset):
    def __init__(self):
        dataset.__init__(self, 'WHO-COVID-19-global-data.csv')


class happiness(dataset):
    def __init__(self):
        dataset.__init__(self, '2019.csv')


# we call 2 instances of the child classes
happyclass = happiness()
covidicos = covid()
