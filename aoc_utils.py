"""Utilities to solve AoC problems."""


def read_input(file_name: str) -> list:
  """Read the input file and return a list of lines.
  
  Args:
    file_name: str, name of the input file. That has to be added
    to the path, in the test_input folder.

  Returns:
    list of str, lines in the input file.
  
  """
  _INPUT_PATH = 'test_inputs/'
  with open(_INPUT_PATH + file_name, 'r') as file:
    return [line.strip() for line in file]