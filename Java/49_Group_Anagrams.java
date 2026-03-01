//Task 49. Group Anagrams
//Given an array of strings strs, group the anagrams together. You can return the answer in any order.

import java.util.*;
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anag = new HashMap<>();

        for(String st:strs){
            char[] chars = st.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            anag.putIfAbsent(sorted, new ArrayList<>());
            anag.get(sorted).add(st);

        }

        return new ArrayList<>(anag.values());
    }
}