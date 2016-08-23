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
    start_date			time_stamp 	not null,
    start_station		varchar		not null,
    start_terminal		sint64		not null,
    end_date			time_stamp 	not null,
    end_station			varchar		not null,
    end_terminal		sint64		not null,
    bike_no				sint64		not null,
    PRIMARY KEY(
        (quantum(start_date, 80, 'd')),
         start_date 
    )
)
WITH (
    n_val = 1
)
"""

try:
    client.ts_query(table, query)
    print("Table '{}' created successfully".format(table))
except Exception as e:
    print(e)