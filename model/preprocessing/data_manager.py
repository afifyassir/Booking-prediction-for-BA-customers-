import logging
from pathlib import Path
from typing import List

import joblib
import pandas as pd
from feature_engine.encoding import RareLabelEncoder
from sklearn.pipeline import Pipeline

from model import __version__ as _version
from model.config.core import DATASET_DIR, TRAINED_MODEL_DIR, config

logger = logging.getLogger(__name__)


def _load_raw_dataset(*, file_name: str) -> pd.DataFrame:
    dataframe = pd.read_csv(Path(f"{DATASET_DIR}/{file_name}"), encoding="ISO-8859-1")
    transformed = handle_rare_labels(dataset=dataframe)
    return transformed


def load_dataset(*, file_name: str) -> pd.DataFrame:
    dataframe = pd.read_csv(Path(f"{DATASET_DIR}/{file_name}"), encoding="ISO-8859-1")
    transformed = handle_rare_labels(dataset=dataframe)
    return transformed


def save_pipeline(*, pipeline_to_persist: Pipeline) -> None:
    """Persist the pipeline.
    Saves the versioned model, and overwrites any previous
    saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.
    """

    # Prepare versioned save file name
    save_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)


def load_pipeline(*, file_name: str) -> Pipeline:
    """Load a persisted pipeline."""

    file_path = TRAINED_MODEL_DIR / file_name
    return joblib.load(filename=file_path)


def remove_old_pipelines(*, files_to_keep: List[str]) -> None:
    """
    Remove old model pipelines.
    This is to ensure there is a simple one-to-one
    mapping between the package version and the model
    version to be imported and used by other applications.
    """
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()


def handle_rare_labels(dataset: pd.DataFrame) -> pd.DataFrame:
    # Grouping rare categories in a new
    # category called "other"
    lab_enc = RareLabelEncoder(
        variables=config.model_config.categorical_vars,
        n_categories=1,
        tol=0.0003,
        replace_with="other",
    )
    return lab_enc.fit_transform(dataset)
