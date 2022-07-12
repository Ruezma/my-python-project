import math, re
from sympy import Matrix, lcm
from tabulate import tabulate

number = 1
data = [[] for _ in range(number)]
elementList = []
elementMatrix = []
output_titration = [["Base Volume",
                     "Hydrogen Power (pH)",
                     "Acid Mole",
                     "Base Mole",
                     "Salt Mole",
                     "Total Volume"]]

print("Chemical Reaction e.g. H2O+Ag3(Fe3O)4")
reactants = input("Input the reactants: ")
products = input("Input the products: ")
reactants = reactants.replace(' ', '').split("+")
products = products.replace(' ', '').split("+")


def add_to_matrix(element, index, count, side):
    if index == len(elementMatrix):
        elementMatrix.append([])
        for o in elementList:
            elementMatrix[index].append(0)
    if element not in elementList:
        elementList.append(element)
        for sum in range(len(elementMatrix)):
            elementMatrix[sum].append(0)
    column = elementList.index(element)
    elementMatrix[index][column] += count * side


def find_elements(segment, index, multiplier, side):
    elements_and_numbers = re.split('([A-Z][a-z]?)', segment)
    i = 0
    while i < len(elements_and_numbers) - 1:  # last element always blank
        i += 1
        if len(elements_and_numbers[i]) > 0:
            if elements_and_numbers[i + 1].isdigit():
                count = int(elements_and_numbers[i + 1]) * multiplier
                add_to_matrix(elements_and_numbers[i], index, count, side)
                i += 1
            else:
                add_to_matrix(elements_and_numbers[i], index, multiplier, side)


def compound_decipher(compound, index, side):
    segments = re.split('(\([A-Za-z0-9]*\)[0-9]*)', compound)
    for segment in segments:
        if segment.startswith("("):
            segment = re.split('\)([0-9]*)', segment)
            multiplier = int(segment[1])
            segment = segment[0][1:]
        else:
            multiplier = 1
        find_elements(segment, index, multiplier, side)


for i in range(len(reactants)):
    compound_decipher(reactants[i], i, 1)
for i in range(len(products)):
    compound_decipher(products[i], i + len(reactants), -1)

elementMatrix = Matrix(elementMatrix)
elementMatrix = elementMatrix.transpose()
solution = elementMatrix.nullspace()[0]

multiple = lcm([val.q for val in solution])
solution = multiple * solution

coefficient = solution.tolist()
output = ""
for i in range(len(reactants)):
    output += str(coefficient[i][0]) + reactants[i]
    if i < len(reactants) - 1:
        output += " + "
output += " → "
for i in range(len(products)):
    output += str(coefficient[i + len(reactants)][0]) + products[i]
    if i < len(products) - 1:
        output += " + "
print("="*50)
print(output)
print(elementMatrix)
print("="*50)

answer = int(input("""Main Menu:
    1. Strong Acid with Strong Base
    2. Weak Acid with Strong Base
    3. Weak Base with Strong Acid
    Your decision: """))


def data_appending(base_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume):
    data[indexing].append(base_volume_0)
    data[indexing].append(hydrogen_concentration)
    data[indexing].append(acid_mole)
    data[indexing].append(base_mole)
    data[indexing].append(salt_mole)
    data[indexing].append(total_volume)
    return output_titration.append(data[indexing])


if answer == 1:
    acid_volume, acid_molar, a = map(float, input("Strong acid: volume,molar,acid valence : ").split(","))
    base_volume, base_molar, b = map(float, input("Strong base: volume,molar,base valence : ").split(","))
    data = [[] for _ in range(number)]
    indexing = 0
    base_volume_0 = 0
    while base_volume_0 <= base_volume:
        salt_mole = 0
        data = [[] for _ in range(number)]
        acid_mole = acid_molar * acid_volume
        base_mole = base_molar * base_volume_0
        total_volume = acid_volume + base_volume_0
        if (acid_mole / coefficient[0][0]) > (base_mole / coefficient[1][0]):
            acid_mole -= (base_mole / coefficient[1][0] * coefficient[0][0])
            salt_mole += (base_mole / coefficient[1][0] * coefficient[2][0])
            base_mole -= base_mole
            concentration_H = a * acid_mole / total_volume
            hydrogen_concentration = -1 * math.log(concentration_H, 10)
            data_appending(base_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        elif (acid_mole / coefficient[0][0]) == (base_mole / coefficient[1][0]):
            acid_mole -= (base_mole / coefficient[1][0] * coefficient[0][0])
            salt_mole += (base_mole / coefficient[1][0] * coefficient[2][0])
            base_mole -= base_mole
            hydrogen_concentration = 7
            data_appending(base_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        else:
            salt_mole += (acid_mole / coefficient[0][0] * coefficient[2][0])
            base_mole -= (acid_mole / coefficient[0][0] * coefficient[1][0])
            acid_mole -= acid_mole
            concentration_OH = b * base_mole / total_volume
            hydroxide_concentration = -1 * math.log(concentration_OH, 10)
            hydrogen_concentration = 14 - hydroxide_concentration
            data_appending(base_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        base_volume_0 += 5

elif answer == 2:
    acid_volume, acid_molar = map(float, input("Weak acid: volume,molar : ").split(","))
    base_volume, base_molar, b = map(float, input("Strong base: volume,molar,base valence : ").split(","))
    data = [[] for _ in range(number)]
    indexing = 0
    base_volume_0 = 0
    ka = (10 ** -5)
    kb = (10 ** -5)
    while base_volume_0 <= base_volume:
        salt_mole = 0
        data = [[] for _ in range(number)]
        acid_mole = acid_molar * acid_volume
        base_mole = base_molar * base_volume_0
        total_volume = acid_volume + base_volume_0
        if base_mole == 0:
            concentration_H = math.sqrt(ka * acid_molar)
            hydrogen_concentration = -1 * math.log(concentration_H, 10)
            data_appending(base_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        elif (acid_mole / coefficient[0][0]) > (base_mole / coefficient[1][0]) and base_volume_0 > 0:
            acid_mole -= (base_mole / coefficient[1][0] * coefficient[0][0])
            salt_mole += (base_mole / coefficient[1][0] * coefficient[2][0])
            base_mole -= base_mole
            concentration_H = ka * acid_mole / salt_mole
            hydrogen_concentration = -1 * math.log(concentration_H, 10)
            data_appending(base_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        elif (acid_mole / coefficient[0][0]) == (base_mole / coefficient[1][0]):
            acid_mole -= (base_mole / coefficient[1][0] * coefficient[0][0])
            salt_mole += (base_mole / coefficient[1][0] * coefficient[2][0])
            base_mole -= base_mole
            concentration_OH = math.sqrt(10**-14 / ka * salt_mole / total_volume)
            hydroxide_concentration = -1 * math.log(concentration_OH, 10)
            hydrogen_concentration = 14 - hydroxide_concentration
            data_appending(base_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        elif (acid_mole / coefficient[0][0]) < (base_mole / coefficient[1][0]) and base_volume_0 < base_volume:
            salt_mole += (acid_mole / coefficient[0][0] * coefficient[2][0])
            base_mole -= (acid_mole / coefficient[0][0] * coefficient[1][0])
            acid_mole -= acid_mole
            concentration_OH = b * base_mole / total_volume
            hydroxide_concentration = -1 * math.log(concentration_OH, 10)
            hydrogen_concentration = 14 - hydroxide_concentration
            data_appending(base_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        else:
            salt_mole += (acid_mole / coefficient[0][0] * coefficient[2][0])
            base_mole -= (acid_mole / coefficient[0][0] * coefficient[1][0])
            acid_mole -= acid_mole
            concentration_OH = b * base_mole / total_volume
            hydroxide_concentration = -1 * math.log(concentration_OH, 10)
            hydrogen_concentration = 14 - hydroxide_concentration
            data_appending(base_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        base_volume_0 += 5

elif answer == 3:
    acid_volume, acid_molar, a = map(float, input("Strong acid: volume,molar,acid valence : ").split(","))
    base_volume, base_molar = map(float, input("Weak base: volume,molar : ").split(","))
    data = [[] for _ in range(number)]
    indexing = 0
    acid_volume_0 = 0
    ka = (10 ** -5)
    kb = (10 ** -5)
    while acid_volume_0 <= acid_volume:
        salt_mole = 0
        data = [[] for _ in range(number)]
        acid_mole = acid_molar * acid_volume_0
        base_mole = base_molar * base_volume
        total_volume = acid_volume_0 + base_volume
        if acid_mole == 0:
            concentration_OH = math.sqrt(kb * base_molar)
            hydroxide_concentration = -1 * math.log(concentration_OH, 10)
            hydrogen_concentration = 14 - hydroxide_concentration
            data_appending(acid_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        elif (acid_mole / coefficient[0][0]) < (base_mole / coefficient[1][0]) and acid_volume_0 > 0:
            salt_mole += (acid_mole / coefficient[0][0] * coefficient[2][0])
            base_mole -= (acid_mole / coefficient[0][0] * coefficient[1][0])
            acid_mole -= acid_mole
            concentration_OH = kb * base_mole / salt_mole
            hydroxide_concentration = -1 * math.log(concentration_OH, 10)
            hydrogen_concentration = 14 - hydroxide_concentration
            data_appending(acid_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        elif (acid_mole / coefficient[0][0]) == (base_mole / coefficient[1][0]):
            salt_mole += (acid_mole / coefficient[0][0] * coefficient[2][0])
            base_mole -= (acid_mole / coefficient[0][0] * coefficient[1][0])
            acid_mole -= acid_mole
            concentration_H = math.sqrt(10**-14 / kb * salt_mole / total_volume)
            hydrogen_concentration = -1 * math.log(concentration_H, 10)
            data_appending(acid_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        elif (acid_mole / coefficient[0][0]) > (base_mole / coefficient[1][0]) and acid_volume_0 < acid_volume:
            acid_mole -= (base_mole / coefficient[1][0] * coefficient[0][0])
            salt_mole += (base_mole / coefficient[1][0] * coefficient[2][0])
            base_mole -= base_mole
            concentration_H = a * acid_mole / total_volume
            hydrogen_concentration = -1 * math.log(concentration_H, 10)
            data_appending(acid_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        else:
            acid_mole -= (base_mole / coefficient[1][0] * coefficient[0][0])
            salt_mole += (base_mole / coefficient[1][0] * coefficient[2][0])
            base_mole -= base_mole
            concentration_H = a * acid_mole / total_volume
            hydrogen_concentration = -1 * math.log(concentration_H, 10)
            data_appending(acid_volume_0, hydrogen_concentration, acid_mole, base_mole, salt_mole, total_volume)
        acid_volume_0 += 5

print(tabulate(output_titration, tablefmt="fancy_grid"))
