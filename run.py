import os
import glob
from glob import glob
import shutil
from geojson import Polygon
from os.path import join, isdir, isfile
from datetime import datetime

# Set Data Paths
data_path = os.getenv('DATA','/data')

# Define Input Paths
inputs_path = os.path.join(data_path, 'inputs')
ssps_path = os.path.join(inputs_path, 'ssps')
parameters_path = os.path.join(inputs_path, 'parameters')

# Define and Create Output Paths
outputs_path = os.path.join(data_path, 'outputs')
if not os.path.exists(outputs_path):
    os.mkdir(outputs_path)
parameter_outputs_path = os.path.join(outputs_path, 'parameters')
if not os.path.exists(parameter_outputs_path):
    os.mkdir(parameter_outputs_path)
parameter_outputs_path = os.path.join(outputs_path, 'parameters')
if not os.path.exists(parameter_outputs_path):
    os.mkdir(parameter_outputs_path)

# Read environment variables
year = os.getenv('YEAR')
ssp = os.getenv('SSP')

# Identify which of the SSP datasets is needed and move into the correct output folder
# Retain the file name containing the SSP and year
ssps = glob(ssps_path + "/*.*",recursive = True)
print('ssp_data:',ssps)

filename=[]
filename=['xx' for n in range(len(ssps))]
print('filename:',filename)

# Create a list of all of the files in the folder
for i in range(0,len(ssps)):
    test = ssps[i]
    file_path = os.path.splitext(test)
    print('Filepath:',file_path)
    filename[i]=file_path[0].split("/")
    print('Filename:',filename[i])

file =[]

# Identify which file in the list relates to the chosen year / SSP
for i in range(0,len(ssps)):
    if ssp in filename[i][-1]:
        if year in filename[i][-1]:
            file = ssps[i]
            dst = os.path.join(outputs_path, filename[i][-1] + '.zip')
    

print('File:',file)

# Move that file into the correct folder.
src=file

if len(src) !=0:
    print('src:',src)
    print('dst:',dst)
    shutil.copy(src,dst)
else:
    ssp = 'No Data Assigned'
    year = 'No Data Assigned'

# Look to see if a parameter file has been added
parameter_file = glob(parameters_path + "/*.csv", recursive = True)
print('parameter_file:', parameter_file)

# Move the amended parameter file to the outputs folder
if len(parameter_file) == 1 :
    file_path = os.path.splitext(parameter_file[0])
    print('Filepath:',file_path)
    filename=file_path[0].split("/")
    print('Filename:',filename[-1])

    src = parameter_file[0]
    print('src:',src)
    dst = os.path.join(parameter_outputs_path,filename[-1] + '.csv')
    print('dst,dst')
    shutil.copy(src,dst)

    # Print all of the input parameters to an excel sheet to be read in later
    with open(os.path.join(dst), 'a') as f:
        f.write('YEAR,%s\n' %year)
        f.write('SSP,%s\n' %ssp)
