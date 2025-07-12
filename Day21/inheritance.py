class Animal:
    def __init__(self):
        print("Animal created")

class fish(Animal):
    def __init__(self):
        super().__init__()
        print("Fish created")

pirana = fish()

