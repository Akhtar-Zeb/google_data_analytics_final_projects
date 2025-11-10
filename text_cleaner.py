import os
import re
import csv

# Company name list
company_list = ["stanley", "usawa", "azmat", "organic",]

while True:
    # Prompt for company name
    company_name = input("Enter company name: ").strip().lower()
    if company_name in company_list:
        break
    else:
        print(f"Company {company_name} not in list.")

files_list = ["CUST.txt", "PROD.txt", "TRANBNS.txt", "TRANBSRET.txt", "TRANS.txt", "TRANSRET.txt"]

while True:
    #Prompt for file name
    file_name = input("Enter file name: ").strip()
    if file_name in files_list:
        break
    else:
        print(f"File {file_name} not in list.")

def main():
    file_path = f"dirty_data/{company_name}/{file_name}"
    # Check name and send it to specific function
    if file_name == "CUST.txt":
        customers(file_path)
    elif file_name == "PROD.txt":
        products(file_path)
    elif file_name == "TRANS.txt":
        transactions(file_path)
    else:
        print("File not found.")

# Clean customer(CUST.txt) text file
def customers(inputfile):
    # make sure folder is exist
    os.makedirs("clean_data", exist_ok=True)
    os.makedirs(f"clean_data/{company_name}", exist_ok=True)
    # Save output file to clean_data folder
    output_file = f"clean_data/{company_name}/customers_clean.csv"

    # Create Empty list for clean data
    clean_data = []
    # Open file with read mode
    with open(inputfile, "r") as infile:
        # Perse file line by line
        for line in infile:
            # Split line by two are more space
            parts = re.split(r'\s{2,}', line.strip())

            # append parts to list
            clean_data.append(parts)
    
    # Open file for write mode
    with open(output_file, "w") as outfile:
        writer = csv.writer(outfile, lineterminator='\n')
        # Give file a Header row
        writer.writerow(["customer_id", "customer_name", "customer_location"])

        # Parse clean data list
        for line in clean_data:
            # Validate Data
            if not line[0].isdigit() or line[1] == "NILL" or line[1].strip() == "":
                continue
            # Remove extra character from line
            # check if line is greater or equal to 3 parts if it is only write three parts
            if len(line) >= 3:
                location = " ".join(line[2:])
                writer.writerow([line[0].strip(), line[1].strip(), location.strip()])
            # check if line equal to two then add empty field
            elif len(line) == 2:
                writer.writerow([line[0].strip(), line[1].strip(), ""])

def products(inputfile):
    # make sure folder is exist
    os.makedirs("clean_data", exist_ok=True)
    os.makedirs(f"clean_data/{company_name}", exist_ok=True)
    # Save output file to clean_data folder
    output_file = f"clean_data/{company_name}/products_clean.csv"

    # Create Empty list for clean data
    clean_data = []
    # Open file with read mode
    with open(inputfile, "r") as infile:
        # Perse file line by line
        for line in infile:
            # Split line by two are more space
            parts = re.split(r'\s{2,}', line.strip())
            # append parts to list
            clean_data.append(parts)
    
    # Open file for write mode
    with open(output_file, "w") as outfile:
        writer = csv.writer(outfile, lineterminator='\n')
        # Give file a Header row
        writer.writerow(["product_id", "company_name", "product_name", "product_rate"])

        # Parse clean data list
        for line in clean_data:
            if len(line) < 3:
                continue
            # Validate Data
            if not line[0].isdigit():
                continue
            if line[2] == "NILL" or line[2].strip == "":
                continue
            if not line[2].isdigit() or line[2] == "0":
                continue
            # check if line is greater or equal to 3 parts if it is only write three parts
            if len(line) >= 3:
                writer.writerow([line[0], f'{company_name.title()}', line[1].title(), line[2]])
            # check if line equal to two then add empty field
            elif len(line) == 2:
                writer.writerow([line[0], f'{company_name.title()}', line[1].title(), ""])

def transactions(inputfile):
    month = input("Enter month of data Example: 'jan': ").strip()
    year = input("Enter year of data Example: '2025': ").strip()
    # make sure folder is exist
    os.makedirs("clean_data", exist_ok=True)
    os.makedirs(f"clean_data/{company_name}", exist_ok=True)
    # Save output file to clean_data folder
    output_file = f"clean_data/{company_name}/transactions_clean.csv"

    # Create Empty list for clean data
    clean_data = []
    # Open file with read mode
    with open(inputfile, "r") as infile:
        # Perse file line by line
        for line in infile:
            # Split line by two are more space
            parts = re.split(r'\s{2,}', line.strip())

            # append parts to list
            clean_data.append(parts)
    
    # Open file for write mode
    with open(output_file, "w") as outfile:
        writer = csv.writer(outfile, lineterminator='\n')
        # Give file a Header row
        writer.writerow(["customer_id", "product_id", "sale_month", "sale_year", "unit_sale", "product_rate", "total_amount"])

        # Parse clean data list
        for line in clean_data:
            # Validate data
            if not any(char.isdigit() for char in line):
                continue
            # check if line is greater or equal to 3 parts if it is only write three parts
            if len(line) >= 5:
                writer.writerow([line[0], line[1], f'{month.title()}', f'{year}', line[2], line[3], line[4]])
            # check if line equal to two then add empty field
            elif len(line) == 4:
                writer.writerow([line[0], line[1], f'{month.title()}', f'{year}', line[2], line[3], ""])


if __name__ == "__main__":
    main()