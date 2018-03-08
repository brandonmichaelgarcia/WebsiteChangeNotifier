#!/usr/bin/env python3

import tracked_url as turl
import email_message as msg
import gmail_api_tools as api_tools

import pickle
import os
import time
import datetime
import requests
from bs4 import BeautifulSoup
from pathlib import Path


######################################################################
def prompt_for_tracked_page():
    url = prompt_for_url()
    selected_div = prompt_for_selected_div()
    return turl(url, selected_div)

def prompt_for_url():
    return input("Please enter the desired url to track.")
    

def prompt_for_selected_div():
    return input("Please enter the name of a specific div you would like to track.\n If you don't know this, hit enter to continue.")
    

def get_current_page(tracked_page):
    try:
        r = requests.get(tracked_page.url)
        soup = BeautifulSoup(r.content,'html5lib')
        page_text = soup.get_text() if selected_div == "" else str(soup.findAll('div', {"class": tracked_page.selected_div}))
        print("Page found and selected text is downloaded.")
        return page_text
    except Exception:
        raise


def pickleResource(cache_path, resource):
    f = open(path, 'wb')
    pickle.dump(resource, f)
    f.close()
    

def check_for_changes_from_cached_copy(div_text, cached_page):
    changes_observed = (div_text[0:328] != cached_page[0:328]) or (div_text[371:] != cached_page[371:])
    return changes_observed
 
 
def update_cache_resources(CACHED_PAGE_PATH, current_text):
    cache_page(CACHED_PAGE_PATH, current_text)
    return current_text
 
 
def cache_page(path, text):
    with open(path, "w+") as cached_page:
        cached_page.write(text)

 
 
def main():
    CACHED_TRACKED_PAGE = "cached_tracked_page.pickle"
    CACHED_EMAIL_MESSAGE = "cached_email_message.pickle"
    CACHED_PAGE_PATH = "cached_page_content.txt"
    
    if not Path(CACHED_TRACKED_PAGE):
        tracked_page = prompt_for_tracked_page()
    else:
        with open(CACHED_TRACKED_PAGE,'rb') as f:
            tracked_page =  pickle.load(f) 
        print("There are some saved url configurations for " + tracked_page.url)
        if 'n' in (input("Would you like to continue following this same webpage? [y/n]")).lower()
            os.remove(CACHED_TRACKED_PAGE)
            tracked_page = prompt_for_tracked_page()
    
    try:
        archived_text = get_current_page(tracked_page)
    except Exception:
        print("Error with entered url, selected div name, or website availability.")
        print("Please check the entered url and div name then retry running this program.")
        print("Quitting.\n")
        quit()
        
    message = msg.prompt_for_email_message()
    
    pickleResource(CACHED_TRACKED_PAGE, tracked_page)
    pickleResource(CACHED_EMAIL_MESSAGE, message)
    
    while True:
        try:
            current_text = get_current_page(url, selected_div)
        except Exception:
            print(str(datetime.datetime.now()) + ":  Website seems to be unavailable at the moment.")
            time.sleep(300)
            continue
        
        if not Path(CACHED_PAGE_PATH).is_file():
            archived_text = update_cache_resources(CACHED_PAGE_PATH, current_text)
            print("No existing cache found. Page cached.\n")
        else:
            if check_for_changes_from_cached_copy(div_text, open(CACHED_PAGE_PATH, 'r').read())
                print(str(datetime.datetime.now()) + ":  A change was observed! Emailing user.")
                api_tools.notify_by_email(message.getSender(), message.getRecipient(), message.getSubject(), message.getBodyText())
                archived_text = update_cache_resources(CACHED_PAGE_PATH, current_text)
            else:
                print(str(datetime.datetime.now()) + ":  No change observed. Sleeping...")
            
        time.sleep(3600)

 
if __name__ == "__main__":

    main()
    
