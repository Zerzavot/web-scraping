#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Zehra
# Created Date: 10/04/2022
# version ='1.0'
#----------------------------------------------------------------------------

# 1.
# Libs
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import os


#----------------------------------------------------------------------------

def connect_driver(url,chromedriver):
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    
    return driver

def quit_driver(driver):
    driver.quit()
    
def print_clues(soup,titles,clues,clue_labels):

    categories = soup.find_all('div', class_='xwd__clue-list--wrapper')
    for category in categories:
        title = category.find('h3', class_='xwd__clue-list--title')
        parent_clues= category.find('ol', class_='xwd__clue-list--list xwd__clue-list--obscured')
        titles.append(title.text)
        if title is not None:
            print("==="+title.text+"===")
        for pc in parent_clues:
            clue_label = pc.find('span',"xwd__clue--label")
            clue       = pc.find('span',"xwd__clue--text xwd__clue-format")
            clue_labels.append(clue_label.text)
            clues.append(clue.text)
            print(str(clue_label.text)+". "+clue.text)

            
def create_dict(titles,clue_labels,clues):
    my_dict = {
            'Group': titles,
            'Number': clue_labels,
            'String': clues
        }
    return my_dict

def dict_to_json(my_dict,json_):
    with open(json_, "w") as outfile:
        json.dump(my_dict, outfile)

def main():
    my_url="https://www.nytimes.com/crosswords/game/mini"
    my_chromedriver="/usr/bin/chromedriver"

    titles = []
    clues=[]
    clue_labels=[]
    
    driver=connect_driver(my_url,my_chromedriver)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    
    print_clues(soup,titles,clues,clue_labels)
    
    dict1=create_dict(titles,clue_labels,clues)
    dict_to_json(dict1,"output.json")
    
    quit_driver(driver)

if __name__ == "__main__":
    main()
    