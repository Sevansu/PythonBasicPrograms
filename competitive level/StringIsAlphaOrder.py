def order(s):
    return (all(s[i+1].lower() >= s[i].lower() for i in range(len(s)-1))) if s.isalpha() else print("Error:Please only enter alphabets")
