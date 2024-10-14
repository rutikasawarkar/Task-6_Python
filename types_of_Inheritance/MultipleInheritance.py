class BackendDeveloper:

    def backend_code(self):
        print('Writing backend code')

class FrontendDeveloper:

    def frontend_code(self):
        print('Writing frontend code')

class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):

    def develop(self):
        self.backend_code()
        self.frontend_code()


dev = FullStackDeveloper()
dev.develop()