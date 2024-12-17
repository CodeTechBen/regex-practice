import re

sentences = ["His birthday was on the 3rd of october 1997.", "He had 12 usb's 1 of them was working.", "There are 12 apples, 3 bananas, and 45 oranges."]
nums = []
for s in sentences:
    nums.append(re.findall(r'[0-9]+',s))
print(nums)
                           