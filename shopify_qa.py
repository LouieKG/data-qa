import pandas as pd
import psutil
import os

#Pick the file

file_name =

# Check file isnt too big for memory
free_memory = psutil.virtual_memory().available
file_size = os.path.getsize(file_name)

def memory_available()
  if file_size * 1.5 > free_memory:
    quit()

#check encoding

#check values
