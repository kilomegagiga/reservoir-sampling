
import os
import csv

class Test_word_frequency_data:

  data_file_names = [
    "ucrel.lancs.ac.uk-bncfreq-lists-5_1_all_rank_noun.txt",
    "ucrel.lancs.ac.uk-bncfreq-lists-5_2_all_rank_verb.txt",
    "ucrel.lancs.ac.uk-bncfreq-lists-5_3_all_rank_adjective.txt",
    "ucrel.lancs.ac.uk-bncfreq-lists-5_4_all_rank_adverb.txt"
    ]

  def test_mustBeFound(self):
    file_path = os.path.realpath(__file__)
    data_path = file_path
    assert os.path.exists(data_path)
    data_path = os.path.abspath(os.path.join(data_path, os.pardir))
    assert 'tests' == data_path[-5:]
    assert os.path.exists(data_path)
    data_path = os.path.abspath(os.path.join(data_path, os.pardir))
    assert 'sample' == data_path[-6:]
    assert os.path.exists(data_path)
    data_path = os.path.join(data_path, 'rsrc')
    assert os.path.exists(data_path)
    data_path = os.path.join(data_path, self.data_file_names[0])
    assert '.txt' == data_path[-4:]
    assert os.path.exists(data_path)

  def test_mustBeImportable(self):

    file_path = os.path.realpath(__file__)
    data_path = file_path
    data_path = os.path.abspath(os.path.join(data_path, os.pardir))
    data_path = os.path.abspath(os.path.join(data_path, os.pardir))
    data_path = os.path.join(data_path, 'rsrc')
    data_path = os.path.join(data_path, self.data_file_names[0])
    assert '.txt' == data_path[-4:]
    assert os.path.exists(data_path)

    result = ''
    with open(data_path, newline='') as file:
      reader = csv.reader(file, delimiter='\t')
      for row in reader:
        result = result + ', '.join(row) + '\n'
    assert ', time, ' == result[:8]
    assert ', 10\n' == result[-5:]

