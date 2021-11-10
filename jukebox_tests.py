import unittest
from jukebox import genre
class jukebox_tests(unittest.TestCase):
    def test_genre(self):
        self.assertEqual(genre("Hip-Hop"), "You chose Hip-Hop as your favorite genre!")
        self.assertEqual(genre("Hip Hop"), "Sorry, you must enter Hip-Hop, R & B, Pop, or Country. Try Again!")
        self.assertEqual(genre("R&B"), "You chose R&B as your favorite genre!")
        self.assertEqual(genre("country"), "Sorry, you must enter Hip-Hop, R & B, Pop, or Country. Try Again!")
        self.assertEqual(genre("Pop"), "You chose Pop as your favorite genre!")

if __name__ == "__main__":
    unittest.main()