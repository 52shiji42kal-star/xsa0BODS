# class2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

p = Point(1, 2)
p.shift(3, 4)
print(p.x, p.y)

# class4
class Potion:
    def __init__(self, name, price, heal):
        self.name = name
        self.price = price
        self.heal = heal

    def describe(self):
        return f"{self.name}: {self.price} gold, +{self.heal} health"

pot = Potion("Healing Potion", 50, 20)
print(pot.describe())

# class6
class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, name, qty):
        self.items[name] = self.items.get(name, 0) + qty

    def total(self):
        return sum(self.items.values())

inv = Inventory()
inv.add("яблоко", 5)
inv.add("банан", 3)
inv.add("яблоко", 2)
print(inv.total())

# class7
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(5, -10)
print(p)

# class8
class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def to_dict(self):
        return {"name": self.name, "health": self.health, "damage": self.damage}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["health"], data["damage"])

hero1 = Hero("Воин", 100, 15)
data = hero1.to_dict()
hero2 = Hero.from_dict(data)
print(hero2.health)
