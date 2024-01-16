class Stadium:
    def __init__(self, stad_name, open_date, country, city, seat_cap):
        self.stad_name = stad_name
        self.open_date = open_date
        self.country = country
        self.city = city
        self.seat_cap = seat_cap



Wembley = Stadium(f"Wembley", "1.1.2000", "UK", "London", 100000)
Nepelu = Stadium(f"stadion nepelu", "1.1.2001", "Slovakia", "Bratislava", 5000)
Dzurillu = Stadium(f"Dzurillu", "1.1.2005", "Slovakia", "Bratislava", 6000)
Panaboha = Stadium(f"Panaboha", "1.1.1990", "Slovakia", "Bratislava", 500000)


stadiony = [Wembley, Nepelu, Dzurillu, Panaboha]

for i in stadiony:
    print(i.seat_cap)


biggest_cap = 0
biggest_stad = None
for i in stadiony:
    if i.seat_cap > biggest_cap:
        biggest_cap = i.seat_cap
        biggest_stad = i

print(f"najvacsi je: {biggest_stad.stad_name}")


class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.__price = price


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError ("Price is negative")

kniha = Book("Harry Potter", 400, 10)
print(kniha.price)
kniha.price = 20
print(kniha.price)
kniha.price = -10

