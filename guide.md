# Week 11 Discussion - Function and Class Design

This discussion covers two programming and software design concepts:

- The Single Responsibility Principle (SRP)
- DRY Code (**D**on't **R**epeat **Y**ourself)

---

## Part 1: Function Design

### Single Responsibility Principle (SRP)

The function `analyze_and_visualize_molecule`, which currently performs multiple tasks:

1. Reading and parsing the molecular file.
2. Assigning colors and calculating molecular weight.
3. Visualizing the molecule.

These tasks can be split into separate functions, each focusing on one specific part:

- A function for reading and parsing the molecular file.
- A function for calculating molecular weight.
- A function for visualizing the molecule.

**Benefits of SRP**:

- **Easier debugging**: Each function has a single, specific task.
- **Improved readability**: Functions are clearly labeled and easy to understand.
- **Enhanced reusability**: Individual functions can be reused across codebases.

**Example Refactor**:

```python
def read_molecule_file(file_name):
    with open(file_name) as f:
        data = f.readlines()
    return data[2:]  # Skip the first two lines for simplicity

def calculate_molecular_weight(atoms):
    weights = {'H': 1, 'O': 16, 'N': 14, 'C': 12}
    return sum(weights[atom] for atom, _ in atoms)

def get_atom_color(atom):
    colors = {'H': 'white', 'O': 'red', 'N': 'blue', 'C': 'gray'}
    return colors.get(atom, 'pink')  # Default to pink

def visualize_molecule(atoms, colors):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    for (atom, coord), color in zip(atoms, colors):
        ax.scatter(*coord, color=color)
    plt.show()
```

### DRY Code

In the original function, repetitive logic for determining atomic weights and colors can be centralized in functions or dictionaries, reducing code duplication and enhancing maintainability.

### Filepaths

Hardcoding file paths can be problematic and limiting to the user. When reading from files, the file paths should most often be given as input parameters.

---

## Part 2: Class Design

### SRP and DRY in the `Molecule` Class

In the `Molecule` class, SRP and DRY principles can be improved. Currently, the class mixes:

1. Atom data management.
2. Molecular weight calculation.
3. Visualization.

These tasks should likely be separated.
  
To make classes more "Pythonic"  - Instead of using `get_something` or `set_something` methods, the `@property` decorator. This way, attributes like molecular weight can be accessed directly.

**Example**:

```python
class Molecule:
    def __init__(self):
        self._atoms = []

    def add_atom(self, atom_type, x, y, z):
        self._atoms.append({'type': atom_type, 'x': x, 'y': y, 'z': z})

    @property
    def atoms(self):
        return self._atoms

    @property
    def molecular_weight(self):
        weights = {'H': 1, 'O': 16, 'N': 14, 'C': 12}
        return sum(weights[atom['type']] for atom in self._atoms)
```

### Molecule Class in C++

