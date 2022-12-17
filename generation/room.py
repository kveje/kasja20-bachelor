class Room:
    """Object representing a boarding school room"""

    def __init__(self, id: int, hall: int, beds: int, gender: str) -> None:
        self.id = id
        self.hall = hall
        self.beds = beds
        self.gender = gender

    def __repr__(self) -> str:
        return "Id: {}, Gender: {}, Beds: {}, Hall: {}".format(self.id, self.gender, self.beds, self.hall)
