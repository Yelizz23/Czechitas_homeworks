from math import ceil


class Locality:
    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient


class Property:
    def __init__(self, locality):
        self.locality = locality


class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        if self.estate_type == "land":
            coefficient = 0.85
        elif self.estate_type == "building site":
            coefficient = 9
        elif self.estate_type == "forest":
            coefficient = 0.35
        else:
            coefficient = 0

        tax = self.area * coefficient * self.locality.coefficient
        return ceil(tax)

    def __str__(self):
        return (f"Pozemek v lokalitě {self.locality.name} (koeficient {self.locality.coefficient}), "
                f"s plochou {self.area} metrů čtverečních. Daň celkem k zaplacení {self.calculate_tax()} Kč.")


class Residence(Property):
    def __init__(self, locality, area, commercial=False):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        tax = self.area * self.locality.coefficient * 15
        if self.commercial:
            tax *= 2
        return ceil(tax)

    def __str__(self):
        return (f"Prostory v lokalitě {self.locality.name} (koeficient {self.locality.coefficient}), "
                f"s podlahovou plochou {self.area} metrů čtverečních, ke komerčnímu využití: "
                f"{'ANO' if self.commercial else 'NE'}. Daň celkem k zaplacení {self.calculate_tax()} Kč.")


if __name__ == "__main__":
    manetin = Locality("Manětín", 1.4)
    brno = Locality("Brno", 3.5)

    estate_1 = Estate(brno, "land", 900)
    estate_2 = Estate(manetin, "building site", 120)

    residence_1 = Residence(manetin, 120)
    residence_2 = Residence(brno, 90, True)

    print("-" * 120)
    print(estate_1)
    print("-" * 120)
    print(estate_2)
    print("-" * 120)
    print(residence_1)
    print("-" * 120)
    print(residence_2)
    print("-" * 120)
