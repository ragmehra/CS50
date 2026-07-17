def main(): 
    mass = input("What is your mass in kilograms?")
    print(mass_to_energy(int(mass)))


def mass_to_energy(mass): 
    c = 3 * 10 ** 8
    energy = mass * c ** 2
    formatted_energy = f"{energy:.0f}"
    return formatted_energy

main()