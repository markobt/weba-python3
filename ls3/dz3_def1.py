def seasons(a):

    s_dict = {
        (12, 1, 2): "winter",
        (3,4,5):    "spring",
        (6,7,8):    "summer",
        (9,10,11):  "autum"
    }

    for k, v in s_dict.items():
        if a in k:
            print(v)

if __name__ == "__main__":
    seasons(12)
    seasons(5)
    seasons(9)
    seasons(6)
