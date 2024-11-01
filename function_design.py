"""
Function design portion of discussion
"""

import matplotlib.pyplot as plt


def analyze_and_visualize_molecule(molecule):
    """
    Read in a molecule file and analyze it.
    """

    print(f"Analyzing molecule {molecule}")

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    file_name = f"molecules/{molecule}.xyz"

    with open(file_name) as f:
        data = f.readlines()

    total_weight = 0
    atoms = []
    colors = []
    for line in data[2:]:
        split_line = line.split()
        atom = split_line[0]

        # Get the colors and coordinates
        x, y, z = float(split_line[1]), float(split_line[2]), float(split_line[3])
        color = "pink"
        if atom == "H":
            color = "white"
        if atom == "O":
            color = "red"
        if atom == "N":
            color = "blue"
        if atom == "C":
            color = "gray"

        atoms.append([atom, [x, y, z]])
        colors.append(color)

    # Calculate the weight
    for i in range(len(atoms)):
        if atoms[i][0] == "H":
            weight = 1
        if atoms[i][0] == "O":
            weight = 16
        if atoms[i][0] == "N":
            weight = 14
        if atoms[i][0] == "C":
            weight = 12

        total_weight += weight

        x, y, z = atoms[i][1][0], atoms[i][1][1], atoms[i][1][2]
        ax.scatter(x, y, z, color=colors[i], s=weight * 100, edgecolor="black")


    print(f"The molecular weight is {total_weight}.")
    plt.savefig(f"{molecule}.png")


if __name__ == "__main__":
    import sys

    mol_analyze = sys.argv[1]

    analyze_and_visualize_molecule(mol_analyze)
