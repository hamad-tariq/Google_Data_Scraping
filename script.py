import pandas as pd
import openpyxl

# Load the Google Sheets file using openpyxl
google_sheets_file = 'practice_data.xlsx'
workbook = openpyxl.load_workbook(google_sheets_file)
sheet = workbook.active

# Initialize lists to store job titles and company names
job_titles = []
company_names = []

# Iterate through rows to extract data
for row in sheet.iter_rows(min_row=2, values_only=True):
    name, job_title, company_name, _ = row
    job_titles.append(job_title)
    company_names.append(company_name)

# Create a DataFrame to work with the extracted data
data = {'Job Title': job_titles, 'Company Name': company_names}
df = pd.DataFrame(data)
display_data: dict={}
display_data=df

# Display the extracted data
print (display_data)
