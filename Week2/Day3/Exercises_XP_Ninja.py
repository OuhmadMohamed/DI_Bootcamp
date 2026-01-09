from abc import ABC, abstractmethod

class Temperature(ABC):
    def __init__(self, value: float):
        self._kelvin = self.to_kelvin(value)

    @abstractmethod
    def to_kelvin(self, value: float) -> float:
        pass

    @abstractmethod
    def from_kelvin(self, kelvin: float) -> float:
        pass

    def to_celsius(self):
        return Celsius(self._kelvin)

    def to_fahrenheit(self):
        return Fahrenheit(self._kelvin)

    def to_kelvin_unit(self):
        return Kelvin(self._kelvin)

    def __repr__(self):
        return f"{self.from_kelvin(self._kelvin):.2f} {self.__class__.__name__}"


class Celsius(Temperature):
    def to_kelvin(self, value):
        return value + 273.15

    def from_kelvin(self, kelvin):
        return kelvin - 273.15


class Fahrenheit(Temperature):
    def to_kelvin(self, value):
        return (value - 32) * 5 / 9 + 273.15

    def from_kelvin(self, kelvin):
        return (kelvin - 273.15) * 9 / 5 + 32


class Kelvin(Temperature):
    def to_kelvin(self, value):
        return value

    def from_kelvin(self, kelvin):
        return kelvin


t = Celsius(25)
print(t)                      # 25.00 Celsius
print(t.to_fahrenheit())      # 77.00 Fahrenheit
print(t.to_kelvin_unit())     # 298.15 Kelvin

##################################
#Exercise 2 — In the Quantum Realm

import random


class QuantumParticle:
    def __init__(self, x=None, y=None):
        self.x = x if x is not None else random.randint(1, 10000)
        self.y = y if y is not None else random.random()
        self.p = random.choice([0.5, -0.5])
        self.entangled_particle = None

    # =========================
    # Internal disturbance
    # =========================
    def _disturb(self):
        self.x = random.randint(1, 10000)
        self.y = random.random()
        print("Quantum Interferences!!")

    # =========================
    # Measurements
    # =========================
    def position(self):
        self._disturb()
        return self.x

    def momentum(self):
        self._disturb()
        return self.y

    def spin(self):
        self._disturb()

        if self.entangled_particle:
            # Opposite spin
            self.p = random.choice([0.5, -0.5])
            self.entangled_particle.p = -self.p
            print("Spooky Action at a Distance !!")

        return self.p

    # =========================
    # Quantum Entanglement
    # =========================
    def entangle(self, other):
        if not isinstance(other, QuantumParticle):
            raise TypeError("Can only entangle with another QuantumParticle")

        self.entangled_particle = other
        other.entangled_particle = self

        print("Spooky Action at a Distance !!")
        return f"Particle {id(self)} is now in quantum entanglement with Particle {id(other)}"

    # =========================
    # Representation
    # =========================
    def __repr__(self):
        return (
            f"QuantumParticle(x={self.x}, "
            f"momentum={self.y:.3f}, "
            f"spin={self.p})"
        )

p1 = QuantumParticle(x=1, y=5.0)
p2 = QuantumParticle(x=2, y=5.0)

p1.entangle(p2)
# Spooky Action at a Distance !!

print(p1.spin())
# Quantum Interferences!!
# Spooky Action at a Distance !!

print(p2.spin())
# Quantum Interferences!!
