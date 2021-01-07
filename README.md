# Company-info-auto-mail-sender

# What for
This project is based on programmatic approach to extract information of requested company and share the information to the receiver email. It can be used as a sample backend.

## The key features are:
1) Extract comapany introduction
2) Information on company's founders, product, market value, official website etc.
3) User can send the informaion in both JSON and CSV format.


Project structure
------------

    .
    ├── app.py                      > Main file which contains all the functionality to run the app.
    ├── config.json                 > Enviornment file storing all required enviornment variables 
    ├── README.md                   > The top-level README for developers using this project.
    ├── requirements.txt            > All the requirements which is needed to run this project.
    ├── log                         > This folder will maintain the logs for each run.
        ├── clean_log_07_01_2021                
        
    ├── src
        ├── mail.py                > To share information file with another clint using their email.
        
    ├── output                     > This folder will contain all the output files, that are going to share to the receiver.
        ├──                      
        


--------
## Testing

  - This can run on Windows / Linux(Ubuntu 20.04) system.
  - It is advised to create a virtual enviornment if you have existing conflicts with python & other libraries/packages installtions.

## Quickstart

  - Make sure you have updated your OS to latest version.
  - Install all necessary dependencies for this project from requirements.txt
    - Run `pip install -r requirements.txt` for installing dependencies. 
  - Please change parameters accordingly in (config.json) config file as per your system configuration before running the app.py file.
      - please add the correct company name. like (Microsoft, Cisco, Apple_Inc)
  - Run app.py file in for turn on the app.
    - Run `python3 app.py`
  - Once the log file has updated a message with `Mail Sent`. Clint will receive the mail attached with the information file.
