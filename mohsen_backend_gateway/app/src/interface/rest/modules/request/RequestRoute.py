from src.application.v1.request.RequestUseCase import RequestUseCase
from src.infrastructure.database.v1.nosql.mongo.db import db 
from flask import  request

def routeResource(**query):
    body = request.get_json() if request.get_json() else {}

    url_rule = str(request.url_rule)
    url_rule = url_rule.replace('<string:','{')
    url_rule = url_rule.replace('>','}')

    return RequestUseCase().request(
    headers = request.headers,
    url_rule= url_rule,
    original_url=request.path,
    method  = request.method,
    body    = body,
    query   = query)

def RequestRoute(app):
    
    permission = db().permission()

    permissions = permission.get_all()
    for route in permissions:
        route['path'] = route['path'].replace('{','<string:')
        route['path'] = route['path'].replace('}','>')

        app.add_url_rule(
        route['path'],
        route['title'],
        methods=[route['method'].upper()])
        app.view_functions[route['title']] = routeResource       
