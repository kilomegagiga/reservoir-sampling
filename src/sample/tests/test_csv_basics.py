
import os
import csv

class Test_os_module:

  def test_mustFindLocationOfCurrentFile(self):
    file_path = os.path.realpath(__file__)
    assert file_path
    assert '/' == file_path[:1]
    assert '.py' == file_path[-3:]

  def test_mustFindParentDirectory(self):
    file_path = os.path.realpath(__file__)
    base_name = os.path.basename(file_path)
    parent_path = os.path.abspath(os.path.join(file_path, os.pardir))
    rejoined_path = os.path.join(parent_path, base_name)
    assert file_path != parent_path
    assert file_path != base_name
    assert file_path == rejoined_path


class Test_csv_module:

  def test_mustImportTabSeparatedValues(self):
    ## Reading from a list instead of a file is not 
    ## documented to work, but it does.

    so_called_file = ['\tfirst\tsecond\tthird']
    reader = csv.reader(so_called_file, delimiter='\t')
    result = ''
    for row in reader:
      result = result + ', '.join(row) + '\n'
        
    assert ', first, second, third\n' == result

  def test_mustImportFromFile(self):
    
    file_path = os.path.realpath(__file__)
    assert os.path.exists(file_path)
    example_path = os.path.abspath(os.path.join(file_path, os.pardir))
    assert os.path.exists(example_path)
    example_path = os.path.join(example_path, "test_rsrc")
    assert os.path.exists(example_path)
    example_path = os.path.join(example_path, "example.tsv")
    assert os.path.exists(example_path)
    result = ''
    with open(example_path, newline='') as file:
      reader = csv.reader(file, delimiter='\t')
      for row in reader:
        result = result + ', '.join(row) + '\n'
    assert ', one, 1\n, two, 2\n, three, 3\n' == result

