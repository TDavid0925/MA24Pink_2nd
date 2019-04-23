from flask import Blueprint, request, jsonify
from flask_restful import Resource
from modelController.relief_proController import Relief_proController
from modelController.lga_postController import Lga_postController


class relief_postcode(Resource):
    def get(self, postcode):
        reliefController = Relief_proController()
        lga_postController = Lga_postController()

        LGAs = lga_postController.getLgasByPosts([postcode])

        filtered_relief = reliefController.getReliefByLGA(LGAs)
        if (len(filtered_relief) < 3):
            postcodes = lga_postController.getPostsByLgas(LGAs)
            filtered_relief = reliefController.getReliefByPost(postcodes)
            if(len(filtered_relief) < 3):
                LGAs = lga_postController.getLgasByPosts(postcodes)
                filtered_relief = reliefController.getReliefByLGA(LGAs)
        
        return filtered_relief

class relief_LGA(Resource):
    def get(self, LGA):
        reliefController = Relief_proController()
        lga_postController = Lga_postController()

        filtered_relief = reliefController.getReliefByLGA([LGA])
        if(len(filtered_relief) < 3):
            postcodes = lga_postController.getPostsByLgas([LGA])
            filtered_relief = reliefController.getReliefByPost(postcodes)
            if(len(filtered_relief) < 3):
                LGAs = lga_postController.getLgasByPosts(postcodes)
                filtered_relief = reliefController.getReliefByLGA(LGAs)
        
        return filtered_relief