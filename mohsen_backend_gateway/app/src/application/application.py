from flask_restful import Api
from dotenv import load_dotenv
from src.interface.rest.modules.request.RequestRoute import RequestRoute
# from src.infrastructure.seeder.seeder import run_seeder
import os

load_dotenv('.env', verbose=True)
SERVER_URL = os.getenv('SERVER_URL')
SWAGGER_URL = '/api/docs'
API_URL = '/app/swagger.json'


def Application(app):
    # ======================== Initializing APP =======================
    RequestRoute(app)
    
    # @app.before_first_request
    # def register_seedes():
    #     run_seeder()
    
    return app

