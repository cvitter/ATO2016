# ATO2016 - Easy Time Series Analysis

This GitHub repository contains instructions and code to reproduce the work demonstrated in my **All Things Open** 2016 Presentation: **Easy Time Series Analysis with NoSQL, Python, Pandas and Jupyter** (https://allthingsopen.org/talk/easy-time-series-analysis-with-nosql-python-pandas-jupyter/).

To run the examples contained in this repo you will need to:

1. Download and install Riak TS (http://docs.basho.com/riak/ts/);
1. Have Python installed on your local computer;
1. Install the Riak Python client using either Easy Install (easy_install riak) or Pip (pip install riak) - Note: Please use Version 2.5.5 or later of the Python client;
1. Install Jupyter Notebook (http://jupyter.org/);
1. Install Pandas (http://pandas.pydata.org/);
1. Clone this repo to your local machine; 
1. Download the Bay Area Bike Share Year 2 data (http://www.bayareabikeshare.com/open-data) used in the example code [1];

Once the pre-requisites are installed/setup on your development environment you can run the example code:

1. Start Riak TS (from the command line navigate to your Riak TS root directory and execute the following command: ``` bin\riak start ```);
2. Run Create_Trip_Table.py script to create the table to store our trip data in;
3. Launch the Riak TS shell from the command line: ``` bin\riak-shell ```
4. Run the ``` DESCRIBE Bike_Share_Trip; ``` command within riak-shell to output the new table's schema as illustrated below:

```
+--------------+---------+-------+-----------+---------+
|    Column    |  Type   |Is Null|Primary Key|Local Key|
+--------------+---------+-------+-----------+---------+
|   trip_id    | sint64  | false |           |         |
|   duration   | sint64  | false |           |         |
|  start_date  |timestamp| false |     1     |    1    |
|start_station | varchar | false |           |         |
|start_terminal| sint64  | false |           |         |
|   end_date   |timestamp| false |           |         |
| end_station  | varchar | false |           |         |
| end_terminal | sint64  | false |           |         |
|   bike_no    | sint64  | false |           |    2    |
+--------------+---------+-------+-----------+---------+
```

5. .
6. .

## Notes 

[1] It is always best to get data right from the source: http://www.bayareabikeshare.com/open-data
