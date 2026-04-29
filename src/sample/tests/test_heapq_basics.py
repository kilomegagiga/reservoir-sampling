
import heapq

class Test_heapq_module:
  def test_canReturnHeapCount(self):
    pq = []
    heapq.heappush(pq, (1, "one"))
    heapq.heappush(pq, (2, "two"))
    heapq.heappush(pq, (3, "three"))
    assert 3 == len(pq)
 
