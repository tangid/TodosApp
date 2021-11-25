



class Todo():
    def __init__(self, title, description = None) -> None:
        self.title = title
        self.state = 0
        self.description = description

    def print(self):
        print("The todo is", self.title)
        print("The state is currently", self.state)
        if self.description: 
            print(self.description)
