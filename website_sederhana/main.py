from aiohttp import web
import json, aiohttp, os, sys, re

index_path = os.path.dirname(os.path.abspath(sys.argv[0]))

def update_variable_value(input_string, variable_name, new_value):
    pattern = re.compile(rf'({variable_name} = )\d+')
    replacement = f'\g<1>{new_value}'
    result = re.sub(pattern, replacement, input_string)
    return result

app = web.Application()
routes = web.RouteTableDef()

keys = ['air_speed', 'motor_rpm', 'vert_speed']
variables = ['airSpeedCurVal', 'motorRpmCurVal', 'vertSpeedCurVal']

@routes.get('/')
async def index_async(request):
    data = {}
    with open(os.path.join(index_path, 'data.json'), 'r') as fp:
        data = json.load(fp)

    with open(os.path.join(index_path, 'index.html')) as fp:
        content = fp.read()
        for var, key in zip(variables, keys):
            content = update_variable_value(content, var, data[key])
        # print(content)
        return web.Response(text=content, content_type='text/html')

@routes.get('/update')
async def update_async(request):
    data = {}
    with open(os.path.join(index_path, 'data.json'), 'r') as fp:
        data = json.load(fp)
    
    for key in keys:
        if request.query.get(key):
            data[key] = request.query.get(key)

    print(data)

    with open(os.path.join(index_path, 'data.json'), 'w') as fp:
        json.dump(data, fp)

    return web.Response()

app.add_routes(routes)

aiohttp.web.run_app(app, port=8000)