import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(filename="templates.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Root directory files
root_directory_files = [
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    "common/__init__.py",
    "execute_train_pipeline.py",
    "execute_prediction_pipeline.py",
]

# Training pipeline files
training_pipeline_files = [
    "training/configuration_manager/__init__.py",
    "training/configuration_manager/configuration.py",
    "training/config/config.yaml",
    "training/config/params.yaml",
    "training/config/schema.yaml",
    "training/components/__init__.py",
    "training/components/data_ingestion.py",
    "training/components/data_validation.py",
    "training/components/image_processing.py",
    "training/components/feature_extraction.py",
    "training/components/feature_engineering.py",
    "training/components/model_trainer.py",
    "training/components/model_evaluation.py",
    "training/pipeline/__init__.py",
    "training/pipeline/01_data_ingestion.py",
    "training/pipeline/02_data_validation.py",
    "training/pipeline/03_image_processing.py",
    "training/pipeline/04_feature_extraction.py",
    "training/pipeline/05_feature_engineering.py",
    "training/pipeline/06_model_trainer.py",
    "training/pipeline/07_model_evaluation.py",
    "training/entity/__init__.py",
    "training/entity/config_entity.py",
    "training/utils/__init__.py",
    "training/utils/common.py",
    "training/constants/__init__.py",
    "training/__init__.py",
]

# Deployment pipeline files
deployment_pipeline_files = [
    "deployment/app.py",
    "deployment/templates/index.html",
    "deployment/templates/train_evaluate.html",
    "deployment/templates/predict.html",
    "deployment/configuration_manager/__init__.py",
    "deployment/configuration_manager/configuration.py",
    "deployment/config/config.yaml",
    "deployment/config/params.yaml",
    "deployment/config/schema.yaml",
    "deployment/components/__init__.py",
    "deployment/components/data_ingestion.py",
    "deployment/components/data_validation.py",
    "deployment/components/image_processing.py",
    "deployment/components/feature_extraction.py",
    "deployment/components/feature_engineering.py",
    "deployment/components/model_loader.py",
    "deployment/components/prediction.py",
    "deployment/pipeline/__init__.py",
    "deployment/pipeline/01_data_ingestion.py",
    "deployment/pipeline/02_data_validation.py",
    "deployment/pipeline/03_image_processing.py",
    "deployment/pipeline/04_feature_extraction.py",
    "deployment/pipeline/05_feature_engineering.py",
    "deployment/pipeline/06_model_loader.py",
    "deployment/pipeline/07_prediction.py",
    "deployment/entity/__init__.py",
    "deployment/entity/config_entity.py",
    "deployment/utils/__init__.py",
    "deployment/utils/common.py",
    "deployment/constants/__init__.py",
    "deployment/__init__.py",
]

# Combine all file lists and create files
for list_of_files in [root_directory_files, training_pipeline_files, deployment_pipeline_files]:
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        # Create directories if they don't exist
        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Created directory: {filedir} for the file: {filename}")

        # Create the file if it doesn't exist or is empty
        if not filepath.exists() or filepath.stat().st_size == 0:
            filepath.touch()
            logging.info(f"Created empty file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")