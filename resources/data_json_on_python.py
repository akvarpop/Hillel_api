import json
import pathlib
from pathlib import Path

path = Path(pathlib.Path.cwd().parent, "resources", "data.json")

with open(path, 'r') as f:
    secret_variables = json.load(f)

NAME_ADMIN = secret_variables['name']
PASSWORD_ADMIN = secret_variables['password']
URL_ENDPOINT = secret_variables['endpoint']


