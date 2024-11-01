class Molecule:
    def __init__(self):
        self.atoms = []

    def add_atom(self, atom_type, x, y, z):
        self.atoms.append({'type': atom_type, 'x': x, 'y': y, 'z': z})

    def get_atoms(self):
        return self.atoms

    def compute_molecular_weight(self):
        weight = 0
        for atom in self.atoms:
            if atom['type'] == "H":
                weight += 1
            elif atom['type'] == "O":
                weight += 16
            elif atom['type'] == "N":
                weight += 14
            elif atom['type'] == "C":
                weight += 12
        return weight

    def visualize(self):
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")

        for atom in self.atoms:
            x, y, z = atom['x'], atom['y'], atom['z']
            if atom['type'] == "H":
                color = "white"
            elif atom['type'] == "O":
                color = "red"
            elif atom['type'] == "N":
                color = "blue"
            elif atom['type'] == "C":
                color = "gray"
            ax.scatter(x, y, z, color=color)

        plt.show()
