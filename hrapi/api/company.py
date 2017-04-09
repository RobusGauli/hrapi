from sanic.response import json
from hrapi.api import api



@api.route('/company', methods=['GET'])
async def get_company(request):
    return json({'test':'working'})

