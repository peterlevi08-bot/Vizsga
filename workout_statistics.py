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

def test_count_calories_male():
    result = count_calories(140, 80, 30, 60, "M")
    expected = (
        (-55.0969 + (0.6309 * 140) + (0.1988 * 80) + (0.2017 * 30))
        / 4.184
    ) * 60

    assert result == expected


def test_count_calories_female():
    result = count_calories(140, 60, 30, 60, "F")
    expected = (
        (-20.4022 + (0.4472 * 140) - (0.1263 * 60) + (0.0740 * 30))
        / 4.184
    ) * 60

    assert result == expected


def test_count_calories_negative_duration():
    try:
        count_calories(140, 80, 30, -10, "M")
        assert False
    except ValueError:
        assert True


def test_count_calories_zero_duration():
    result = count_calories(140, 80, 30, 0, "M")

    assert result == 0