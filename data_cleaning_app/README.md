# Data cleaning API

### Requirements 
1. REST API to support
   1. upload data as .csv and save the raw data into a SQLite db
      1. upload data 
      2. create new table with the csv headers 
      3. extract data types for each column from csv, if not available, make it a text column
   2. remove duplicates in a dataset
   3. remove NULL values in a dataset 
   4. replace NULL values with a specified value
      1. replace all NULL values with specified value 
      2. replace NULL values for a specified column with a specified value
   5. replace NULL values with the mean
      1. replace all NULL values with the mean by column
      2. replace all NULL values for a specified column with the mean for that column
   6. replace NULL values with the median
      1. replace all NULL values with the median value by column 
      2. replace all NULL values for a specified column with the median for that column
   7. aggregations 
      1. mean
         1. return mean by column 
         2. return mean of a specified column
      2. median 
         1. return median by column 
         2. return median for a specified column
      3. standard deviation 
         1. return std by column 
         2. return std for a specified column 
      4. sliding window average 
         1. return sliding window average for all columns
         2. return sliding window average for a specified column
      5. sliding window average (centered)
         1. return sliding window average for all columns
         2. return sliding window average for a specified column
      6. sliding window std (centered)
         1. return sliding window std for all columns
         2. return sliding window std for a specified column