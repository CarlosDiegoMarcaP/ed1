"""Servicios para ejecutar operaciones de conjuntos."""

from __future__ import annotations

from typing import Any

from app.models.conjunto import Conjunto


def resolver_operaciones(a: list[Any], b: list[Any]) -> dict[str, Any]:
    conjunto_a = Conjunto.desde_iterable(a)
    conjunto_b = Conjunto.desde_iterable(b)

    return {
        "A": conjunto_a.a_lista_ordenada(),
        "B": conjunto_b.a_lista_ordenada(),
        "union": conjunto_a.union(conjunto_b).a_lista_ordenada(),
        "interseccion": conjunto_a.interseccion(conjunto_b).a_lista_ordenada(),
        "diferencia_A_B": conjunto_a.diferencia(conjunto_b).a_lista_ordenada(),
        "diferencia_B_A": conjunto_b.diferencia(conjunto_a).a_lista_ordenada(),
        "diferencia_simetrica": conjunto_a.diferencia_simetrica(conjunto_b).a_lista_ordenada(),
        "A_subconjunto_B": conjunto_a.es_subconjunto(conjunto_b),
        "B_subconjunto_A": conjunto_b.es_subconjunto(conjunto_a),
        "A_superconjunto_B": conjunto_a.es_superconjunto(conjunto_b),
        "B_superconjunto_A": conjunto_b.es_superconjunto(conjunto_a),
    }
