class Solution {
    public boolean isAnagram(String s, String t) {
        
        char[] ca_1 = s.toCharArray();
        char[] ca_2 = t.toCharArray();
        Arrays.sort(ca_1);
        Arrays.sort(ca_2);
        s = String.valueOf(ca_1);
        t = String.valueOf(ca_2);
        if (s.equals(t) == true){
            return true;
        }
        else 
        {
            return false;
        }


       
    
    
    }
}