import os # system library
from pathlib import Path # for handling file paths automatically conver to OS-specific paths
import logging # logging library

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "mlProject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py",



]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} for file: {file_name}")
    
    if (not os.path.exists(file_path) or (os.path.getsize(file_path) == 0)):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Created file: {file_path}")

    else:
        logging.info(f"File already exists and is not empty: {file_path}")
