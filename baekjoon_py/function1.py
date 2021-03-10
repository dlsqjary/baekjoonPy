def say_myself(name, old, man=True):
    print("이름: %s " %name)
    print("나이: %d " %old)
    if man:
        print("남자")
    else:
        print("여자")

say_myself("abcd", 42, False)
