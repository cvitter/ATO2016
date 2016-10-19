# Create_Trip_Table.py
# Python script that creates the Bike_Share_Trip table in Riak TS

# Import and call the Riak client to connect to your Riak TS node or cluster
# See http://docs.basho.com/riak/ts/latest/developing/python/ for more information
# on how to use the Riak client for Python
from riak import RiakClient
client = RiakClient()

table = "Bike_Share_Trip"

# Create the DDL used to create the new table and execute with .ts_query()
# See http://docs.basho.com/riak/ts/latest/using/planning/ for more information on
# creating Riak TS tables (supported data types, primary keys, etc.)
query = """\
CREATE TABLE Bike_Share_Trip (
	trip_id				sint64		not null,
	duration			sint64		not null,
    start_date			timestamp 	not null,
    start_station		varchar		not null,
    start_terminal		sint64		not null,
    end_date			timestamp 	not null,
    end_station			varchar		not null,
    end_terminal		sint64		not null,
    bike_no				sint64		not null,
    PRIMARY KEY(
        (quantum(start_date, 7, 'd')),
         start_date, bike_no 
    )
)
WITH (
    n_val = 1
)
"""
# Note: By default Riak TS replicates each record 3 times (n_val = 3), in this 
# example we are telling Riak TS to only create 1 copy of each record, if you
# want 3 copies change the 'WITH (n_val = 1)' value or remove the entire line from
# the DDL to revert to the default setting

# Execute our SQL DDL statement with .ts_query()
try:
    client.ts_query(table, query)
    print("Table '{}' created successfully".format(table))
except Exception as e:
    print(e)