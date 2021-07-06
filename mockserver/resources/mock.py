from flask_restful import Resource
import time

'''
Mock Service to handle timeouts
'''
class MockServiceTimeout(Resource):
    '''
    Delay the response for the interval provided in the request as path param.
    '''
    def get(self, interval):
        time.sleep(interval)
        return {"message": f"Success response after {interval} seconds"}, 200


class MockServiceHttpStatus(Resource):
    '''
    Return the HTTP status code, provided in the request as path param.
    '''
    def get(self, status):
        return {"message": f"Generating a response with HTTP status {status}"}, status

