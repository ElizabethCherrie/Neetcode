// 347. Top K Frequent Elements
// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for(int n : nums){
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        }
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(
            (a,b) -> b.getValue() - a.getValue()
        );

        pq.addAll(freq.entrySet());

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = pq.poll().getKey();
        }

        return result;
    }
}