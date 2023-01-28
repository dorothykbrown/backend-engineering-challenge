import json
import unittest
from datetime import datetime
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

        unformatted_translations = [
            {
                "timestamp": "2018-12-26 18:11:08.509654",
                "translation_id": "5aa5b2f39f7254a75aa5",
                "source_language": "en",
                "target_language": "fr",
                "client_name": "easyjet",
                "event_name": "translation_delivered",
                "nr_words": "30",
                "duration": "20"
            },
            {
                "timestamp": "2018-12-26 18:15:19.903159",
                "translation_id": "5aa5b2f39f7254a75aa4",
                "source_language": "en",
                "target_language": "fr",
                "client_name": "easyjet",
                "event_name": "translation_delivered",
                "nr_words": "30",
                "duration": "31"
            }
        ]
        
        formatted_translations = AverageTranslationTime.format_translation_results(unformatted_translations)
        
        expected_formatted_translations = [
            {
                "timestamp": datetime(year=2018, month=12, day=26, hour=18, minute=11, second=8, microsecond=509654),
                "translation_id": "5aa5b2f39f7254a75aa5",
                "source_language": "en",
                "target_language": "fr",
                "client_name": "easyjet",
                "event_name": "translation_delivered",
                "nr_words": "30",
                "duration": 20
            },
            {
                "timestamp": datetime(year=2018, month=12, day=26, hour=18, minute=15, second=19, microsecond=903159),
                "translation_id": "5aa5b2f39f7254a75aa4",
                "source_language": "en",
                "target_language": "fr",
                "client_name": "easyjet",
                "event_name": "translation_delivered",
                "nr_words": "30",
                "duration": 31
            }
        ]

        self.assertEqual(
            formatted_translations,
            expected_formatted_translations,
            "formatted translations are not as expected"
        )

    def test_convert_string_to_datetime(self):
        datetime_str = "2018-12-26 18:15:19.903159"
        datetime_object = AverageTranslationTime.convert_string_to_datetime(datetime_str)
        expected_datetime_object = datetime(year=2018, month=12, day=26, hour=18, minute=15, second=19, microsecond=903159)
        
        self.assertEqual(
            datetime_object,
            expected_datetime_object,
            "datetime object is not as expected"
        )
    
    def test_calculate_avg_translation_time(self):
        AverageTranslationTime.calculate_avg_translation_time(
            input_file_name="input.json", 
            window_size=10
        )

        output_file = open("output_test.json")
        avg_translation_times = json.load(output_file)

        expected_output_file = open("expected_output_test.json")
        expected_avg_translation_times = json.load(expected_output_file)
        
        self.assertEqual(
            avg_translation_times,
            expected_avg_translation_times,
            "avg_translation_times are not as expected"
        )

        output_file.close()
        expected_output_file.close()

if __name__ == '__main__':
    unittest.main()