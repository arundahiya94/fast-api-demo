from .models import ExampleModel

class SomeService:
    @staticmethod
    def get_example1():
        return ExampleModel.get_example1_data()

    @staticmethod
    def get_example2():
        return ExampleModel.get_example2_data()

    @staticmethod
    def get_example3():
        return ExampleModel.get_example3_data()
