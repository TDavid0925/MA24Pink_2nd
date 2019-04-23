from modelController.LGA_post import LGA_post

class Lga_postController():
    def getLgasByPosts(self, posts):
        LGAs = set()
        for ele in LGA_post:
            if ele["Postcode"] in posts:
                LGAs.add(ele["LGA region"])
        return LGAs

    def getPostsByLgas(self, lgas):
        posts = set()
        for ele in LGA_post:
            if ele["LGA region"] in lgas:
                posts.add(ele["Postcode"])
        return posts
    
    def getAllPosts(self):
        posts=set()
        for ele in LGA_post:
            posts.add(ele["Postcode"])
        return posts

    def getAllLgas(self):
        LGAs=set()
        for ele in LGA_post:
            LGAs.add(ele["LGA region"])
        return LGAs
    
    def checkPost(self, post):
        for ele in LGA_post:
            if ele["Postcode"] == post:
                return True
        return False

    def checkLGA(self, LGA):
        for ele in LGA_post:
            if ele["LGA region"] == LGA:
                return True
        return False
