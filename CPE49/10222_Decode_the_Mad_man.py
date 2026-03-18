a = "1234567890qwertyuiop[]asdfghjkl;'zxcvbnm,./"
dict = {}
for i in range(2, len(a)):
    dict[a[i]] = a[i - 2]
dict[' '] = ' '
while True:
    try:
        s = input()
    except:
        break
    ans = ""
    for ch in s:
        if (ch.isupper()):
            ch = ch.lower()
        ans += dict[ch]
    print(ans);
