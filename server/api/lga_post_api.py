from flask import Blueprint, request, jsonify
from flask_restful import Resource
from modelController.lga_postController import Lga_postController

class get_all_LGAs(Resource):
    def get(self):
        lga_postController = Lga_postController()

        return [{"LGAs": lga_postController.getAllLgas()}]

class get_all_postcodes(Resource):
    def get(self):
        lga_postController = Lga_postController()

        return [{"postcodes": lga_postController.getAllPosts()}]

class check_LGA_api(Resource):
    def get(self, LGA):
        lga_postController = Lga_postController()

        if(lga_postController.checkLGA(LGA)):
            return [{"result": "exist"}]
        else:
            return [{"result": "doesn't exist"}]

class check_post_api(Resource):
    def get(self, postcode):
        lga_postController = Lga_postController()

        if(lga_postController.checkPost(postcode)):
            return [{"result": "exist"}]
        else:
            return [{"result": "doesn't exist"}]


