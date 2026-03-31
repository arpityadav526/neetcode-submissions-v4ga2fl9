class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        counter={}

        for i in nums:
            counter[i]=1+counter.get(i,0)
            top_two = sorted(counter.items(), key=lambda item: item[1], reverse=True)[:k]

        return [i[0] for i in top_two]
        

