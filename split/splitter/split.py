import random

def split(items, ratios):
     a=[]
     s = []
     s.extend(items)
     for i in range(len(ratios)):
        x = round((ratios[i])*len(items))
        selected = random.sample(s, x)
        for item in selected:
            s.remove(item)
        a.insert(i, selected)
     return a

def get_valid_ratios(items):
    while True:
        ratios_str = input("Enter ratios separated by space: ")
        ratios = [float(ratio) for ratio in ratios_str.split()]
        if sum(ratios) == 1:
            if len(ratios) < len(items):
                print(ratios)
                return ratios
            else:
                print("Error: The length of ratios list must be lesser than length of items list. Please enter valid ratios.")
        else:
            print("Error: The sum of ratios must be equal to 1. Please enter valid ratios.")

def main():
    items_str = input("Enter items separated by space: ")
    items = [int(item) for item in items_str.split()]
    print(items)
    # Get valid ratios from the user
    valid_ratios = get_valid_ratios(items)
    result = split(items, valid_ratios)
    print("the output will be:\n",result)


if __name__ == '__main__':
    main()