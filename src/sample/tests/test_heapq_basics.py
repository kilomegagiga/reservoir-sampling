
import heapq

class Test_heapq_module:

  oneTenth = 1.0/10.
  oneSeventh = 1.0/7.
  oneFifth = 1.0/5.
  oneHalf = 1.0/2.

  def test_mustInsertRealNumber(self):
    pq = []
    heapq.heappush(pq, (self.oneSeventh, "a seventh"))
    assert self.oneSeventh == pq[0][0]

  def test_mustReturnHeapCount(self):
    pq = []
    heapq.heappush(pq, (self.oneSeventh, "a seventh"))
    heapq.heappush(pq, (self.oneTenth, "a tenth"))
    heapq.heappush(pq, (self.oneFifth, "a fifth"))
    assert 3 == len(pq)
 
  def test_mustReturnMinimumValueOfHeap(self):
    pq = []
    heapq.heappush(pq, (self.oneSeventh, "a seventh"))
    heapq.heappush(pq, (self.oneTenth, "a tenth"))
    heapq.heappush(pq, (self.oneFifth, "a fifth"))
    assert self.oneTenth == pq[0][0]

  def test_mustRemoveMinimumItemAndInsertSomethingLarger(self):
    pq = []
    heapq.heappush(pq, (self.oneSeventh, "a seventh"))
    heapq.heappush(pq, (self.oneTenth, "a tenth"))
    heapq.heappush(pq, (self.oneFifth, "a fifth"))
    min = heapq.heappop(pq)
    heapq.heappush(pq, (self.oneHalf, "a half"))
    assert self.oneTenth == min[0]
    assert 3 == len(pq)
    assert self.oneSeventh == pq[0][0]


