
import getpass
import os
import os.path
from os import path
import urllib.request
from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
#pip install icrawler
#https://icrawler.readthedocs.io/en/latest/api.html#module-icrawler.downloader
#https://buildmedia.readthedocs.org/media/pdf/icrawler/latest/icrawler.pdf package manual?



def create_directory(file_directory): #if the directory doesnt exist you get one/ or it will create a folder to DL the images
    user_name = getpass.getuser() #gets username
    directory_name = 'Online_Images' #folder name
    try:
        file_directory = os.mkdir(f"C:/Users/{user_name}/Pictures/{directory_name}") #this program can be run anywhere so we secure a spot in the pictures folder with our own directory
        return file_directory
    except FileExistsError:
        print(f"Directory has already been created.")
        file_directory = f"C:/Users/{user_name}/Pictures/{directory_name}"
        return file_directory

def check_file(file_path):
    file_path = input("Please enter the file path: ") #program closes if the file path doesnt exist, extremely simple rather than setting up the program to never end
    if path.isfile(file_path) == True:
        print("File Path Exists")
        return file_path
    else:
        print("File path doesn't exist or non-file path given, the program will now close.")
        quit()

def download_image(file_directory, search_query): #webscraper function, google didn't work for me so we try the alternatives
    print(file_directory)

    bing_crawler = BingImageCrawler(parser_threads=2, downloader_threads=4,storage={'root_dir': file_directory})
    picture_count = 1

    for items in search_query:
        
        print(f"NEW IMAGE DOWNLOADING ITS AN IMAGE OF {items}")
        bing_crawler.crawl(keyword = items, filters = None, max_num = picture_count)
        picture_count += 1
        


if __name__ == "__main__":
    file_path = ''
    file_directory = ''
    search_query = [] #this list will hold every line from the file 
    file_directory = create_directory(file_directory)
    file_path = check_file(file_path)

    opened_file = open(file_path,'r') # open file
    file_string = opened_file.read()
    search_query = file_string.split("\n")
    print("File successfully opened.")
    print(f"List of items to be looked up: {search_query}")
    download_image(file_directory, search_query)


    opened_file.close()
    

