from collections import deque

# List of people and rank
list = [
    ("S", "Mary"), ("P", "Dee"), ("P", "Dee"), ("E", "Eileen"), ("E", "Mike"), ("E", "Joe"), ("P", "Dee"),
    ("E", "Vicky"), ("E", "George"), ("P", "Dee"), ("P", "Joe"), ("E", "Sally"), ("P", "Joe"), ("S", "Pete"),
    ("P", "Dee"), ("S", "Bill"), ("S", "Chase"), ("E", "Price"), ("P", "Dee"), ("E", "Sue")
]
# Put into queues
def categorize_packets(list):
    premium = deque()
    standard = deque()
    economy = deque()

    for priority, name in list:
        if priority == "P":
            premium.append(name)

        elif priority == "S":
            standard.append(name)

        elif priority == "E":
            economy.append(name)

    return premium, standard, economy

#WFQ
def wfq(premium, standard, economy):
    while premium or standard or economy:
        for _ in range(3):
            if premium:
                print(f"P {premium.popleft()}")
        for _ in range(2):
            if standard:
                print(f"S {standard.popleft()}")
        for _ in range(1):
            if economy:
                print(f"E {economy.popleft()}")

#
premium, standard, economy = categorize_packets(list)
print("List in order")
wfq(premium, standard, economy)