import os
from pathlib import Path

# Define the project structure
project_structure = {
    "data": ["raw", "processed", "interim", "external"],
    "src": {
        "data": ["__init__.py", "preprocess_data.py"],
        "features": ["build_features.py"],
        "models": ["__init__.py", "train_model.py", "predict_model.py"],
        "visualization": ["visualize.py"],
        "utils": ["helper_functions.py"],
        "config": ["config.yaml"],
    },
    "models": {
        "model1": ["model.pkl", "model_params.json"],
        "model2": ["model.pkl", "model_params.json"],
    },
    "reports": ["figures", "tables", "presentations"],
    "notebooks": ["exploration", "modeling"],
    "docs": ["README.md", "report.md"],
    "tests": ["test_data.py", "test_models.py"],
    "root_files": ["environment.yml", "requirements.txt", "main.py"],
}

# Function to create directories and files
def create_project_structure(base_path, structure):
    for folder, contents in structure.items():
        if isinstance(contents, dict):  # Nested folders
            for subfolder, subcontents in contents.items():
                path = Path(base_path) / folder / subfolder
                path.mkdir(parents=True, exist_ok=True)
                for file in subcontents:
                    file_path = path / file
                    file_path.touch(exist_ok=True)
        elif isinstance(contents, list):  # Files or subfolders
            path = Path(base_path) / folder
            path.mkdir(parents=True, exist_ok=True)
            for item in contents:
                if "." in item:  # It's a file
                    file_path = path / item
                    file_path.touch(exist_ok=True)
                else:  # It's a subfolder
                    subfolder_path = path / item
                    subfolder_path.mkdir(parents=True, exist_ok=True)

# Create the project structure
def main():
    project_name = input("Enter the project name: ")
    base_path = Path(project_name)
    create_project_structure(base_path, project_structure)
    print(f"Project structure created at: {base_path}")

if __name__ == "__main__":
    main()