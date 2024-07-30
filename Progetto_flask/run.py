# from app import create_app 
# import os 
# config_name = os.getenv('FLASK_CONFIG') or 'default' 
# app = create_app()
# if __name__ == '__main__': 
#     app.run()

from app import app

if __name__ == '__main__':
  app.run()