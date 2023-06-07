from evolutionary_algorithm import EvolutionaryAlgorithm
from preprocess_utils import get_data


def main():
    features, labels = get_data(False)
    evolutionary_algorithm = EvolutionaryAlgorithm(5, 10, 6, 1, 1, 2, 1.5, features, labels)
    evolutionary_algorithm.run()


if __name__ == '__main__':
    main()
