# Import and call the Riak client to connect to your Riak TS node or cluster
# See http://docs.basho.com/riak/ts/latest/developing/python/ for more information
# on how to use the Riak client for Python
from riak import RiakClient
client = RiakClient()

from datetime import datetime
import csv

table = "Bike_Share_Trip"

# write_date method does the heavy lifting of storing the data to our table 
def write_data (data_to_write):
    result_message = ""
    try:   
        #Create new tsObject and save to the database with .store()
        table_object = client.table(table).new(data_set)
        result = table_object.store()
        result_message = "Records written: {}".format(result)
    except Exception as e:
        result_message = "Error: {}".format(e)
    return result_message

# Convert the string representation of a date to a date with the proper time zone
def convert_string_to_date(date_to_convert):
    first_split = date_to_convert.split(' ')
    date_split = first_split[0].split('/')
    time_split = first_split[1].split(':')

    try:
        date_out = datetime(int(date_split[2]), int(date_split[0]), int(date_split[1]), int(time_split[0]), int(time_split[1]))
        return date_out
    except Exception, e:
        return None

data_set = []
batch_count = 0
total_count = 0

# Read our csv file, iterate over each row, create batches of 100 rows, and
# send the batches to write_data() to write the data to our table
with open('201508_trip_data.csv') as csvfile:
    rows = csv.reader(csvfile, delimiter=',', quotechar="'" )

    for row in rows:
        try:
            # Convert data strings to date objects
            start_date = convert_string_to_date(row[2])
            end_date = convert_string_to_date(row[5])
            
            # Create a new row removing the last couple of columns from the original row
            # that we don't want to save to our table, append the row to our batch (data_set)
            new_row = [int(row[0]), int(row[1]), start_date, row[3], int(row[4]), end_date, row[6], int(row[7]), int(row[8])]
            print new_row
            
            if total_count > 0:
                data_set.append(new_row)
 
            total_count = total_count + 1
            batch_count = batch_count + 1
 
            if batch_count == 100:
                print write_data(data_set)
                data_set = []
                batch_count = 0
        except Exception, e:
            print e

print write_data(data_set)
print "Total Records: " + str(total_count - 1)
