"""API Flask para simulador de operaciones de conjuntos."""

from __future__ import annotations

from typing import Any

from flask import Flask, jsonify, request
from flask_cors import CORS

from app.services.operaciones import resolver_operaciones

app = Flask(__name__)
CORS(app)


def _normalizar_entrada(elementos: list[str]) -> list[Any]:
    """Intenta convertir numericos, en otro caso deja el string."""
    salida: list[Any] = []
    for elemento in elementos:
        limpio = elemento.strip()
        if limpio == "":
            continue
        try:
            if "." in limpio:
                salida.append(float(limpio))
            else:
                salida.append(int(limpio))
        except ValueError:
            salida.append(limpio)
    return salida


@app.get("/health")
def health() -> tuple[dict[str, str], int]:
    return {"status": "ok"}, 200


@app.post("/api/conjuntos/operaciones")
def operaciones() -> tuple[Any, int]:
    body = request.get_json(silent=True) or {}
    a = body.get("A")
    b = body.get("B")

    if not isinstance(a, list) or not isinstance(b, list):
        return jsonify({"error": "A y B deben ser listas de elementos."}), 400

    resultado = resolver_operaciones(_normalizar_entrada(a), _normalizar_entrada(b))
    return jsonify(resultado), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
