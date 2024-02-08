import re
number = int(raw_input())
def yes_or_no(phone_num):
    if(len(phone_num)==10):
	if(re.match(r'[7-9]',phone_num) and phone_num.isdigit()):   ##re.match only match the beginging of a string, re.search would match any of string, re.fullmatch match all of string.
            answer = "YES"
        else:
            answer = "NO"
    else:
        answer = "NO"   
    return answer

for i in range(0,number):
    phone_num = raw_input()
    answer = yes_or_no(phone_num)
    print(answer)


Python offers different primitive operations based on regular expressions:

re.match() checks for a match only at the beginning of the string

re.search() checks for a match anywhere in the string (this is what Perl does by default)

re.fullmatch() checks for entire string to be a match

For example:

>>>
re.match("c", "abcdef")    # No match
re.search("c", "abcdef")   # Match
<re.Match object; span=(2, 3), match='c'>
re.fullmatch("p.*n", "python") # Match
<re.Match object; span=(0, 6), match='python'>
re.fullmatch("r.*n", "python") # No match
