class Student:
    """Object representing a boarding school student"""

    def __init__(
        self, id: int, gender: str, postal_code: int, school_class: int, group: int, second_year: bool
    ) -> None:
        self.id = id
        self.gender = gender
        self.postal_code = postal_code
        self.school_class = school_class
        self.group = group
        self.second_year = second_year

    def __repr__(self) -> str:
        return "Id: {}, Gender: {}, Class: {}, Group: {}, SecondYear: {}".format(
            self.id, self.gender, self.school_class, self.group, self.second_year
        )
