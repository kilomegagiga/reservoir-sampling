
## Pseudocode for the A-Res algorithm by Efraimidis and Spirakis
## as presented on the Reservoir_sampling wikipedia page.

##  ##  S is a stream of items to sample
##  ##  S.Current returns current item in stream
##  ##  S.Weight  returns weight of current item in stream
##  ##  S.Next advances stream to next position
##  ##  The power operator is represented by ^
##  ##  min-priority-queue supports:
##  ##    Count -> number of items in priority queue
##  ##    Minimum() -> returns minimum key value of all items
##  ##    Extract-Min() -> Remove the item with minimum key
##  ##    Insert(key, Item) -> Adds item with specified key
##  
##  ReservoirSample(S[1..?])
##    H := new min-priority-queue
##    while S has data
##      r := random() ^ (1/S.Weight)   // random() produces a uniformly random number in (0,1)
##      if H.Count < k
##        H.Insert(r, S.Current)
##      else
##        // keep k items with largest associated keys
##        if r > H.Minimum
##          H.Extract-Min()
##          H.Insert(r, S.Current)
##        end
##      end
##      S.Next
##    end
##    return items in H
##  end


## Tests are in place that confirm the needed functionality
## is provided by the heapq module.
import heapq

import random

class WeightedSample:
  ## Select a weighted sample using A-Res reservoir sampling
  items = []
  k = 0  ## size of sample to select
  pq = []  ## a priority queue ultimately holding the sample
  
  def __init__(self, weightedItemsI, kI):
    ## a weightedItem is a tuple of form (weight, rawItem)
    self.k = kI
    self.items = weightedItemsI

  def extract(self):
    self.pq = []

    for item in self.items:
      r = random.random() ** (1/item[0])
      if len(self.pq) < self.k:
        heapq.heappush(self.pq, (r, item[1]))
      else:
        ## keep k items with largest associated keys
        if r > self.pq[0][0]:
          heapq.heappop(self.pq)
          heapq.heappush(self.pq, (r, item[1]))
    ## self.pq contains the result
    return self.pq

