# dome9-permissions-check
This project creates a list of missing permissions of AWS, Azure and GCP in Dome9/ Check Point CSPM

To run this script, you need to define API Key and Secret in the CSPM First. 
After that, these API Credentials need to be placed as variables in the OS

Linux : 

export DOME9_USERNAME="YOUR-API-KEY"
export DOME9_PASSWORD="YOUR-API-SECRET"

Once done, you may run the script with this syntax:

python3 dome9_permissions_v1.py <aws> or <azure> or <gcp> 
  
All results will be written into an Excel table :
  
output_aws.xlsx
output_azure.xlsx
output_gcp.xlsx
  
