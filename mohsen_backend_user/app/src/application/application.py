from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv
from src.interface.index import resources_dict
from src.infrastructure.permissionService.permissionProducer import permission_Produceres
from swagger.swagger import generated_swagger
import os

load_dotenv('.env', verbose=True)
SERVER_URL = os.getenv('SERVER_URL')
SWAGGER_URL = '/api/docs'
API_URL = '/app/swagger.json'


def Application(app, api_user):
    # ======================== Initializing APP =======================
    @api_user.route(API_URL, methods=['GET'])
    def swagger_api_docs_yml():
        try:
            generated_swagger['servers'] = [{'url':f'http://{SERVER_URL}:5001/api'},{'url':f'http://{SERVER_URL}:5002/api'}]
            return generated_swagger
        except:
            pass

    swaggerui_bluprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL
    )
    
    api = Api(app, prefix='/api/')

    # ========================= Add Resources =========================
    print(resources_dict.keys())
    for routs in resources_dict.keys():
        for resource in resources_dict[routs]:
            api.add_resource(resource[0], routs + resource[1])
    
    # ======================= Register Bluprint =======================
    app.register_blueprint(api_user)
    app.register_blueprint(swaggerui_bluprint)
    
    @app.before_first_request
    def register_seedes():
        permission_produceres = permission_Produceres()
        permission_produceres.register_permission(generated_swagger['paths'])
        permission_produceres.flush_close()


    return app

