class Car:

    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:

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
        income_from_cars = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income_from_cars += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income_from_cars,1)

    def calculate_washing_price(self, car: Car) -> float:
        return ((car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating)
                / self.distance_from_city_center)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        if 1 <= rating <= 5:
            self.count_of_ratings += 1
            self.average_rating = round(
                (((self.average_rating * (self.count_of_ratings - 1)) + rating)
                 / self.count_of_ratings),
                1
            )

bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

ws = CarWashStation(6, 8, 3.9, 11)

income: float = ws.serve_cars([
    bmw,
    audi,
    mercedes
])

print(
    income,
    income == 41.6,
    41.7,
    bmw.clean_mark == 8,
    audi.clean_mark == 9,
    mercedes.clean_mark == 8,
)
# audi wasn't washed
# all other cars are washed to '8'

ford = Car(2, 1, 'Ford')
wash_cost = ws.calculate_washing_price(ford)
# only calculating cost, not washing
print(
    wash_cost == 9.1,
    ford.clean_mark == 1,
)
#
ws.average_rating = 2.2
ws.count_of_ratings = 2
#
ws.rate_service(5)

print(
    ws.count_of_ratings == 3,
    ws.average_rating,
    ws.average_rating == 3.1,
    3.1
)
