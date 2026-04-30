from sample.sample import WeightedSample

class Test_WeightedSample:
  one_half = 1./2.
  one_third = 1./3.
  one_fourth = 1./4.
  one_fifth = 1./5.
  one_sixth = 1./6.
  one_seventh = 1./7.
  one_eighth = 1./8.
  one_ninth = 1./9.
  one_tenth = 1./10.
  one_eleventh = 1./11.

  example_items = []

  def load_example_items(self):
    self.example_items = [
      ( self.one_half , "one_half") ,
      ( self.one_third , "one_third") ,
      ( self.one_fourth , "one_fourth") ,
      ( self.one_fifth , "one_fifth") ,
      ( self.one_sixth , "one_sixth") ,
      ( self.one_seventh , "one_seventh") ,
      ( self.one_eighth , "one_eighth") ,
      ( self.one_ninth , "one_ninth") ,
      ( self.one_tenth , "one_tenth") ,
      ( self.one_eleventh , "one_eleventh")
    ]

  def test_mustInitializeWithoutError(self):
    ws = WeightedSample([],0)
    assert ws

  def test_mustAcceptWeightItem(self):
    ws = WeightedSample([(0.1, "item")], 1)
    assert ws

  def test_mustSucceedMinimalExample(self):
    ws = WeightedSample([(0.1, "item")], 1)
    assert ws
    sample = ws.extract()
    assert sample
    assert 1 == len(sample)
    assert 1.0 > sample[0][0]
    assert 0.0 < sample[0][0]
    assert "item" == sample[0][1]

  def test_mustReturnCorrectNumberOfItems(self):
    self.load_example_items()
    assert self.example_items
    assert 10 == len(self.example_items)
    ws = WeightedSample(self.example_items,5)
    assert ws
    sample = ws.extract()
    assert sample
    assert 5 == len(sample)
    
