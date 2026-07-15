def describe_habit(name, **kwargs):
    print(f"Habit: {name}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

describe_habit("Біг", frequency="щодня", duration="30 хв", streak=5)