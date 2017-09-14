#Pancakes in Petersburg
#Shaina Peters and Carol Pan
#HWO3
#2017

#got a reader
import csv

'''Step 1: read file'''
target_doc = csv.reader(open('../occupations.', 'rU'), delimiter = ",", quotechar = "|")
print target_doc
