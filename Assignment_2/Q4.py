#input function 
def get_input(list_name):
    num = []
    print(f"\n--- Enter integers for {list_name} (or q to quit) ---")
    while True:
        urs_inp = input("> ") 
        if urs_inp.lower() == 'q':
            break

        try:
            val = int(urs_inp)
            num.append(val)
        except ValueError:
            print("Please enter a valid integer.")
    return num 
#function call 
list_1 = get_input("List 1")
list_2 = get_input("List 2")
list_3 = get_input("List 3")
#addint all list to a superlist 

all_lists = [list_1, list_2, list_3]

list_num = 1 
for sub_list in all_lists:
    dis = {}

    for n in sub_list:
        if n in dis:
            dis[n] += 1
        else:
            dis[n] = 1
        
    print(f"\n--- Results for List {list_num} ---")
    print(f"You entered: {sub_list}")
    print(f"Occurrences: {dis}")

    list_num += 1