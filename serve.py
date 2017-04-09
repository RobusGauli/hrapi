import os
import argparse
from hrapi.app_config import create_app
from sanic_cors import CORS
from asyncpg import create_pool

DB_CONFIG = {
    'host': 'localhost', 
    'user' : 'user',
    'password' : 'postgres',
    'port' : '5432',
    'database' : 'hr'
}

#create an app instance 

app = create_app()
CORS(app)

@app.listener('before_server_start')
async def register_db(app, loop):
    app.pool = await create_pool(**DB_CONFIG, loop=loop, max_size=300)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('--port', dest='port', type=int, default=4000)
    parser.add_argument('--workers', dest='workers', type=int, default=1)

    args = parser.parse_args()
    app.run(host=args.host, port=args.port, workers=args.workers, debug=True)

if __name__ == '__main__':
    main()


