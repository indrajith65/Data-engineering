import pandas as pd
from typing import List, Dict, Any
import logging
import kagglehub

# Download latest version
path = kagglehub.dataset_download("andrewmvd/data-engineer-jobs")

print("Path to dataset files:", path)
# logging.basicConfig(filename='app.log', level=logging.INFO)
# logger = logging.getLogger(__name__)
print(f"{path}\DataEngineer.csv")
input_file = pd.read_csv(f"{path}\DataEngineer.csv")
print(input_file.head())
class DataPipeline:
    """Basic data engineering pipeline."""
    
    def __init__(self, name: str):
        self.name = name
        self.data = None
    
    def extract(self, source: str) -> pd.DataFrame:
        """Extract data from source."""
        logger.info(f"Extracting from {source}")
        self.data = pd.read_csv(source)
        return self.data
    
    def transform(self, transformations: List[callable]) -> pd.DataFrame:
        """Apply transformations to data."""
        logger.info(f"Transforming {len(transformations)} steps")
        for transform in transformations:
            self.data = transform(self.data)
        return self.data
    
    def load(self, destination: str) -> None:
        """Load data to destination."""
        logger.info(f"Loading to {destination}")
        self.data.to_csv(destination, index=False)
    
    def run(self, source: str, destination: str, transformations: List[callable] = None):
        """Execute full pipeline."""
        self.extract(source)
        if transformations:
            self.transform(transformations)
        self.load(destination)
        logger.info(f"Pipeline {self.name} completed")

"""
# Example usage
if __name__ == "__main__":
    pipeline = DataPipeline("ETL_Pipeline")
    
    # Define transformations
    transforms = [
        lambda df: df.dropna(),
        # lambda df: df[df['age'] > 18],
    ]
    
    pipeline.run("input.csv", "output.csv", transforms)"""
input_file.head()