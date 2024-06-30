def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words,nums,words)


t=((786,"awais"),(1100,"saqib"),(1099,"saad"),(1098,"ali abbas"),(1097,"mubeen"),(1096,"abdullah"),(1095,"ismail"),(1090,"Nimra"))

a,b,c,nums,words=get_data(t)
print(nums)
print(words)
print(a)
print(b)
print(c)
