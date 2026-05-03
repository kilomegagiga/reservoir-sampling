
import os
import csv
from sample.sample import WeightedSample

class Test_collected_sample:
  data_file_names = [
    "ucrel.lancs.ac.uk-bncfreq-lists-5_1_all_rank_noun.txt",
    "ucrel.lancs.ac.uk-bncfreq-lists-5_2_all_rank_verb.txt",
    "ucrel.lancs.ac.uk-bncfreq-lists-5_3_all_rank_adjective.txt",
    "ucrel.lancs.ac.uk-bncfreq-lists-5_4_all_rank_adverb.txt"
    ]

  def data_path_to_nouns(self):
    data_file_name = self.data_file_names[0]

    file_path = os.path.realpath(__file__)
    data_path = file_path
    data_path = os.path.abspath(os.path.join(data_path, os.pardir))
    data_path = os.path.abspath(os.path.join(data_path, os.pardir))
    data_path = os.path.join(data_path, 'rsrc')
    data_path = os.path.join(data_path, data_file_name)
    return data_path

  def load_from_path(self, data_path):
    result = []
    with open(data_path, newline='') as file:
      reader = csv.reader(file, delimiter='\t')
      for row in reader:
        result.append([float(row[2]), row[1]])
    return result
    

  def test_mustBeCorrectSize(self):
    data_path = self.data_path_to_nouns()
    assert '.txt' == data_path[-4:]
    assert os.path.exists(data_path)

    frequencyNouns = self.load_from_path(data_path)
    assert 'time' == frequencyNouns[0][1]
    assert 10 == frequencyNouns[-1][0]

    ws = WeightedSample(frequencyNouns, 27)
    sample = ws.extract()

    assert 27 == len(sample)

