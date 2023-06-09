from fuzzy_system import fuzzy_system_config
from evolutionary_algorithm import EvolutionaryAlgorithm
from fuzzy_system.enums import Features
from fuzzy_system.linguistic_variable import LinguisticVariable
from fuzzy_system.rule import Rule
from preprocess_utils import get_data


def main():
    # fuzzy_system_config.X, fuzzy_system_config.Y = get_data(False)
    Features.TWO.min_value = 0
    Features.TWO.max_value = 100
    var = LinguisticVariable.random_linguistic_variable(Features.TWO)
    var.plot()

    # evolutionary_algorithm = EvolutionaryAlgorithm(5, 10, 6, 0, 0, 2)
    # evolutionary_algorithm.run()
    # evolutionary_algorithm.show_statistics()


if __name__ == '__main__':
    main()
