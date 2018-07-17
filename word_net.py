from prac.core.wordnet import WordNet

__word_net__ = WordNet()


def determine_path_similarity_between_two_concepts(a, b):
    return __word_net__.similarity(a, b, 'path')
