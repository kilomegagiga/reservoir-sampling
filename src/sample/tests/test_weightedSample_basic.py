from sample.sample import WeightedSample

class Test_WeightedSample:
  def test_mustInitializeWithoutError(self):
    ws = WeightedSample([],0)
    assert ws

