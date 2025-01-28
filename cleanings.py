class cleanings:
    def __init__(self, name, day, canLiveOuts, isDishes):
        self.name = name
        self.day = day
        self.canLiveOuts = bool(canLiveOuts == "True" or canLiveOuts == "TRUE")
        self.isDishes = bool(isDishes == "True" or isDishes == "TRUE")

    def __repr__(self):
        return(self.name + " is completed on " + self.day)