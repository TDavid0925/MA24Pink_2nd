from flask import Blueprint, request, jsonify
from flask_restful import Resource
from modelController.hospitalController import HospitalController
from modelController.lga_postController import Lga_postController

class hospital_location(Resource):
    def get(self, postcode):
        hospitalController = HospitalController()
        lga_postController = Lga_postController()

        LGAs = lga_postController.getLgasByPosts([postcode])

        filtered_hospital = hospitalController.getHospitalByLGA(LGAs)
        if (len(filtered_hospital) < 3):
            postcodes = lga_postController.getPostsByLgas(LGAs)
            filtered_hospital = hospitalController.getHospitalByPost(postcodes)
            if(len(filtered_hospital) < 3):
                LGAs = lga_postController.getLgasByPosts(postcodes)
                filtered_hospital = hospitalController.getHospitalByLGA(LGAs)

        return filtered_hospital

class hospital_LGA(Resource):
    def get(self, LGA):
        hospitalController = HospitalController()
        lga_postController = Lga_postController()

        filtered_hospital = hospitalController.getHospitalByLGA([LGA])
        if (len(filtered_hospital) < 3):
            postcodes = lga_postController.getPostsByLgas([LGA])
            filtered_hospital = hospitalController.getHospitalByPost(postcodes)
            if(len(filtered_hospital) < 3):
                LGAs = lga_postController.getLgasByPosts(postcodes)
                filtered_hospital = hospitalController.getHospitalByLGA(LGAs)
        
        return filtered_hospital

