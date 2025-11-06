import os
import sys
import re
import csv

def main():
    # Ask for file path
    input_file = input("Enter file path: ").strip()
    # Split file path and name
    file_name = os.path.basename(input_file)

    # Check name and send it to specific function
    if file_name == "CUST.txt":
        customers(input_file)
    elif file_name == "PROD.txt":
        products(input_file)
    elif file_name == "TRANS.txt":
        transactions(input_file)
    else:
        print("File not found.")

        
# Clean customer(CUST.txt) text file
def customers(inputfile):
    # make sure folder is exist
    os.makedirs("clean_data_using_powerquary", exist_ok=True)
    # Save output file to clean_data folder
    output_file = f"clean_data_using_powerquary/customers_clean.csv"

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
    os.makedirs("clean_data_using_powerquary", exist_ok=True)
    # Save output file to clean_data folder
    output_file = f"clean_data_using_powerquary/products_clean.csv"

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
        writer.writerow(["product_id", "product_name", "product_rate"])

        # Parse clean data list
        for line in clean_data:
            # check if line is greater or equal to 3 parts if it is only write three parts
            if len(line) >= 3:
                writer.writerow(line[:3])
            # check if line equal to two then add empty field
            elif len(line) == 2:
                writer.writerow(line + [""])

def transactions(inputfile):
    # make sure folder is exist
    os.makedirs("clean_data_using_powerquary", exist_ok=True)
    # Save output file to clean_data folder
    output_file = f"clean_data_using_powerquary/transactions_clean.csv"

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
        writer.writerow(["customer_id", "product_id", "unit_sale", "product_rate", "total_amount"])

        # Parse clean data list
        for line in clean_data:
            # check if line is greater or equal to 3 parts if it is only write three parts
            if len(line) >= 6:
                writer.writerow(line[:6])
            # check if line equal to two then add empty field
            elif len(line) == 5:
                writer.writerow(line + [""])



if __name__ == "__main__":
    main()