from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, RobustScaler
from sklearn.tree import DecisionTreeClassifier

from model.config.core import config

# Creating the pipeline

scaler = RobustScaler()
encoder = OrdinalEncoder()
params = {"criterion": "entropy", "max_depth": 24}
classifier = DecisionTreeClassifier()

# Preprocessing steps for the numerical variables
num_preproc = Pipeline(steps=[("scaler", scaler)])

# Preprocessing steps for the categorical variables
cat_preproc = Pipeline(steps=[("encoder", encoder)])

preprocessor = ColumnTransformer(
    transformers=[
        ("cat_preprocessor", cat_preproc, config.model_config.categorical_vars),
        ("numerical_preprocessor", num_preproc, config.model_config.numerical_vars),
    ]
)

pipe = Pipeline(steps=[("preprocessing", preprocessor), ("model", classifier)])
