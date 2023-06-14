# find-a-job

## Introduction
```find-a-job``` is a Python script designed to automate the bulk sending of Curriculum Vitae (CV) to companies via LinkedIn. 
This script aims to save time and effort by streamlining the process of reaching out to multiple companies for job applications.


## Installation
1. Clone the repository:

```
git clone https://github.com/Axlfc/find-a-job
```

2. Navigate to the project directory:

```
cd find-a-job
```

3. Install the required dependencies:

```
pip3 install -r requirements.txt
```


4. Set up the environment variables:
- Create a new file named `.env` in the project directory.
- Open the `.env` file in a text editor.
- Add the following environment variables:
  ```
  LINKEDIN_CLIENT_EMAIL=your_linkedin_email@example.com
  LINKEDIN_CLIENT_PASSWORD=your_linkedin_password
  ```
- Replace `your_linkedin_email@example.com` with your actual LinkedIn email address.
- Replace `your_linkedin_password` with your actual LinkedIn password.

## Usage
1. Ensure that you have set up the `.env` file correctly (as explained in the Installation section).

2. Run the script:
 
```
python3 reachout.py
```

3. The script will open a Firefox browser window and navigate to the LinkedIn login page.

4. Once logged in, the script will perform automated actions to send your CV to the companies. 

5. Sit back and let the script automate the bulk sending process for you!

## License
```find-a-job``` is licensed under the GNU General Public License (GPL) version 2.0. You can find the full text of the license in the [LICENSE](LICENSE) file.

## Disclaimer
The use of ```find-a-job``` to automate the sending of CVs to companies should comply with the terms and conditions of the targeted platforms (e.g., LinkedIn). 
Usage of this script is at your own risk. The developers are not responsible for any misuse or violations.