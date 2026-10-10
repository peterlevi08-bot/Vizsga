#1. Feladat
def count_calories(avg_heartbeat, weight, age, duration, gender):
    if duration < 0:
        raise ValueError("A duration nem lehet negatív.")

    if gender == "M":
        calories = (
            (-55.0969 +
             (0.6309 * avg_heartbeat) +
             (0.1988 * weight) +
             (0.2017 * age))
            / 4.184
        ) * duration


    elif gender == "F":
        calories = (
            (-20.4022 +
             (0.4472 * avg_heartbeat) -
             (0.1263 * weight) +
             (0.0740 * age))
            / 4.184
        ) * duration

    else:
        raise ValueError("A gender csak 'M' vagy 'F' lehet.")

    return calories

#2.Feladat
class Athlete:
    def __init__(self, name, age=18, weight=0, sex=""):
        self.name = name
        self.age = age
        self.weight = weight
        self.sex = sex

import matplotlib.pyplot as plt

#3. feladat
def show_stats(df):
    plt.plot(df["Nap"], df["Kalória"])
    plt.xlabel("Nap")
    plt.ylabel("Kalória")
    plt.title("Kalóriaégetés")
    plt.show()