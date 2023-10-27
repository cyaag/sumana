# Project Sumana IoT Device Activate & Deactivate

This project consists of three modules designed to interact with Google Cloud Storage and manage flat files. Below, you'll find an overview of each module, and instructions on running modules 1 and 2 on an edge gateway.

Before configuring the modules, you should setup the Google Cloud Project with the Google Cloud resources for your project, including creating a project, a storage bucket, a service account, and setting IAM (Identity and Access Management) policies for the service account to write and read files in Google Cloud Storage:

## Google Cloud Services & Account Configration

To interact with Google Cloud Storage, you'll need to set up credentials for your Google Cloud project:

1) Create a Google Cloud project if you haven't already.

    ** Go to the Google Cloud Console.

    ** Click the project selector at the top of the page, and then click "New Project."

    ** Enter a name for your project, and choose an organization if applicable. You can also            edit the project ID, which is a unique identifier for your project.

    ** Click "Create" to create the project.


2) Create a Google Cloud Storage bucket in your project to store the files.

    ** In the Google Cloud Console, make sure you have selected your project from the project          selector.

    ** In the left navigation pane, go to "Storage" > "Browser."

    ** Click the "Create Bucket" button.

    ** Enter a globally unique name for your bucket, choose a default storage class, and               configure other bucket settings as needed.

    ** Click "Create" to create the bucket.
   
4) Create a service account in your project that will be used to authenticate with Google Cloud Storage.

   ** In the Google Cloud Console, navigate to "IAM & Admin" > "Service Accounts."

   ** Click the "Create Service Account" button.

   ** Enter a name and description for the service account, and then click "Create."

   ** Choose the role for the service account, depending on your requirements. For reading and       writing files in Google Cloud Storage, you can assign roles like "Storage Object Admin"         (for read/write access) or "Storage Object Viewer" (for read-only access).

   ** Click "Continue" to grant additional permissions if needed.

   ** Choose the option to create a key for the service account and select the key type (JSON         is commonly used).

   ** Click "Create" to create the service account and download the key file to your local            machine. 

6) Set IAM policies for the service account to allow it to read and write files in the storage bucket.

   ** To allow the service account to read and write files in your Google Cloud Storage bucket,       you need to set up IAM policies:

   ** In the Google Cloud Console, go to "IAM & Admin" > "IAM."

   ** Find the member (service account) for which you want to set permissions. It will be             listed in the format <service-account-name>@<project-id>.iam.gserviceaccount.com.

   ** Click the member to open the permissions page.

   ** Click the "Edit" button to add or edit roles.

   ** To allow read and write access, add the following roles to the service account:
      For read access, you can use the role "Storage Object Viewer."
      For write access, you can use the role "Storage Object Admin."

   ** Click "Save" to apply the IAM policies.

## Edge Gateway Modules

### 1) Activate Module

The "Activate Module" is responsible for checking a specific local repository of an edge gateway and uploading flat files to a Google Cloud Storage (GCS) bucket. This module is configured to run as a batch job in the Linux crontab and is scheduled to execute once daily.

```python
# Code for Activate Module
[Activate](sumana-activate/main.py)

### 2) Deactivate Module

The "Deactivate Module" checks a GCS bucket for any flat files and downloads them to a specific path on the edge gateway. This module is configured to run as a batch job in the Linux crontab and is scheduled to execute once daily.

```python
# Code for Activate Module
[Deactivate](sumana-deactivate/main.py)

### 2) UI Module

The "UI Module" provides a basic user interface to manage, upload, download, and view the files stored in the Google Cloud Storage bucket.

## Running Module 1 & 2 on an Edge Gateway

To run Module 1 and 2 on an edge gateway, follow these steps:

### Step 1: Prerequisites

* Ensure you have Python and pip installed on your edge gateway.

Before you can run Module 1 and 2 on your edge gateway, ensure that Python and pip are installed. If they are not already installed, you can follow the instructions below to install them:

#### Install Python

If Python is not already installed, you can download the latest version of Python for your platform from the [Python official website](https://www.python.org/downloads/).

- For Linux (e.g., Ubuntu):
  ```bash
  sudo apt-get update
  sudo apt-get install python3

#### Install pip

  ```bash
  python -m ensurepip --default-pip

### Step 2: Install Dependencies

  ```bash
  pip install google-cloud-storage

### Step 3: Set Up Google Cloud Credentials

  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/gcpkey.json"

### Step 4: Configure Crontab

Edit your crontab file to schedule Module 1 (Activate Module) to run daily at 11 PM & Module 2 (Deactivate Module) to run daily at 12 PM. Open the crontab configuration using the following command:

  ```bash
  crontab -e
  0 23 * * * /usr/bin/python3 /path/to/sumana-activate/main.py >> /var/log/activate_module.log 2>&1
  0 23 * * * /usr/bin/python3 /path/to/sumana-deactivate/main.py >> /var/log/activate_module.log 2>&1

* Replace /path/to/activate_module.py with the actual path to your Activate Module script.
* The >> /var/log/activate_module.log 2>&1 part redirects the output to a log file.
