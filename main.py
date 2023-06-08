from fuzzy_system import fuzzy_system_config
from evolutionary_algorithm import EvolutionaryAlgorithm
from preprocess_utils import get_data


def main():
    fuzzy_system_config.X, fuzzy_system_config.Y = get_data(False)
    evolutionary_algorithm = EvolutionaryAlgorithm(5, 10, 6, 0, 0, 2)
    evolutionary_algorithm.run()
    evolutionary_algorithm.show_statistics()


if __name__ == '__main__':
    main()
