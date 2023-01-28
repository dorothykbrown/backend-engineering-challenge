import unittest
from avg_translation_time import AverageTranslationTime

class TestAverageTranslationTime(unittest.TestCase):
    def test_calculate_avg_delivery_time(self):
        delivery_times = [10, 20, 30, 45]

        average = AverageTranslationTime.calculate_avg_delivery_time(delivery_times)
        expected_average = sum(delivery_times)/len(delivery_times)

        self.assertEqual(average, expected_average, "average is not as expected")

    def test_calculate_avg_delivery_time_empty_list(self):
        delivery_times = []

        average = AverageTranslationTime.calculate_avg_delivery_time(delivery_times)

        self.assertEqual(average, None, "average is not None")

    def test_format_translation_results(self):
        pass

    def test_convert_string_to_datetime(self):
        pass
    
    def test_calculate_avg_translation_time(self):
        pass

if __name__ == '__main__':
    unittest.main()