print("Let's see your chances at a few Minnesota universities!")

GPA = float(input("Your unweighted GPA (0.0 to 4.0): "))
while GPA < 0 or GPA > 4.0:
    print("Invalid input. Unweighted GPA must be between 0.0 and 4.0.")
    GPA = float(input("Your unweighted GPA (0.0 to 4.0): "))

ACT = int(input("Your ACT composite (1 to 36): "))
while ACT < 1 or ACT > 36:
    print("Invalid input. ACT must be between 1 and 36.")
    ACT = int(input("Your ACT composite (1 to 36): "))

print("\na. Carleton College")
print("b. Minnesota State Mankato")
print("c. St. Thomas")
print("d. UMN Twin Cities - CLA")
print("e. UMN Twin Cities - CSE")
colleges = input("Which universities are you applying to? Type letters like a or a,c,e: ").lower()


def rate(score, low, high):
    if score < low:
        return "Reach"
    elif score <= high:
        return "Match"
    else:
        return "Likely"


def show(name, act_low, act_high, gpa_low=None, gpa_high=None):
    act_fit = rate(ACT, act_low, act_high)
    print("\n" + name)
    print("  ACT:", act_fit, "(middle 50%:", act_low, "-", str(act_high) + ")")
    if gpa_low is not None:
        gpa_fit = rate(GPA, gpa_low, gpa_high)
        print("  GPA:", gpa_fit, "(middle 50%:", gpa_low, "-", str(gpa_high) + ")")
        order = ["Reach", "Match", "Likely"]
        overall = order[min(order.index(act_fit), order.index(gpa_fit))]
    else:
        print("  GPA: no published range")
        overall = act_fit
    print("  Overall:", overall)


if "a" in colleges:
    show("Carleton College", 32, 35)
if "b" in colleges:
    show("Minnesota State Mankato", 21, 25)
if "c" in colleges:
    show("St. Thomas", 23, 29, 3.3, 4.0)
if "d" in colleges:
    show("UMN Twin Cities - CLA", 26, 32, 3.37, 3.87)
if "e" in colleges:
    show("UMN Twin Cities - CSE", 29, 34, 3.62, 4.00)

print("\nThese are only predictions based off average data from the students who got in.")