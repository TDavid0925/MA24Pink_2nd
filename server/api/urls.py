from api import api_resource
from flask_restful import Resource, Api
from api.hospital_api import hospital_location, hospital_LGA
from api.relief_pro_api import relief_postcode, relief_LGA
from api.lga_post_api import check_LGA_api, check_post_api

api = Api(api_resource)

api.add_resource(check_post_api, '/api/lga_post/check_post/<int:postcode>')
api.add_resource(check_LGA_api, '/api/lga_post/check_LGA/<string:LGA>')

api.add_resource(hospital_location, '/api/hospital/<int:postcode>')
api.add_resource(hospital_LGA, '/api/hospital_lga/<string:LGA>')

api.add_resource(relief_postcode, '/api/relief_pro/<int:postcode>')
api.add_resource(relief_LGA, '/api/relief_pro_lga/<string:LGA>')


