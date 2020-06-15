from flask import Response
import json

scoped_response = {'status': 'Success',
                   'code': 200,
                   'message': "",
                   'data': None}


def prepare_response(**kwargs):
    return Response(response=json.dumps({'status': kwargs.get("status"),
                                         'message': kwargs.get("message"),
                                         'user': kwargs.get('user'),
                                         'data': kwargs.get('data')}),
                    status=kwargs.get("code"), mimetype='application/json')
