import re
from tuchong.util import login

__author__ = 'Langley'

def parse_tuchong_photo(albumAddress):
    page = login(albumAddress)
    userID = get_tuchong_userID(page)
    if userID == None:
        return
    url = r'http://photos.tuchong.com/' + userID +'/f/(.+?).jpg'
    print url
    pattern = re.compile(url)
    if pattern.findall(page):
        list = pattern.findall(page)
        print list
        return generate_photo_address(userID, list)
    else:
        print 'find no photo address'
        return None

def get_tuchong_userID(page):
    pattern = re.compile(r'http://photos.tuchong.com/(.+?)/')
    if pattern.findall(page):
        list = pattern.findall(page)
        print list[0]
        return list[0]
    else:
        print 'find no photo address'
        return None

def generate_photo_address(userID, pictureIDs):
    uri_list = list()
    if pictureIDs:
        for i in  pictureIDs:
            uri = r'http://photos.tuchong.com/' + userID + '/f/' + i + '.jpg'
            if uri not in uri_list:
                uri_list.append(uri)
                print uri
    return uri_list
