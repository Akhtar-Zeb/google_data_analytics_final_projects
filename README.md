# Prapare Data & Process Data

## Using Python
1) Using re.split(r'\s{2,}', line) to separate by 2+ spaces
2) Remove extra spaces and tabs
3) Hidden characters ('\n')
4) Blank lines
5) Avoid extra blank rows in the csv (lineterminator='\n')

Result: Clean, perfectly aligned CSV - ready for Excel or SQl

## Using with Excel (Power Query)
1) Import text files via Data → Get Data → From Text/CSV.
2) Split by two spaces and trim/clean columns.
3) Remove blanks, rename headers, and fix numeric errors.
4) Change column types or filter invalid rows to load cleanly

## 