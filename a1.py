def list_len(list1):
    count = 0
    for i in list1:
        count += 1
    return count


# print(list_len([]))


def list_max(list1):
    largest = 0
    for i in list1:
        if i > largest:
            largest = i
        else:
            continue
    if largest == 0:
        return None
    return largest


# print(list_max([]))


def list_copy(list1):
    list2 = []

    list2 = list1[:]
    list1.remove(3)
    print(list1)
    return list2


l1 = [1, 2, 3, 4]


# print(list_copy(l1))


def list_append(list1, val):
    list2 = list1[:] + [val]
    return list2


# print(list_append([1, 2, 3], 4))


def list_insert(list1, loc, val):
    list2 = list1[:loc]
    list2 += [val]
    list2[loc + 2:] = list1[loc:]
    return list2


# print(list_insert([1, 2, 3, 4], 3, 5))

def list_remove(list1, val):
    for i in range(list_len(list1)):
        if list1[i] == val:
            list2 = list1[:i] + list1[i + 1:]
    print(list1)
    return list2


# print(list_remove([10, 20, 30], 20))


def list_reverse(list1):
    list2 = []
    i = (list_len(list1) - 1)
    while i >= 0:
        list2 += [list1[i]]
        i = i - 1
    return list2


# print(list_reverse([10, 20, 30, 40]))


def products_store():
    product_list = ["soft drink", "onion rings", "small fries"]
    product_stock = [10, 5, 20]
    product_costs = [0.99, 1.29, 1.49]

    while True:
        x = ' ' * 3
        user_input = input("(s)earch for product or (a)dd or (r)emove or (l)ist or (u)pdate or r(e)port or (q)uit: ")
        if user_input == "s":
            user_product = input("Enter a product name: ")
            if user_product not in product_list:
                print("Sorry, we don't sell", user_product)
            else:
                for i in range(len(product_list)):
                    if user_product == product_list[i]:
                        print("We sell", product_list[i], "at", product_costs[i], "per unit.")
                        print("We currently have", product_stock[i], "in stock")
        elif user_input == "l":
            print("Product" + x + "Price" + x + "Quantity")
            for i in range(len(product_list)):
                print(product_list[i] + x + str(product_costs[i]) + x + str(product_stock[i]))
        elif user_input == "q":
            quit()
        elif user_input == "a":
            user_product_add = input("What product do you want to add: ")
            if user_product_add not in product_list:
                user_product_add_price = input("What is the price of " + user_product_add + ": ")
                if float(user_product_add_price) > 0:
                    user_product_add_stock = input("How many to add: ")
                    if float(user_product_add_stock) >= 1:
                        product_list.append(user_product_add)
                        product_stock.append(user_product_add_stock)
                        product_costs.append(user_product_add_price)
                    else:
                        print("Invalid Input")
                else:
                    print("Invalid Input")
            else:
                print("It is already there.")
        elif user_input == "r":
            user_product_remove = input("Which product to remove: ")
            if user_product_remove not in product_list:
                print("Doesnt exist.")
            else:
                for i in range(len(product_list) - 1):
                    if product_list[i] == user_product_remove:
                        product_list.pop(i)
        elif user_input == "u":
            user_update_choice = input("What do you want to update(n), (c) or (q): ")
            if user_update_choice == "n":
                user_name_update_original = input("Which one do you want to update: ")
                if user_name_update_original not in product_list:
                    print("Doesn't exist")
                else:
                    user_name_update_new = input("New name: ")
                    for i in range(len(product_list) - 1):
                        if product_list[i] == user_name_update_original:
                            product_list[i] = user_name_update_new
            elif user_update_choice == "c":
                user_name_update_original = input("Which one do you want to update: ")
                if user_name_update_original not in product_list:
                    print("Doesn't exist")
                else:
                    user_cost_update = input("What is new cost: ")
                    if float(user_cost_update) > 0:
                        for i in range(len(product_list) - 1):
                            if product_list[i] == user_name_update_original:
                                product_costs[i] = user_cost_update
                    else:
                        print("Invalid input")
            elif user_update_choice == "q":
                user_name_update_original = input("Which one do you want to update: ")
                if user_name_update_original not in product_list:
                    print("Doesn't exist")
                else:
                    user_stock_update = input("What is new quantity: ")
                    if float(user_stock_update) > 0:
                        for i in range(len(product_list) - 1):
                            if product_list[i] == user_name_update_original:
                                product_stock[i] = user_stock_update
                    else:
                        print("Invalid input")
            else:
                print("Invalid input.")
        elif user_input == "e":
            largest = 0
            for i in product_costs:
                if i > largest:
                    largest = i
            for i in range(len(product_costs)):
                if largest == product_costs[i]:
                    print("Most expensive product:     " + str(largest) + "(" + product_list[i] + ")")
            smallest = largest
            for i in product_costs:
                if i < smallest:
                    smallest = i
            print(largest)
            for i in range(len(product_costs)):
                if smallest == product_costs[i]:
                    print("Least expensive product:     " + str(smallest) + "(" + product_list[i] + ")")
        else:
            print("Invalid input. Try again")


products_store()


