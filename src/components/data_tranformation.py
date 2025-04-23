import sys
from dataclasses import dataclass
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from src.expection import CustomException
from src.logger import logging
import os

@dataclass
class DataTransformationconfig:
  preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class Datatransformation:
  def __inti__(self):
    self.data_transformation_config=DataTransformationconfig()
  
  def get_data_transformation_object(self):
    try:
      numerical_columns = ["writing_score", "reading_score"]
      categorical_columns = ["gender",
                             "race_ethnicity",
                             "lunch",
                             "test_preparation_course",
      ]
      num_pipeline=Pipeline(
        steps=[
          ("imputer",SimpleImputer(strategy="median")),
          ("scaler",StandardScaler())
        ]
      )
      cat_pipeline=Pipeline(
        steps=[
          ("imputer",SimpleImputer(strategy=""))
        ]
      )
    except:
