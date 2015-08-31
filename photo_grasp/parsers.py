import logging
import re
from photo_grasp.util import login

__author__ = 'Langley'

def parse_tuchong_photo(albumAddress):
    page = login(albumAddress)
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
        logging.debug(page)
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
