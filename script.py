import pandas as pd
import openpyxl
from googlesearch import search
import requests
import time
from bs4 import BeautifulSoup
import webbrowser

# Load the Excel file using pandas
excel_file = 'practice_data.xlsx'
df = pd.read_excel(excel_file)

# Initialize lists to store job titles, company names, LinkedIn URLs, and names
job_titles = []
company_names = []
linkedin_urls = []
names = []

# Iterate through rows to extract data
for index, row in df.iterrows():
    name = row['Name']
    job_title = row['Job Title']
    company_name = row['Company Name']
    linkedin_url = row['LinkedIn URL']

    # Construct search query
    search_query = f"{job_title} {company_name}"

    # Retry mechanism with timeout handling
    MAX_RETRIES = 3
    for _ in range(MAX_RETRIES):
        try:
            search_results = list(search(search_query, num_results=1))
            break  # Break out of the loop if the search succeeds
        except requests.exceptions.ReadTimeout:
            print("Timeout occurred, retrying...")
            time.sleep(5)  # Wait for a moment before retrying
    else:
        print("Max retries reached, search failed.")
        continue  # Move on to the next row

    # Process search results if available
    if search_results:
        first_result = search_results[0]
        
        # Print the search result URL (for demonstration purposes)
        print( first_result)

        # Update the lists with the extracted data
        job_titles.append(job_title)
        company_names.append(company_name)
        linkedin_urls.append(linkedin_url)
        names.append(name)

# Create a DataFrame to display the extracted data
extracted_data = {
    'Name': names,
    'Job Title': job_titles,
    'Company Name': company_names,
    'LinkedIn URL': linkedin_urls
}
extracted_df = pd.DataFrame(extracted_data)

# Display the extracted data
print(extracted_df)
