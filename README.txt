File collect_data.py is used to collect new data. The datasets are saved as .csv files under the directory "dataset".
There are 3 raw datasets that would be collected: crime2017.csv; felony2016.csv; juvenilearrests.csv
Usage: python/python3 collect_data.py


File analysis.py defines variable cleanness to evaluate how messy an attribute is.
There are 2 types of bad values. The first is NaN. The second is values whose dtype is not compatible with attribute's dtype
Therefore the cleanness is defined by numbers of bad value divided by total number of values
Usage: python/python3 analysis.py -f file-path (the default is ./dataset/crime2017.csv)


File clean.py first drop the columns whose messy value is bigger than a certain threshold, then drop the rows with bad values in the 3 least clean columns
After cleaning, save the cleaned data to the same directory with the sub-fix '_cleaned'. For example crime2017.csv will be resaved as crime2017_cleaned.csv
Usage: python/python3 analysis.py -f file-path (the default is ./dataset/crime2017.csv)

File proj1_v1.0.docx is the introduction of this project. It introduces the background of the project, the dataset we use and the problem we will dicuss.

Here is our github link:
https://github.com/da-group/project1
Unfortunately, as one of my teammate said, running python script analysis.py and clean.py on windows will lead to unexpected error.(I do not know whether it is related to windows)
It is about the variable wrong_list in analysis.py. And it looks like it can not make correct logical calculation under his environment.
Therefore I highly recommend to use mac and python 3.6.5, which is my environment, or linux. (I wish it will be OK)


