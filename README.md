# All Things Open 2016 - Easy Time Series Analysis

This GitHub repository contains instructions and code to reproduce the work demonstrated in my **All Things Open** 2016 Presentation: **Easy Time Series Analysis with NoSQL, Python, Pandas and Jupyter** (https://allthingsopen.org/talk/easy-time-series-analysis-with-nosql-python-pandas-jupyter/).

To run the examples contained in this repo you will need to:

1. Download and install Riak TS (http://docs.basho.com/riak/ts/);
1. Have Python installed on your local computer;
1. Install the Riak Python client using either Easy Install (easy_install riak) or Pip (pip install riak) - Note: Please use Version 2.5.5 or later of the Python client;
1. Install Jupyter Notebook (http://jupyter.org/);
1. Install Pandas (http://pandas.pydata.org/);
1. Clone this repo to your local machine; 
1. Download the Bay Area Bike Share Year 2 data (http://www.bayareabikeshare.com/open-data) used in the example code [1];

Once the pre-requisites are installed/setup on your development environment you create the table that we are going to use to read and write our data:

1. Start Riak TS (from the command line navigate to your Riak TS root directory and execute the following command: ``` bin/riak start ```);
1. Run Create_Trip_Table.py script to create the table to store our trip data in (``` python Create_Trip_Table.py ```);
1. Launch the Riak TS shell from the command line: ``` bin/riak-shell ```
1. Run the following commands within riak-shell to list the tables in your Riak TS database and output the new table's schema:
```
riak-shell(1)>SHOW TABLES;
+---------------+
|     Table     |
+---------------+
|Bike_Share_Trip|
+---------------+


riak-shell(2)>DESCRIBE Bike_Share_Trip;
+--------------+---------+-------+-----------+---------+--------+----+
|    Column    |  Type   |Is Null|Primary Key|Local Key|Interval|Unit|
+--------------+---------+-------+-----------+---------+--------+----+
|   trip_id    | sint64  | false |           |         |        |    |
|   duration   | sint64  | false |           |         |        |    |
|  start_date  |timestamp| false |     1     |    1    |   7    | d  |
|start_station | varchar | false |           |         |        |    |
|start_terminal| sint64  | false |           |         |        |    |
|   end_date   |timestamp| false |           |         |        |    |
| end_station  | varchar | false |           |         |        |    |
| end_terminal | sint64  | false |           |         |        |    |
|   bike_no    | sint64  | false |           |    2    |        |    |
+--------------+---------+-------+-----------+---------+--------+----+
```  

In the next series of steps we will load the Bay Are Bike Share data into our newly created table:

1. Place the 201508_trip_data.csv in the directory where your python scripts are located (or update the file's location in Write_Trip_Data.py line 42);
1. Run Write_Trip_data.py (``` python Write_Trip_data.py ```) to import the file's records into your newly created table (when the script completes the final line should say ``` Total Records: 354151 ```);
1. Using riak-shell you can verify that the records have been written by running the following ``` SELECT ``` statement:

```
riak-shell(3)>SELECT * FROM Bike_Share_Trip WHERE start_date > '2014-09-01 10:00:00' AND start_date < '2014-09-01 10:30:00';
+-------+--------+--------------------+--------------------------------+--------------+--------------------+------------------------------+------------+-------+
|trip_id|duration|     start_date     |         start_station          |start_terminal|      end_date      |         end_station          |end_terminal|bike_no|
+-------+--------+--------------------+--------------------------------+--------------+--------------------+------------------------------+------------+-------+
|433020 |  130   |2014-09-01T10:02:00Z|        Clay at Battery         |      41      |2014-09-01T10:04:00Z|       Davis at Jackson       |     42     |  109  |
|433022 |  461   |2014-09-01T10:04:00Z|         Market at 10th         |      67      |2014-09-01T10:12:00Z|        Market at 4th         |     76     |  438  |
|433021 |  461   |2014-09-01T10:04:00Z|         Market at 10th         |      67      |2014-09-01T10:12:00Z|        Market at 4th         |     76     |  498  |
|433024 |  708   |2014-09-01T10:05:00Z|      Golden Gate at Polk       |      59      |2014-09-01T10:17:00Z|      Steuart at Market       |     74     |  100  |
|433025 |  1631  |2014-09-01T10:17:00Z|Grant Avenue at Columbus Avenue |      73      |2014-09-01T10:44:00Z|    Embarcadero at Sansome    |     60     |  416  |
|433026 |  1631  |2014-09-01T10:17:00Z|Grant Avenue at Columbus Avenue |      73      |2014-09-01T10:44:00Z|    Embarcadero at Sansome    |     60     |  549  |
|433027 |  109   |2014-09-01T10:22:00Z|     Embarcadero at Bryant      |      54      |2014-09-01T10:23:00Z|       Spear at Folsom        |     49     |  468  |
|433029 |  333   |2014-09-01T10:29:00Z|Castro Street and El Camino Real|      32      |2014-09-01T10:35:00Z|Mountain View Caltrain Station|     28     |  17   |
+-------+--------+--------------------+--------------------------------+--------------+--------------------+------------------------------+------------+-------+
```



## Notes 

[1] It is always best to get data right from the source: http://www.bayareabikeshare.com/open-data
