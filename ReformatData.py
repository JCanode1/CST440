import csv
from itertools import product

def process_data(input_file, output_file):
    with open(input_file, 'r') as csv_input, open(output_file, 'w', newline='') as csv_output:
        reader = csv.reader(csv_input)
        writer = csv.writer(csv_output)
        
        # Write headers to the output file
        writer.writerow(['DOI', 'Author', 'Reference'])
        
        # Skip header row
        next(reader)
        
        # Process each row in the input file
        for row in reader:
            doi = row[0]
            authors = row[1]
            references = row[3].split(';')
            
            # Remove Author ID column
            authors = [author.strip() for author in authors.strip("[]").split(",")]

            # Compute Cartesian product of authors and references
            for author, reference in product(authors, references):
                writer.writerow([doi, author.strip(), reference.strip()])



input_file = "test.csv" 
output_file = "output.csv"  
process_data(input_file, output_file)
