import bs4
import requests
import re
import pandas
import json  
from src.mail import send_mail
import logging


def get_side_info(response):
    '''
    This function will extract the infobox from wikipedia. 
        args:
            response: response of the wikipedia page for requested company
    '''
    side_info = {}
    urlpage =  response.url
    data = pandas.read_html(urlpage)[0]
    null = data.isnull()
    for x in range(len(data)):
        first = data.iloc[x][0]
        second = data.iloc[x][1] if not null.iloc[x][1] else ""
        side_info[first] = ''.join(second)
    empty_keys = [k for k,v in side_info.items() if not v]
    empty_keys_same = [k for k,v in side_info.items() if k==v]
    for k in empty_keys:
        del side_info[k]
    for key in empty_keys_same:
        del side_info[key]
    return side_info

def intro_info(response):
    '''
    This function will extract the introduction details from wikipedia. 
        args:
            response: response of the wikipedia page for requested company
    '''

    if response is not None:
        html = bs4.BeautifulSoup(response.text, 'html.parser')

        title = html.select("#firstHeading")[0].text
        paragraphs = html.select("p")
        for para in paragraphs:
            print (para.text)

        # just grab the text up to contents as stated in question
        intro = '\n'.join([ para.text for para in paragraphs[1:2]])
        return intro


 

if __name__ == "__main__":
    info = {}
    

    try:
        # extract all parameters from config file
        with open('config.json', 'r') as config:
            params = json.load(config)["params"]
        # params
        output_dir = params["output_folder"]
        company = params["company_name"]
        Mail_sender_id = params["Mail_sender_id"]
        Mail_sender_password = params["Mail_sender_password"]
        Mail_receiver_id = params["Mail_receiver_id"]
        output_type = params["output_type"]
        
    except Exception as e:
        print(f'Exception occurred while taking parameters from config file! {e}')
    response = requests.get(f"https://en.wikipedia.org/wiki/{company}")
    message = f'Please find the attached information on {company}.'

    info['intro'] = intro_info(response)

    info_box = get_side_info(response)
    for i in info_box:
        info[i] = info_box[i]

    # For JSON request
    if output_type=="JSON":
        # Serializing json    
        with open(output_dir + f"{company}.json", "w") as outfile:  
            json.dump(info, outfile) 
        
        file = output_dir + f"{company}.json"
    #for CSV request
    elif output_type=="CSV":
        df = pandas.DataFrame.from_dict(info, orient="index")
        df.to_csv(output_dir + f"{company}.csv")
        file = output_dir + f"{company}.csv"

    send_mail(Mail_sender_id, Mail_sender_password, Mail_receiver_id, message, company, file)