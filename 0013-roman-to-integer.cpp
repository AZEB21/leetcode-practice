class Solution {
public:
    int romanToInt(string s) {
        
        unordered_map <char ,int> Roman= {
{'I' ,1}, {'V',5},{'X',10},{'L',50},
{'C',100} ,{'D',500},{'M',1000} };
 int i=0;
 int result=0;
while(i<s.size()){
    if(i+1<s.size() && Roman[s[i]]<Roman[s[i+1]] ){
        result -=Roman[s[i]];
    }else {
        result +=Roman[s[i]];
    }
    i++;
}
return result;
    }
};