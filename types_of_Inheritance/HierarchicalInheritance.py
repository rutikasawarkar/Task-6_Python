class Developer:

    def code(self):
        print('Writing code')

class BackendDeveloper(Developer):

    def backend_code(self):
        print('Writing backend code')

class FrontendDeveloper(Developer):

    def frontend_code(self):
        print('Writng frontend code')


backend_dev = BackendDeveloper()
backend_dev.code()
backend_dev.backend_code()


frontend_dev = FrontendDeveloper()
frontend_dev.code()
frontend_dev.frontend_code()
