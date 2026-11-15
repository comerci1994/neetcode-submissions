class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting_list=Counter(nums).most_common(k)
        top_k_freq=[]
        for more_freq in counting_list:
            top_k_freq.append(more_freq[0])
        return top_k_freq