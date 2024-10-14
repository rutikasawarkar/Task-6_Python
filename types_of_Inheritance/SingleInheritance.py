class Developer:

    def __init__(self,name):
        self.name = name

    def code(self):
        print(f'{self.name} is writing code')


class BackendDeveloper(Developer):

    def __init__(self,name,backend_skill):
        super().__init__(name)
        self.backend_skill = backend_skill

    def deploy(self):
        print(f'{self.name} is deploying a {self.backend_skill} application ')


dev = BackendDeveloper('Shree', 'Python')
dev.code()
dev.deploy()