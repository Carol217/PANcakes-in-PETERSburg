#Pancakes in Petersburg
#Shaina Peters and Carol Pan
#HWO3
#2017

#got a reader
import csv

'''Step 1: read file'''
dictv = {'':''}
target_doc = csv.reader(open('occupations.csv', 'rU'), delimiter = ",", quotechar = "\"")
for row in target_doc:
	dictv[row[0]] = row[1]
	#print dictv
print dictv
