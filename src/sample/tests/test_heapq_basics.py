
import heapq

class Test_heapq_module:

  oneSeventh = 1.0/7.

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
 
