class TestScript:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def run_test(self):
        print(f"Running Test {1}")
        self.test_invalid_input()
        print()

        print(f"Running Test {2}")
        self.test_number_of_seats()
        print()

        print(f"Running Test {3}")
        self.test_house_full()

    def test_invalid_input(self):
        print("#####################################################")
        print("Running test: Check for invalid input" )
        for key, value in self.input.items():
            if value<=0:
                try:
                    assert(self.output[key] == "Invalid Reservation")
                    print("Test Passed for invalid input")
                except AssertionError:
                    print("Test Failed for invalid input")
                    print("Expected: Invalid Reservation")
                    print("Actual: ", self.output[key])
                    return
        print("Finished test: Check for invalid input")
        print("######################################################")

    def test_number_of_seats(self):
        print("#####################################################")
        print("Running test: Check for number of seats reserved" )
        for key, value in self.input.items():
            try:
                if self.output[key] != "House full" and self.output[key] != "Invalid Reservation":
                    assert(len(self.output[key]) == value)
                    print("Correct number of seats reserved")
            except AssertionError:
                print(key)
                print("Test Failed for number of seats reserved")
                print(f"Expected: {value}")
                print("Actual: ", len(self.output[key]))
                return
        print("Finished test: Check for number of seats reserved")
        print("######################################################")

    def test_house_full(self):
        print("#####################################################")
        print("Running test: Check for house full" )
        for key, value in self.input.items():
            try:
                if key == "R013":
                    assert(self.output[key] == "House full")
                    print("Test Passed for house full")
            except AssertionError:
                print("Test Failed for house full")
                print("Expected: House full")
                print("Actual: ", self.output[key])
                return
        print("Finished test: Check for house full")
        print("######################################################")