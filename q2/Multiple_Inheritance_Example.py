class Father:
    eyes = "blue eyes"

class Mother:
    hair = "black hair"

class You(Father, Mother):
    def describeYourself(self):
        print(f"I have {self.eyes} and {self.hair}")

me = You()
me.describeYourself()
