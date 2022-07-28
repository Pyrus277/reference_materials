## Apache Hive

Data Engineer: "I hate having to write muliple lines of Java to do what would take 1 or 2 lines in SQL when talking to this HDFS db."
Hive: "Allow me to introduce myself."

**Hive is a Query engine**
People refer to it as a DB, but technically it's just an SQL interface for HDFS.

Mainly used to compliment the Hadoop filesystem with its interface.
Lets users talk to Hadoop with SQL-like queries called HQL, or Hive Query language to extract data.

These HQL queries are converted to MapReduce jobs (Java Code for ETL) that talk to Hadoop and HDFS filesystems.

#### Uses of Hive
- OLAP processing

#### What Hive can't be used for
- A relational DB
- OLTP
- Real time updates or queries
- Scenarios where low latency data retrieval is expected

#### Qualities of Hive
- Schema on read
- Stores on HDFS, so it can store 100s of petabytes of data


#### External Tables
An external table describes the metadata/schema on external files. These are stored in an RDBMS and used when files are already present or in remote locations.  

### Partitions
Hive breaks huge tables into **partitions** to more efficiently query their contents.  
This process makes it so when we retrieve data, only data from a specified partition will be queried. 
Look up the commands on how to actually partition your tables.



#### Other notes
Hive stores its metadata in an RDBMS. This is completely separate from where your working data is stored in a HDFS.
Hive can also be used with S3.
