class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:

        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True

        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True

        elif carType == 3:
            if self.small > 0:
                self.small -= 1
                return True

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna