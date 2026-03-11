# Logic Gate Simulator

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)

**Object-oriented logic gate simulation in Python.**

A clean implementation of digital logic gates using inheritance and polymorphism, demonstrating OOP design patterns.

---

## Features

- **Base Classes**: `LogicGate`, `BinaryGate`, `UnaryGate`
- **Gate Implementations**: AND, OR, NOT, NAND, NOR
- **Extensible Design**: Easy to add new gate types
- **Interactive Input**: Command-line pin value entry

---

## Class Hierarchy

```
LogicGate (base)
├── BinaryGate
│   ├── AndGate
│   ├── OrGate
│   └── NandGate
└── UnaryGate
    └── NotGate
```

---

## Usage

```python
from logicGateClasses import AndGate

gate = AndGate("G1")
result = gate.get_output()
# Enter pin A input for gate G1: 1
# Enter pin B input for gate G1: 1
# result = 1
```

---

## Concepts Demonstrated

- Class inheritance
- Method overriding
- Polymorphism
- Constructor chaining with `super()`

---

<p align="center">
  Built by <a href="https://nickstafford.dev">Nick Stafford</a>
</p>
