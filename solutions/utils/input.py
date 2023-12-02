"""
    Helper functions for parsing input data files neccessary for developing 
    AoC solutions.
"""
import os
from pathlib import Path


def get_input_data(file_name: str, data_dir: str = "data") -> list[str]:
    """Returns the contents of the provided data file as a list
    of strings. Each string represents a line in the file.

    Parameters
    ----------
    file_name : str
        The name of the file to read.

    data_dir : str, optional (default: "./data")
        The directory containing the data files.

    Returns
    -------
    list[str]
        The contents of the file as a list of strings.
    """
    project_dir = Path(__file__).parent.parent.parent
    data_dir = os.path.join(project_dir, data_dir)
    filepath = os.path.join(data_dir, file_name)
    with open(filepath, "r", encoding="utf-8") as input_file:
        lines_list = input_file.readlines()
    return lines_list
