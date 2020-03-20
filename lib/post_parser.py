import xml.etree.ElementTree as et
import urllib
from urllib import request

KEY_ATTR_MAP = {
    'Id': ('post_id', str),
    'TypeId': ('post_type_id', str),
    'ParentId': ('parent_id', str),
    'CreationDate': ('creation_date', str),
    'CommentCount': ('comment_count', int),
    'ViewCount': ('view_count', int),
    'AnswerCount': ('answer_count', int),
    'Score': ('score', int),
    'Title': ('title', str),
    'Body': ('body', str),
    'OwnerUserId': ('owner_user_id', str),
    'LastEditorUserId': ('last_editor_user_id', str),
    'LastEditDate': ('last_edit_date', str),
    'LastActivityDate': ('last_activity_date', str),
    'CommentCode': ('comment_code', str),
}


def get_xml_data_from_file(url):
    """
    Given an XML file, read the data and return the data as list of dict

    :param(str) url: URL of XML Data file
    :return(list of dict): XML Data
    """
    file = urllib.request.urlopen(url)
    data = file.read()
    file.close()
    root = et.fromstring(data)
    children = []
    for child in root:
        children.append(child.attrib)
    return children


def create_posts_from_xml(url):
    """
    Read XML file data and add each row as a post to database

    :param(str) url: Web URL of XML Data
    :return(int): No of Posts added to database
    """
    data = get_xml_data_from_file(url)
    count = 0
    from posts.models import Post
    for row in data:
        new_post = Post()
        for key, value in row.items():
            object_attr_type = KEY_ATTR_MAP.get(key)
            if not object_attr_type:
                continue        # XML key not of our interest
            attribute = object_attr_type[0]
            data_type = object_attr_type[1]
            # Type cast and assign value to mapped attribute of `post` object
            setattr(new_post, attribute, data_type(value))
        new_post.save()
        count += 1
    print("{} Posts added".format(count))
    return count
