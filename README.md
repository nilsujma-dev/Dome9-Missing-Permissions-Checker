## Check Point CloudGuard Compliance Reporting Script for Multiple Cloud Platforms

This GitHub repository contains a Python script that interacts with the Check Point CloudGuard API to generate reports on missing permissions for cloud accounts across different hyperscalers: AWS, Azure, and GCP. The script automates the process of querying the CloudGuard API and compiling detailed compliance reports.

### Script Features
1. **Hyperscaler Argument Check**: Validates the command-line argument to ensure it specifies one of the supported platforms: AWS, Azure, or GCP.
2. **Environment Variable Validation**: Checks for the presence of CloudGuard credentials (username and password) set as environment variables.
3. **Platform-Specific API Calls**: Depending on the provided platform, the script makes API calls to the corresponding CloudGuard endpoints to fetch missing permissions data.
4. **Data Processing and Report Generation**:
   - Analyzes the JSON response to calculate the maximum number of actions per ID.
   - Constructs a pandas DataFrame to structure the data effectively.
   - Retrieves additional information like the account name for each ID.
   - Saves the final report in an Excel file named `output_{platform}.xlsx`.

### Usage Scenario
This script is particularly valuable for cloud security engineers and compliance officers who use Check Point CloudGuard for managing cloud security across AWS, Azure, and GCP. It simplifies the task of generating compliance reports, identifying missing permissions, and ensuring that cloud accounts adhere to security best practices.

### Prerequisites
- Python environment with `requests` and `pandas` libraries installed.
- Check Point CloudGuard account with API access and the necessary permissions.

### Security and Best Practices
- Secure management of CloudGuard credentials using environment variables.
- Handle the output Excel files securely, as they contain sensitive information about cloud account permissions.

---

This readme summary provides a comprehensive overview of the script's functionality and its application in generating compliance reports for multiple cloud platforms using Check Point CloudGuard. It serves as a guide for CloudGuard users to efficiently use the script for enhancing cloud security and compliance reporting.
