from modelController.hospital import hospital

class HospitalController():
    def getHospitalByLGA(self, LGAs):
        filtered_hospital = []
        for hos in hospital:
            if hos["LGA"] in LGAs:
                filtered_hospital.append(hos)
        return filtered_hospital
    
    def getHospitalByPost(self, postCodes):
        filtered_hospital = []
        for hos in hospital:
            if hos["Postcode"] in postCodes:
                filtered_hospital.append(hos)
        return filtered_hospital