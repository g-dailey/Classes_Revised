############
# Part 1   #
############


import code


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        """Initialize a melon."""

        self.pairings = []



    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)



    def update_code(self, new_code):
        self.code = new_code
        """Replace the reporting code with the new_code."""

    def __repr__(self):
        return f'Melon code is {self.code}, date of first harvest is {self.first_harvest}'


def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True,"Musklemon" )
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType("cas", 2003, "orange", True, False, "Casaba")
    casaba.add_pairing("mint")
    casaba.add_pairing("strawberries")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren",  1996, "green", True, True, "Crenshaw")
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw",  2013, "yellow", True, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)


    return all_melon_types

melon_types = make_melon_types()
def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    #print(melon_types)
    for melon in melon_types:
        print(f'{melon.name} pairs well with:')
        print(','.join(melon.pairings))
        # print(f'- {strings}')

    # Fill in the rest

print_pairing_info(melon_types)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melons_by_code = {}

    for melon in melon_types:
        # if melon.code not in melons_by_code:
        melons_by_code[melon.code] = melon
    return melons_by_code

melons_by_code = make_melon_type_lookup(melon_types)
    # Fill in the rest

############
# Part 2   #
############


class Melon:
    """Initialize a melon."""
    """A melon in a melon harvest."""
    def __init__(
        self, melon_type, shape_rating, color_rating, harvested_from, harvested_by
    ):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by
        """Initialize a melon."""
    """A melon in a melon harvest."""

    def __repr__(self):
        return f'{self.melon_type} is harvested from {self.harvested_from}'

    #shape and color ratings >5 and if it did not come from field 3

    def is_sellable(self):
        if self.shape_rating >5 and self.color_rating >5 and self.harvested_from !=3:
            return True
        else:
            return False



    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    harvested_melons = []

    melons_by_code = make_melon_type_lookup(melon_types)

    melon_one = Melon(melons_by_code['yw'], 8, 7, 2, "Sheila")
    harvested_melons.append(melon_one)

    melon_two = Melon(melons_by_code['yw'], 3, 4, 2, "Sheila")
    harvested_melons.append(melon_two)

    melon_three = Melon(melons_by_code['yw'], 9, 8, 3, "Sheila")
    harvested_melons.append(melon_three)

    melon_four = Melon(melons_by_code['cas'], 10, 6, 35, "Sheila")
    harvested_melons.append(melon_four)

    melon_five = Melon(melons_by_code['cren'], 8, 9, 35, "Michael")
    harvested_melons.append(melon_five)

    melon_six = Melon(melons_by_code['cren'], 8, 2, 35, "Michael")
    harvested_melons.append(melon_six)

    melon_seven = Melon(melons_by_code['cren'], 2, 3, 4, "Michael")
    harvested_melons.append(melon_seven)

    melon_eight = Melon(melons_by_code['musk'], 6, 7, 4, "Michael")
    harvested_melons.append(melon_eight)

    melon_nine = Melon(melons_by_code['yw'], 7, 10, 3, "Sheila")
    harvested_melons.append(melon_nine)

    return harvested_melons

    # Fill in the rest

melons = make_melons(melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            print(f'Harvested by {melon.harvested_by} from Field {melon.harvested_from} (CAN BE SOLD)')
        else:
            print(f'Harvested by {melon.harvested_by} from Field {melon.harvested_from} (NOT SELLABLE)')
    # Fill in the rest

get_sellability_report(melons)