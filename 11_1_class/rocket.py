class Rocket:

    def __init__(self, year, mileage):
        self.year = year
        self.mileage = mileage

    def print_fields(self):
        print(f'Год создания: {self.year}')
        print(f'Пробег: {self.mileage}')

    def avg_mileage(self):
        return self.mileage / (2019 - self.year)


class UFO(Rocket):

    def __init__(self, year, mileage, brand, company):
        self.year = year
        self.mileage = mileage
        self.brand = brand
        self.company = company

    def print_fields(self):
        print(f'Год создания: {self.year}')
        print(f'Пробег: {self.mileage}')
        print(f'Марка: {self.brand}')
        print(f'Владелец {self.company}')


if __name__ == "__main__":
    year, mileage = [int(i) for i in input().split()]
    r = Rocket(year, mileage)
    year, mileage, brand, company = input().split()
    u = UFO(int(year), int(mileage), brand, company)
    r.print_fields()
    print(r.avg_mileage())
    u.print_fields()
    print(u.avg_mileage())
