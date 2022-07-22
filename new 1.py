#Library Import
import glob
#Library Import
import pandas as pd

# The file path
path = "C:\Users\Vishal\Downloads\Engineering Test Risk Analytics\Engineering Test Risk Analytics\Engineering Test Files"

# Finds the excel files from the provided path
file_list = glob.glob(path + "/*.xlsx")

#List all the excel files read it
#start the merging appending process
excl_list = []

for file in file_list:
	excl_list.append(pd.read_excel(file))

# Concatinating all the files
excl_merged = pd.concat(excl_list, ignore_index=True)

# Store in the specifed files
excl_merged.to_excel('Combined.xlsx', index=False)
