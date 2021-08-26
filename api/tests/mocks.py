class MockResponse:
 
    def __init__(self):
        self.status_code = 200
 
    def json(self):
        return {
            "info": {
                "version": "3.2.6"
            }
        }


class MockPypiResponse:
 
    def __init__(self):
        self.name = "Django"
        self.version= "3.2.6"