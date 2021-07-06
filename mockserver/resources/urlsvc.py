'''
Service class for URL shortner functionality.

'''

from flask_restful import Resource, reqparse
from models.urlmodel import UrlModel

import random
import string


class URLService(Resource):
    '''
    Return the actual URL from the shortest URL provided.
    '''
    def get(self, url_key):
        url_obj = UrlModel.find_by_key(url_key)
        if url_obj:
            location = "https://" + url_obj.url if "https://" not in url_obj.url else url_obj.url
            return {}, 301, {'location': location}
        return {"message": f"URL not found with key '{url_key}'"}, 404


'''
Generate a shorter URL from a long URL and map it in the database.
'''
class URLServiceGenerate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url',
                        type=str,
                        required=True,
                        help="URL is Mandatory"
                        )
    '''
    Accept the url in the post body as a JSON data.
    '''
    def post(self):
        payload = URLServiceGenerate.parser.parse_args()
        '''
        if UrlModel.find_by_key(payload['url_key']):
            return {"message": "Duplicate Key Found"}, 400
        '''

        ukey = URLServiceGenerate.generate_random_key()

        while(UrlModel.find_by_key(ukey)):
            ukey = URLServiceGenerate.generate_random_key()

        url_obj = UrlModel(ukey, payload['url'])
        url_obj.save_to_db()

        return {"shorten_url_key": url_obj.key}, 201

    '''
    Generate a random 8 character string, which will be mapped for an URL. 
    '''
    @classmethod
    def generate_random_key(cls):
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(8))
        return result_str