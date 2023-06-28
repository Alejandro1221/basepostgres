#!/bin/bash

# Espera a que el servicio de la base de datos esté disponible
while ! nc -zv db 5432; do
  sleep 1
done

flask db migrate
flask db upgrade

python3 app.py
