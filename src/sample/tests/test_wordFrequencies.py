
from sample.WordFrequencies import WordFrequencies

class Test_WordFrequencies_module:
  def test_mustHaveNounList(self):
    wf = WordFrequencies()
    assert 'noun.txt' == wf.get_source_filename('nouns')[-8:]

    source = wf.get_source('nouns')
    assert 3030 == len(source)
