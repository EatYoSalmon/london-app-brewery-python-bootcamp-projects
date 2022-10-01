class FlightData:

    def __init__(
        self, price,
        dept_city_name, dept_city_code, dept_airport,
        dest_city_name, dest_city_code, dest_airport,
        travel_date, return_date
    ):

        self.price = price

        self.dept_cname = dept_city_name
        self.dept_ccode = dept_city_code
        self.dept_airport = dept_airport

        self.dest_cname = dest_city_name
        self.dest_ccode = dest_city_code
        self.dest_airport = dest_airport

        self.travel_date = travel_date
        self.return_date = return_date

    def print_data(self):

        print(f"{self.dest_cname}: £{self.price}")
        print(f"Departure: {self.travel_date}")
        print(f"Return: {self.return_date}")
        print("---\n\n")
