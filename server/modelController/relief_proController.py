from modelController.relief_pro import relief_provider

class Relief_proController():
    def getReliefByLGA(self, LGAs):
        filtered_relief = []
        for rel in relief_provider:
            if rel["LGA"].strip() in LGAs:
                filtered_relief.append(rel)
        return filtered_relief

    def getReliefByPost(self, postCodes):
        filtered_relief = []
        for rel in relief_provider:
            if rel["Postcode"] in postCodes:
                filtered_relief.append(rel)
        return filtered_relief