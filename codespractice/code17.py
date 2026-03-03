#prefix "is" sting modifier
def new_string(text):#define a fun name "new_sting"that take str para called "text"
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text
    print(new_string("Array"))
    print(new_string("IsEmpty"))
