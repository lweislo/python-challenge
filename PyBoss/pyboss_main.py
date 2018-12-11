
#PyBoss exercise from UNC Data Analytics Bootcamp Python-3

import os
import csv
import datetime
import re

#Import the dictionary to convert states

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

file_path = os.path.join('employee_data.csv')

with open(file_path, newline='') as f:
    dataset = csv.reader(f, delimiter=',')
    next(dataset)
    
    idn = []
    fn = []
    ln = []
    dob = []
    ssn = []
    st = []
    for row in dataset:
        idn.append(row[0]) #add ID from csv to dataset
        fn.append(row[1].split(' ')[0]) #split the name - first name
        ln.append(row[1].split(' ')[1]) #split the name - last name
        dob.append(datetime.datetime.strptime(row[2], "%Y-%m-%d").strftime("%m/%d/%Y")) #convert date format
        ssn.append('**-' + '***-'+(row[3].split('-')[2])) #mask the SSN
        st.append(us_state_abbrev[row[4]]) #Look up the state and put in code
   
    employees = zip(idn,fn,ln,dob,ssn,st)

# save the output file path
output_file = os.path.join("employee_data2.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

    writer.writerows(employees)

