# Copy the required file_path from your file
# Import required modules
# The log_file looks like this
# 03/22 08:51:06 INFO   :.....mailslot_create: creating mailsl .....
# 03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated .....
# 03/22 08:51:06 INFO   :.....mailslot_create: creating mailslot ....
# 03/22 08:51:06 INFO   :....mailbox_register: mailbox 

import re
from collections import defaultdict

def counting(file_path):
     log_pattern = re.compile(r'(\d{2}/\d{2}) (\d{2}:\d{2}:\d{2}) (\w+)(\s*)(.+)')
     result = defaultdict(int)

     with open(file_path, 'r') as file:
          for line in file: # Iterate over each line from the log_file

               match = log_pattern.match(line) # Match the compiled line
               if match:
                    level = match.group(3)
                    result[level] += 1
     
     for level, count in result.items(): # Display result in the console
          print(f'{level}: {count}')

log_file_path = 'insert your file_path here like: #C//.;;;....' # Select the file path of your file

counting(log_file_path) # Call the counting functionwith the file_path.
