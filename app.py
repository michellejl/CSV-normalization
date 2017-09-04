#!/usr/bin/python3

import csv
import codecs

# Get a file name from stdin and save it to selectedFile variable
selectedFile = input('Enter the name of a CSV formatted file to normalize: ')
print('Normalizing ' + selectedFile + '...\n')

# Temporarily setting file name in code to save time while building project.
# TODO: Delete this and uncomment lines above for final
# selectedFile = 'sample.csv'
# selectedFile = 'sample-with-broken-utf8.csv'


# Use csv module to read all information from selectedFile
# TODO: clean this up and make it all nice and DRY
try:
    with codecs.open(selectedFile, encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        alldata = []
        for row in readCSV:
            alldata.append(row)
except Exception as e:
    with codecs.open(selectedFile, encoding='utf-8', errors='replace') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        alldata = []
        for row in readCSV:
            alldata.append(row)
    print("Non UTF-8 characters were found in this file and replaced.\n")


# pull the headers off of the main data object
headers = alldata.pop(0)

def checkZipCode(data):
    """
    Checks length of Zip Code item.
    If less than required length (5): add leading 0s
    If more than required length (5): remove after digit 5
    """
    if len(data) < 5:
        while len(data) < 5:
            data = '0' + data
    elif len(data) > 5:
        data = data[0:4]
    # print(data)
    return (data)


def checkTimeStamp(data):
    # TODO: Look more. There has to be a more straight forward way to do this
    timeStamp = data.split(' ')

    # Reorder date
    dateSplit = timeStamp[0].split('/')
    year = '20' + dateSplit[2]
    month = dateSplit[0]
    if len(month) < 2:
        month = '0' + month
    day = dateSplit[1]
    if len(day) < 2:
        day = '0' + day

    # Convert Time
    ampm = timeStamp[2]
    time = timeStamp[1].split(':')
    hour = int(time[0])

    # Convert to 24hr time
    if ampm == ('pm' or 'PM'):
        hour = hour + 12

    # Convert to UTC
    hour = hour + 7

    # Put everything back together
    convertedTime = str(hour) + ':' + time[1] + ':' + time[2] + '-04:00'
    date = year + '-' + month + '-' + day
    convertedDateTime = date + 'T' + convertedTime
    return (convertedDateTime)


def checkFullName(data):
    # TODO: Get clarification on requirement:
    # Not sure if you wanted first letter capital (.title())
    # or all the letters transformed to uppercase (.uppercase())
    data = data.title()
    # TODO: Check: does this work on non-English names?
    return (data)


def checkDuration(data):
    time = data.split(':')
    convertHoursToSeconds = float(time[0]) * 60 * 60
    convertMinutesToSeconds = float(time[1]) * 60
    totalSeconds = convertHoursToSeconds + convertMinutesToSeconds + float(time[2])
    return (totalSeconds)


def getTotalDuration(foo, bar):
    return (foo + bar)

for row in alldata:
    row[0] = checkTimeStamp(row[0])
    # non utf-8 characters have been replaced already. Address section left alone
    row[2] = checkZipCode(row[2])
    row[3] = checkFullName(row[3])
    row[4] = checkDuration(row[4])
    row[5] = checkDuration(row[5])
    row[6] = getTotalDuration(row[4], row[5])
    # non utf-8 characters have been replaced already. Note section left alone


# TODO: right now I am just spitting the information out. I need to write it back into a new file
alldata.insert(0, headers)
print(alldata)
