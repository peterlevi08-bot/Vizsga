#1. Feladat
def count_calories(avg_heartbeat, weight, age, duration, gender):
    if hasattr(duration, "any"):
        if (duration < 0).any():
            raise ValueError("A duration nem lehet negatív.")
    elif duration < 0:
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


# 2. Feladat
class Athlete:
    def __init__(self, name, age=18, weight=0, sex=""):
        self.name = name
        self.age = age
        self.weight = weight
        self.sex = sex


# 3. Feladat
import matplotlib.pyplot as plt
import pandas as pd


def show_stats(df):
    plt.plot(df["Nap"], df["Kalória"])
    plt.xlabel("Nap")
    plt.ylabel("Kalória")
    plt.title("Kalóriaégetés")
    plt.show()

#4.Feladat
def main():
    name = input("Név: ")
    age = int(input("Életkor: "))
    weight = float(input("Testsúly: "))
    sex = input("Nem (M/F): ")

    felhasznalo = Athlete(name, age, weight, sex)

    workout_df = pd.read_excel("Workout_Data.xlsx")

    workout_df["Kalória"] = count_calories(
        workout_df["Szívverés(bpm)"],
        felhasznalo.weight,
        felhasznalo.age,
        workout_df["Edzéshossz(perc)"],
        felhasznalo.sex
    )

    show_stats(workout_df)


if __name__ == "__main__":
    main()