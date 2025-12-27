#!/bin/bash

sudo apt update

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install pypandoc

sudo apt install texlive-xetex texlive-latex-extra texlive-fonts-recommended -y

pypandoc --version
xelatex --version

python3 convert.py