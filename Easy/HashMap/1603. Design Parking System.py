class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big 
        self.medium = medium 
        self.small = small 


    def addCar(self, carType):
        if carType == 1 :
            if self.big :
                self.big -= 1 
                return True 
            else : return False 
        elif carType == 2 :
            if self.medium :
               self.medium -= 1
               return True 
            else :
                return False 
        elif carType == 3 :
            if self.small :
                self.small -= 1
                return True 
            else :
                return False 
         
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)