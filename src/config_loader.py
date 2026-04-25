"""
Configuration Loader.
Provides utility functions to load configuration files
used across the project.
"""
import yaml
def load_config(path: str):
    """
    Load configuration from a YAML file.
    Args:
        path (str): Path to the YAML configuration file.
    Returns:
        dict: Parsed configuration as a dictionary. 
    Raises:
        FileNotFoundError: If the file does not exist.
        yaml.YAMLError: If the file contains invalid YAML.
    """
    with open(path, "r") as file:
        return yaml.safe_load(file)