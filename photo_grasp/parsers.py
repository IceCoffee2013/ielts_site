import logging
import re
from bs4 import BeautifulSoup
from photo_grasp.util import login, is_tuchong

__author__ = 'Langley'

def parse_tuchong_photo(albumURL):
    page = login(albumURL)
    userID = get_tuchong_userID(page)
    # print userID
    if userID == None:
        logging.debug('userID == None') #
        return
    url = r'http://photos.tuchong.com/' + userID +'/f/(.+?).jpg'
    print url
    logging.debug('url:' + url)  #
    pattern = re.compile(url)
    if pattern.findall(page):
        list = pattern.findall(page)
        print list
        logging.debug(list)  # debug
        return generate_photo_address(userID, list)
    else:
        print 'find no photo address'
        logging.debug('find no photo address')  #
        return None

def get_tuchong_userID(page):
    pattern = re.compile(r'http://photos.tuchong.com/(.+?)/')
    if pattern.findall(page):
        list = pattern.findall(page)
        print list[0]
        logging.debug('userID:'+list[0]) #
        return list[0]
    else:
        print 'find no userID'
        logging.debug('find no userID')  #
        logging.debug(page)
        return None

def generate_photo_address(userID, pictureIDs):
    uri_list = list()
    if pictureIDs:
        for i in  pictureIDs:
            uri = r'http://photos.tuchong.com/' + userID + '/f/' + i + '.jpg'
            if uri not in uri_list:
                uri_list.append(uri)
                print uri
                logging.debug(uri)   #
    return uri_list

def parse_lofter_photo(albumURL):
    photo_urls = list()
    page = login(albumURL)
    soup = BeautifulSoup(page, "html.parser")
    # result = soup.find_all('a', class_='imgclasstag')
    result = soup.find_all('div', class_='pic')
    if result:
        for i in result:
            # print i
            div_soup = BeautifulSoup(i.prettify(), "html.parser")
            img = div_soup.find_all('img')
            for n in img:
                photo_url = n.get('src')
                photo_url = url_filter(photo_url)
                photo_urls.append(photo_url)
                print photo_url
    else:
        print 'parse_lofter_photo find none'
        logging.debug('parse_lofter_photo find none')
    return photo_urls

def url_filter(url):
    if '?' in url:
        pattern = re.compile(r'(.+?)\?')
        if pattern.findall(url):
            list = pattern.findall(url)
            # print list[0]
            return list[0]

def parse_url(url):
    if is_tuchong(url):
        return parse_tuchong_photo(url)
    else:
        return parse_lofter_photo(url)
