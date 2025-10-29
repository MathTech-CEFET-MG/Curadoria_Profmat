#!/bin/bash

rm ./docs/dissertations/*
rm ./docs/schools/*
rm ./docs/years/*

python src/csv_to_md.py

uv run -m mkdocs serve