import pandas as pd
import psutil
import os

#Pick the file

file_name =

# Check file isnt too big for memory
free_memory = psutil.virtual_memory().available
file_size = os.path.getsize(file_name)

def memory_available()
  if (file_size * 1.5) > free_memory:
    print("Not enough memory to load file") and quit()
  else:
    pd.read_csv(file_name, error_bad_lines=False)

#check encoding

#check unique counts of columns

# (maybe grep for column colours and sizes to determine those columns) value_counts to determine categories

#counts for each column
