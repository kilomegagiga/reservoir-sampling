
import heapq

class Test_heapq_module:

  oneTenth = 1.0/10.
  oneSeventh = 1.0/7.
  oneFifth = 1.0/5.

  def test_canInsertRealNumber(self):
    pq = []
    heapq.heappush(pq, (self.oneSeventh, "a seventh"))
    assert self.oneSeventh == pq[0][0]

  def test_canReturnHeapCount(self):
    pq = []
    heapq.heappush(pq, (1, "one"))
    heapq.heappush(pq, (2, "two"))
    heapq.heappush(pq, (3, "three"))
    assert 3 == len(pq)
 
  def test_canReturnMinimumValueOfHeap(self):
    pq = []
    heapq.heappush(pq, (self.oneSeventh, "a seventh"))
    heapq.heappush(pq, (self.oneTenth, "a tenth"))
    heapq.heappush(pq, (self.oneFifth, "a fifth"))
    assert self.oneTenth == pq[0][0]

