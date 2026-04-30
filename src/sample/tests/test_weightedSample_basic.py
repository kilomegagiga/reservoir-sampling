from sample.sample import WeightedSample

class Test_WeightedSample:
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
    assert 0.1 > sample[0][0]
    assert 0.0 < sample[0][0]
    assert "item" == sample[0][1]
