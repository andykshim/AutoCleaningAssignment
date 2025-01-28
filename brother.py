class brother:
    def __init__(self, first, last, livesIn, dishes, num):
        self.first = first
        self.last = last
        self.livesIn = bool(livesIn == "True" or livesIn == "TRUE")
        self.dishes = bool(dishes == "True" or dishes == "TRUE")
        self.num = int(num)

    def __str__(self):
        return(self.first + " " + self.last + " has done " + str(self.num) + " cleanings.")
