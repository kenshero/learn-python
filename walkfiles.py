import os
import os.path
from datetime import date, datetime

f = []
for (dirpath, dirnames, filenames) in os.walk("source_files/package_files/"):
    f.extend(filenames)
    
print(f)

source_file_name = "testPackageBatch1-2016-10-27 15:06:33.061780.csv"

list_files = ['testPackageBatch1-2016-10-27 14:19:49.377870.zip',
 'testPackageBatch1-2016-10-27 14:39:10.975501.zip',
 'testPackageBatch1-2016-10-27 14:30:22.493240.zip',
 'testPackageBatch1-2016-10-27 14:46:48.341791.zip',
 'testPackageBatch1-2016-10-27 15:06:33.061780.zip',
 'testPackageBatch1-2016-10-27 15:04:06.347015.zip',
 'testPackageBatch1-2016-10-27 14:34:13.991889.zip',
   'testPackageBatch1-2016-10-27 14:54:06.947720.zip',
   'testPackageBatch1-2016-10-27 14:23:53.580227.zip',
   'testPackageBatch1-2016-10-27 15:05:11.124646.zip']

have_file = 'testPackageBatch1-2016-10-27 15:06:33.061780.csv'.replace('.csv', '.zip') in list_files

print("have_file : ", have_file)

print(date.today())