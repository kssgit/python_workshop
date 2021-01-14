class Product:
    def __init__(self, p_id, p_name, price, description):
        self.p_id = p_id
        self.p_name = p_name
        self.price = price
        self.description = description

    def __eq__(self, p_id):
        if self.p_id == p_id:
            return True
        else:
            return False

    def __str__(self):
        return "p_id : {0} , p_name : {1} , price : {2} , description : {3}".format(self.p_id, self.p_name, self.price, self.description)
