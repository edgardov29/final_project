# NLP Emotion Detection - Proyecto Final

Este proyecto implementa un **detector de emociones** usando técnicas de Procesamiento de Lenguaje Natural (NLP) y un servidor Flask.

## Objetivo
El sistema recibe texto como entrada y devuelve las emociones detectadas (ira, disgusto, miedo, alegría, tristeza) junto con la emoción dominante.

## Funcionalidades
- Interfaz web en `localhost:5000` con formulario para introducir texto.
- Endpoint `/emotionDetector` que devuelve resultados en formato JSON.
- Manejo de errores para entradas vacías (mensaje: "¡Texto inválido! ¡Por favor, intenta de nuevo!").
- Código validado con PyLint para cumplir estándares de calidad.

## Ejecución
1. Instalar dependencias:
   ```bash
   python3 -m pip install flask pylint requests
