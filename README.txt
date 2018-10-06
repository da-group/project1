File analysis.py defines variable cleanness to evaluate how messy an attribute is.
There are 2 types of bad values. The first is NaN. The second is values whose dtype is not compatible with attribute's dtype
Therefore the cleanness is defined by numbers of bad value divided by total number of values
Usage: python/python3 analysis.py -f file-path (the default is ./dataset/crime2017.csv)


File clean.py first drop the columns whose messy value is bigger than a certain threshold, then drop the rows with bad values in the 3 least clean columns
Usage: python/python3 analysis.py -f file-path (the default is ./dataset/crime2017.csv)
