import csv
import requests


# Define a function to retrieve metadata for a given DOI
def get_metadata(doi):
    url = f"https://opencitations.net/index/api/v1/metadata/{doi}"
    headers = {"Authorization": "94762995-8420-4272-a366-8b7aad4c40f8"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        metadata = response.json()
        print("Metadata received:", metadata)  # Debugging line to inspect the structure
        return metadata
    else:
        print("Failed to retrieve metadata:", response.status_code)  # Debugging line for errors
        return None


# Assuming references is a string of DOIs separated by "; "
references = "10.1108/jd-12-2013-0166"  # Example, replace this with your actual references string
reference_list = references.split("; ")

# Specify the CSV file to write to
csv_file_path = "project_data.csv"

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Reference DOI', 'ORCID iDs', 'Cited DOIs'])  # Updated header for ORCID iDs

    # Process the references to get ORCID iDs and write to the CSV
    for reference_doi in reference_list:
        metadata = get_metadata(reference_doi)
        if metadata:
            # Check if 'author' field exists and is not empty
            if 'author' in metadata[0] and metadata[0]['author']:
                # Initialize an empty list to hold ORCID iDs
                orcid_ids = []
                # Split the author string on semicolon to get individual author entries
                authors_list = metadata[0]['author'].split(';')
                for author in authors_list:
                    # Trim leading and trailing spaces
                    author = author.strip()
                    # Extract the last 19 characters of each author entry, assuming it's the ORCID iD
                    if len(author) >= 19:
                        orcid_id = author[-19:]
                        orcid_ids.append(orcid_id)
                # Join ORCID iDs back with semicolon for CSV output
                orcid_str = '; '.join(orcid_ids)
            else:
                orcid_str = 'No ORCID iDs listed'
            # Extract cited DOIs, assuming they are semicolon-separated
            cited_dois = metadata[0]['citation'] if 'citation' in metadata[0] else 'No citations listed'
            writer.writerow([reference_doi, orcid_str, cited_dois])
        else:
            writer.writerow([reference_doi, 'Metadata not found', ''])


# Output the path to the CSV file for user to access
csv_file_path
