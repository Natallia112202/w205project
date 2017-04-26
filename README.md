# w205project

Background: This prototype will ingest consumer complaints data on financial products from one source (cfpb) and media data from another source (GDELT). It will also ingest two pre-downloaded files on banks asset value and number of employee. It will then upload into postgres, clean, and transform (filter/merge). Finally it will output summary view of consumer complaints data aginst a bank asset value and number of employees, and it will output the complaints vs media analysis for the top 6 banks.

How to Run the Prototype: Please execute the below files in order.

Setup_staging_1.sh : Downloads the complaints database, media database into AMI 

Database_setup_2.py : Upload the two database into postgres (ccdata, mediadata)

Ccdatadanalysisnew_3.py : Clean complaints database company name and then break it down into 2016 and 2017 file

Mediaanalysis_4.py : Break the mediadata into 2016 and 2017 and create index

Media_complaints_analysis_5.py : create a union table between ccdata and mediadata on the most current months data. And then combined with previous months data  to create the complaints_media_analysis_combined table. 

Top_company_media_analysis_6.py : create the complaints vs media analysis table for each of the top 6 banks

run_create_asset_employee_table_sql_7.sh: runs the create_asset_employee_table.sql which uploads and then cleans the company name from assets_bank and num_emp_bank csv in postgres. It then creates a join table between each of these table with ccdata

run_extract_table_CSV_sql_8.sh: runs the extract_table_CSV.sql which extract the below tables from postgres into CSV output

Join_assets_banks_1
Join_num_emp_banks_1
Complaints_media_analysis_boa
Complaints_media_analysis_equifax
Complaints_media_analysis_experian
Complaints_media_analysis_jpm
Complaints_media_analysis_wellfargo
complaints_media_analysis_transunion
