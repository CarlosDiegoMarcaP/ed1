"""Modelo de conjunto para operaciones basicas."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable


@dataclass
class Conjunto:
    """Representa un conjunto y sus operaciones elementales."""

    elementos: set[Any] = field(default_factory=set)

    @classmethod
    def desde_iterable(cls, elementos: Iterable[Any]) -> "Conjunto":
        return cls(set(elementos))

    def union(self, otro: "Conjunto") -> "Conjunto":
        return Conjunto(self.elementos | otro.elementos)

    def interseccion(self, otro: "Conjunto") -> "Conjunto":
        return Conjunto(self.elementos & otro.elementos)

    def diferencia(self, otro: "Conjunto") -> "Conjunto":
        return Conjunto(self.elementos - otro.elementos)

    def diferencia_simetrica(self, otro: "Conjunto") -> "Conjunto":
        return Conjunto(self.elementos ^ otro.elementos)

    def es_subconjunto(self, otro: "Conjunto") -> bool:
        return self.elementos.issubset(otro.elementos)

    def es_superconjunto(self, otro: "Conjunto") -> bool:
        return self.elementos.issuperset(otro.elementos)

    def a_lista_ordenada(self) -> list[Any]:
        return sorted(self.elementos, key=lambda x: (str(type(x)), str(x)))
