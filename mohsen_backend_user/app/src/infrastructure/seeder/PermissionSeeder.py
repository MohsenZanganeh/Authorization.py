import re
from src.infrastructure.database.v1.nosql.mongo.db import db
from src.infrastructure.seeder.RoleSeeder import create_role
def create_permissions(paths):
    permission_model = db().permission()
    routes =  _get_all_routes(paths)

    for route in routes:
        if permission_model.get_one({'title':route['title']}):
            permission_model.updateByQuery({'title':route['title']},route)    
        else:
            permission_model.insert(route)
    create_role()

def _get_all_routes(paths):
    routes = []
    for path in paths:
        new_path = path.replace('/','_')
        new_path = re.sub('_$',"",new_path)
        new_path = new_path[1:]
        url = f'/api{path}'
        group = re.findall("((^[A-Za-z]+|-[A-Za-z]+)*)",new_path)[0][0]
        for method in paths[path]:

            route = {}
            route['title'] = f'{new_path}_{method}'
            route['path'] = str(url)
            route['method'] = method
            route['group'] = group

            if paths[path][method].get('is_admin'):
                route['is_admin'] = paths[path][method].get('is_admin')
            else:
                print(f"This Route hasn't [ is_admin ]: {path}  method: {method}")

            if paths[path][method].get('is_generic'):
                route['is_generic'] = paths[path][method].get('is_generic')
            else:
                print(f"This Route hasn't [ is_generic ]: {path}  method: {method}")

            if paths[path][method].get('is_public'):
                route['is_public'] = paths[path][method].get('is_public')
            else:
                print(f"This Route hasn't [ is_public ]: {path}  method: {method}")
            routes.append(route)
        print("\n //----next route----\\")

    return routes