#Pancakes in Petersburg
#Shaina Peters and Carol Pan
#HW03 - Stl/O: Divine Your Destiny!
#2017-09-18

#got a reader
import csv
#and the random generator
import random

'''Step 1: turn csv into a dictionary'''
#instantiate a dictionary to add in the occupations
DICTV = {}

#code for reading csv taken from Stack
target_doc = csv.reader(open('occupations.csv', 'rU'), delimiter = ",", quotechar = "\"")

#goes row by row and inputs job name as key, and percentage as element
for row in target_doc:
        #don't want Job Class : Percentage or Total: 99.8
        if row[1] != 'Percentage' and row[0] != 'Total':
                DICTV[row[0]] = float(row[1])
#test to make sure construction successful
#print DICTV #successful

'''Step 2: write a function that returns a randomly selected occupation with weight'''

def job_generator ():
        #here is the randomness
        val = random.random() * 99.8
        #print val

        #for each key in DICTV (which is the job class)
        for x in range(0, len(DICTV.keys()) - 1):
                #take the job's percentage away from random value
                val = val - DICTV[DICTV.keys()[x]]
                #until below 0 is reached
                '''
                The idea here is that each job class has an interval, denoted by percentage.
                The random number generator gives a value between [0, total percentage)
                Now the function will look for the correct 'interval' to place the random #
                It does this by subtracting the current interval and seeing if it hits 0
                The effects of the subtraction linger.
                '''
                if val < 0:
                        print DICTV.keys()[x];
                        return; #found it, stop the fxn

#have to do batches for tests to test whether code is correct
for x in range(0,100):
        job_generator()

'''
during runs, 'Office & admin support' was pretty common
in contrast, code had to be run 3 times for 'farming' to come up
Conclusion: seems right
'''

#Question: is there a more efficient way to do thi?
