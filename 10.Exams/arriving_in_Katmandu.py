import re

while True:
    string = input()
    if string == "Last note":
        break
    pattern = r"((^[\d+\w\!\@\#\$\?]+)=(\d+)<<(.+)$)"
    match = re.findall(pattern, string)
    if not match:
        print("Nothing found!")
    for n in match:
        if not match:
            print("Nothing found!")
        if len(match[0][3]) == int(match[0][2]):
            pattern2 = r"[a-zA-Z]"
            match2 = re.findall(pattern2, match[0][1])
            new_match = ("".join(match2))
            print(f"Coordinates found! {new_match} -> {match[0][3]}")
        else:
            print("Nothing found!")
        # if "," in match[0][0]:
        #     print("Nothing found!")
        # elif ":" in match[0][0]:
        #     print("Nothing found!")
        # elif "." in match[0][0]:
        #     print("Nothing found!")
