# Prapare & Process Data

## Using Python
I write a Python script for this it do the following thinks.
1) Using re.split(r'\s{2,}', line) to separate by 2+ spaces
2) Remove extra spaces and tabs
3) Hidden characters ('\n')
4) Blank lines
5) Avoid extra blank rows in the csv (lineterminator='\n')

Result: Clean, perfectly aligned CSV - ready for Excel or SQl

## Using Excel (Power Query) to clean data
1) Import text files via Data → Get Data → From Text/CSV.
2) Split by two spaces and trim/clean columns.
3) Remove blanks, rename headers, and fix numeric errors.
4) Change column types or filter invalid rows to load cleanly

## using Excel to more clean the data
1) Remove blank and null using filtering and sorting

## Using SQL for more processing the data

### First use python script and  SQLite3 to enter clean data to database for furthur prossing
* I Create SQLite3 Database then create table acording to data.
* Here i use python script to to insert data to SQLLite3 table
