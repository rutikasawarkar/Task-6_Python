class Developer:

    def code(self):
        print('Writing code')

class BackendDeveloper(Developer):

    def backend_code(self):
        print('Writing backend code')

class SeniorBackendDeveloper(BackendDeveloper):

    def lead_project(self):
        print('Leading a backend project')


dev = SeniorBackendDeveloper()
dev.code()
dev.backend_code()
dev.lead_project()