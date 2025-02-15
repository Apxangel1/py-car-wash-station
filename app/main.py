class Car:

    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: int) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation():

    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                self.wash_single_car()
                income += round(self.calculate_washing_price())
        return income

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            (car.comfort_class
                * (self.clean_power - car.comfort_class)
                * self.average_rating
                / self.distance_from_city_center),
            1
        )

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        if 1 <= rating <= 5:
            self.average_rating = (
                ((self.average_rating * self.count_of_ratings) + rating)
                / self.count_of_ratings
            )
            self.count_of_ratings += 1
