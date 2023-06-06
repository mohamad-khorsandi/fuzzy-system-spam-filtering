import numpy as np

# define input variables
temperature = np.arange(0, 101, 1)
humidity = np.arange(0, 101, 1)

# define output variable
fan_speed = np.arange(0, 101, 1)


# define membership functions for input variables
def temp_cold(x):
    if x <= 0 or x >= 50:
        return 0
    elif x < 25:
        return (x - 0) / (50 - 0)
    else:
        return (50 - x) / (50 - 25)


def temp_warm(x):
    if x <= 0 or x >= 100:
        return 0
    elif x < 50:
        return (x - 0) / (50 - 0)
    else:
        return (100 - x) / (100 - 50)


def temp_hot(x):
    if x <= 50 or x >= 100:
        return 0
    elif x < 75:
        return (x - 50) / (100 - 50)
    else:
        return (100 - x) / (100 - 75)


def hum_low(x):
    if x <= 0 or x >= 50:
        return 0
    elif x < 25:
        return (x - 0) / (50 - 0)
    else:
        return (50 - x) / (50 - 25)


def hum_medium(x):
    if x <= 0 or x >= 100:
        return 0
    elif x < 50:
        return (x - 0) / (50 - 0)
    else:
        return (100 - x) / (100 - 50)


def hum_high(x):
    if x <= 50 or x >= 100:
        return 0
    elif x < 75:
        return (x - 50) / (100 - 50)
    else:
        return (100 - x) / (100 - 75)


# define membership functions for output variable
def fan_slow(x):
    if x <= 0 or x >= 50:
        return 0
    elif x < 25:
        return (x - 0) / (50 - 0)
    else:
        return (50 - x) / (50 - 25)


def fan_medium(x):
    if x <= 0 or x >= 100:
        return 0
    elif x < 50:
        return (x - 0) / (50 - 0)
    else:
        return (100 - x) / (100 - 50)


def fan_fast(x):
    if x <= 50 or x >= 100:
        return 0
    elif x < 75:
        return (x - 50) / (100 - 50)
    else:
        return (100 - x) / (100 - 75)


# define rules
def rule1(temp, hum):
    return np.fmin(temp_cold(temp), hum_low(hum))


def rule2(temp, hum):
    return np.fmin(temp_cold(temp), hum_medium(hum))


def rule3(temp, hum):
    return np.fmin(temp_warm(temp), hum_high(hum))


def rule4(temp, hum):
    return np.fmin(temp_hot(temp), hum_medium(hum))


# apply rules to input variables
activation1 = rule1(60, 30)  # activate rule 1 with temp=60 and hum=30
activation2 = rule2(60, 70)  # activate rule 2 with temp=60 and hum=70
activation3 = rule3(80, 80)  # activate rule 3 with temp=80 and hum=80
activation4 = rule4(90, 50)  # activate rule 4 with temp=90 and hum=50

# aggregate rule activations
aggregate = np.fmax(activation1, np.fmax(activation2, np.fmax(activation3, activation4)))

# defuzzify to get crisp output
fan_speed_crisp = (np.sum(aggregate * fan_speed)) / (np.sum(aggregate))

print("Fan speed (crisp):", fan_speed_crisp)
