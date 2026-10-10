import pytest

from workout_statistics import count_calories


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
    with pytest.raises(ValueError):
        count_calories(140, 80, 30, -10, "M")


def test_count_calories_zero_duration():
    result = count_calories(140, 80, 30, 0, "M")

    assert result == 0