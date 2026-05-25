def main():
    converter()

def converter():
    mass = input("Enter a mass (KG, integer): ")
    c = int(300000000) #speed of light, m/s
    c = c * c #bruh
    energy = int(mass) * c

    print(f"Energy is:{energy} joules")

    return(energy)

main()