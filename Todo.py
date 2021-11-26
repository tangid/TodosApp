



from os import stat


class Todo():
    def __init__(self, title, state=0,  description = "") -> None:
        self.title = title
        #State 0 = Todo, 1 = Done
        self.state = state
        self.description = description

    def print(self):
        print("The todo is", self.title)
        print("The state is currently", self.state)
        if self.description: 
            print(self.description)
