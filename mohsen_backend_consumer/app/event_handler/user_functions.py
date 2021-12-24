import requests
url = 'http://mohsen-user:5000/api/permission/create-many'

def register_permission(value):
    requests.post(url=url, json=value)