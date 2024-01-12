class Linear:
    def __init__(self, co_x, co_y, constant):
        self.co_x = co_x
        self.co_y = co_y
        self.constant = constant
    
    def __str__(self):

        return "{}x + {}y = {}".format(self.co_x, self.co_y, self.constant)
    
    def __add__(self,other):

        newx_co = self.co_x + other.co_x
        newy_co = self.co_y + other.co_y
        new_constant = self.constant + other.constant

        return "{}x + {}y = {}".format(newx_co, newy_co, new_constant)
    
    def __sub__(self, other):
        subx_co = self.co_x + other.co_x
        suby_co = self.co_y + other.co_y
        sub_constant = self.constant + other.constant

        return "{}x + {}y = {}".format(subx_co, suby_co, sub_constant)
    
    def __multiply__(self, n):
        multix_co = self.co_x*n
        multiy_co = self.co_y*n
        multi_constant = self.constant*n

        return "{}x + {}y = {}".format(multix_co, multiy_co, multi_constant)
    
    def __solve__(self,other):
        determinant = self.co_x*other.co_x - self.co_y*other.co_x

        if determinant == 0:
            if (self.constant*other.co_y -other.constant*self.co_y) == 0:
                return "Infinite solutions (dependent system)"
            else:
                return "No solution (inconsistent system)"
        
        else:
            x = (self.constant*other.co_y - other.constant*self.co_y)/determinant
            y = (self.co_x*other.constant - self.constant*other.co_x)/determinant

            print (f"x : {x}")
            print (f"y : {y}")



    
