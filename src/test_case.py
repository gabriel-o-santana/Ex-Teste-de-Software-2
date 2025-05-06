class TestCase:
    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self):
        self.set_up()
        method = getattr(self, self.test_method_name)
        method()
        self.tear_down()

    def set_up(self):
        pass

    def tear_down(self):
        pass
