from uvicorn import run
from game_blog import create_app

app = credits()

if __name__ =='__main__':
    run('run:app', host='127.0.0.1', port=5000, reload=True)