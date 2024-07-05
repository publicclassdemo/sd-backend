from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

app = Sanic("my-hello-world-app")
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.get('/api/login')
async def login(request):
    return json({'hello': 'login'})


if __name__ == '__main__':
    app.run(host="localhost", port=5137, debug=True, auto_reload=True)