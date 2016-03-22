poison_trees = 0
poison_tree_limit = 33224202171613280406600885863289624718
trees_cut = 0
day = 1

def get_poison_amount(): #TODO fix this junk to work properly with more than one year
    if (day < 3) or (21 <= (day % 72) <= 36):
        return 0.0
    elif day >= 3:
        return ((30/67) * (day-3) + 3)/100

while poison_trees < poison_tree_limit:
    for i in range (1, 1000001):
        trees_cut += 1
        poison_trees += get_poison_amount()
        if (poison_trees >= 33224202171613280406600885863289624718):
            print ("ANSWER: " + trees_cut)
            input()
    print ("Day " + str(day) + ". " + str(trees_cut) + " trees cut. "
           + str(poison_trees) + " poison trees.")
    day += 1
