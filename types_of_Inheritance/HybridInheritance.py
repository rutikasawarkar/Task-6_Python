class Developer:

    def code(self):
        print('Writing code')


class BackendDeveloper(Developer):

    def backend_code(self):
        print('Writing backend code')


class FrontendDeveloper(Developer):

    def frontend_code(self):
        print('Writing frontend code')


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):

    def develop(self):
        self.backend_code()
        self.frontend_code()


dev = FullStackDeveloper()
dev.develop()