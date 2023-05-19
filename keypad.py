def keypad_char(s):
    str=["2", "22", "222",
         "3", "33", "333",
         "4", "44", "444",
         "5", "55", "555",
         "6", "66", "666",
         "7", "77", "777", "7777",
         "8", "88", "888", "8888",
         "9", "99", "999", "9999"]

    answer = ""
    # nonchar_dict = {"1":"1", "0":"0", "*":"*", "#":"#"}
    nonchar_dict = {i:i for i in ("1","0","*","#")} 
    alpha_dict={chr(i+65):i for i in range(26)}


    for i in s:
        if i in nonchar_dict:
            answer += nonchar_dict[i]
        else:
            answer += str[alpha_dict[i]]
    return answer


s="GEEKSFORGEEKS"
print(keypad_char(s))

 
