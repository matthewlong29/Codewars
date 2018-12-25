# 6 kyu

# A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more capitals letters. The 1st letter of a code is the capital letter of the book category. In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

# For example an extract of one of the stocklists could be:

# L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
# or
# L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....

# You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :

#   M = {"A", "B", "C", "W"}
# or
#   M = ["A", "B", "C", "W"] or ...

# and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.

# For the lists L and M of example you have to return the string (in Haskell/Clojure a list of pairs):

#   (A : 20) - (B : 114) - (C : 50) - (W : 0)

# where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.

# If L or M are empty return string is "" (Clojure should return an empty array instead).

# Note:
# In the result codes and their values are in the same order as in M.

def stock_list(b, c):
    bName = []
    bValue = []
    if len(b) == 0 or len(c) == 0:
        return ""
    for art in b:  # split b into name and value
        bValue.append(int(art.split(" ")[1]))
        bName.append(art.split(" ")[0])
    print("bName: {}").format(str(bName))
    print("bValue: {}").format(bValue)
    formattedString = ""
    for i in range(len(c)):
        tempSum = 0
        print("checking {};-----------").format(c[i])
        for j in range(len(b)):
            if bName[j][0] == c[i][0]:
                print("{} is in {}!").format(c[i], bName[j])
                print("bValue[i]: {}").format(bValue[j])
                tempSum += bValue[j]
        formattedString += "({} : {})".format(c[i], tempSum)
        if i < len(c) - 1:
            formattedString += " - "
    print(formattedString)
    return formattedString


if __name__ == "__main__":
    print("-----------------------")
    b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B"]
    stock_list(b, c)  # "(A : 200) - (B : 1140)"
    print("-----------------------")
    d = ['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239', 'DRTYMKH 060']
    e = []
    stock_list(d, e)
