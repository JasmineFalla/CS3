# anything private is inside the class
# anything public can be accessed outside the class

class Human:
    name = ""
    age = 15
    credit_card = "4539 7894 4561 2345"
    def eat():
        print("Nom nom nom")
    def sleep():
        print("Zzzzzzz")

hooman = Human()
hooman.name = "Sir JM"
hooman.age = 33
print(f"{hooman.name} is {hooman.age} years old")
print(f"CC number is {hooman.credit_card}")
