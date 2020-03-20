## XML Parser API

##### Selection test for `"Ingesting the Canadian Common CV"`

**Description**

This is a simple Django project which allows ingestion of XML file from a given URL, extract data and store them in a structured RDBMS.
Furthermore it exposed APIs to view all of them, ordering, filtering and searching.

##### Postman collection for some sample APIs:

`https://documenter.getpostman.com/view/10782841/SzS7Q6U9?version=latest`

** The following map is used for fetching data from XML and storing in SQLite table **

```python
{
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

```
The `key` part of the above is the key of the XML, where as the `value` part is a tuple whose first value is the attribute of the `posts` table and second is the corresponding data type.


##### Run the application server:

0. Suggested to create a virtualenv
1. Install requirements `pip3 install -r requirements.txt`
2. Run migrations `python3 manage.py migrate`
3. Run python django server `python3 manage.py runserver`

Note:
* Using default settings, a Sqlite file will be create `db.sqlite3`
* This could be easily changed to another RDBMS like MqSQL or PGSQL
* The APIs can be served using gateways like WSGI, but for non-production `runserver` should be enough.