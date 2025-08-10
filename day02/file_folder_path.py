import os
import sys
folder_path = os.path.dirname(__file__)
folder_path = os.path.dirname(folder_path)
print(folder_path)

test_file_path = os.path.join(folder_path, 'test.txt')
with open(test_file_path, 'r') as file:
  lines = file.readlines()

for line in lines:
  print(line)