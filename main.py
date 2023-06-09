from fuzzy_system.enums import Features
from fuzzy_system.linguistic_variable import LinguisticVariable


def main():
    pass
    # fuzzy_system_config.X, fuzzy_system_config.Y = get_data(False)
    # evolutionary_algorithm = EvolutionaryAlgorithm(5, 10, 6, 0, 0, 2)
    # evolutionary_algorithm.run()
    # evolutionary_algorithm.show_statistics()


if __name__ == '__main__':

    Features.TWO.min_value = 0
    Features.TWO.max_value = 100
    var = LinguisticVariable.random_linguistic_variable(Features.TWO)
    var.plot()