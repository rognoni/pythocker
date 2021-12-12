#!/usr/bin/env python

import os, subprocess

if not os.path.exists('py-env'):
    os.system('python -m venv py-env')
    subprocess.run('source py-env/bin/activate; pip install poetry; poetry install', shell=True, capture_output=True, executable="/bin/bash")

os.system('tail -f /dev/null')
