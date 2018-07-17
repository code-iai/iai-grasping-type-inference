import unittest
import word_net


class WordNetTest(unittest.TestCase):
    def test_should_return_path_similarity_1_between_same_concepts(self):
        similarity = word_net.determine_path_similarity_between_two_concepts('cup.n.01', 'cup.n.01')
        self.assertEqual(similarity, 1.0)


if __name__ == "__main__":
    unittest.main()
