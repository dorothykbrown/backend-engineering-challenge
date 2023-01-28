import json
from typing import Optional
from datetimerange import DateTimeRange
from datetime import timedelta, datetime

class AverageTranslationTime:

    def calculate_avg_translation_time(input_file_name: str, window_size: int):
        file = open(input_file_name)
        translations = json.load(file)

        formatted_translations = AverageTranslationTime.format_translation_results(translations)

        start_time = formatted_translations[0]["timestamp"].replace(second=0, microsecond=0)
        
        end_time = formatted_translations[-1]["timestamp"].replace(second=0, microsecond=0)

        time_range = DateTimeRange(start_time, end_time + timedelta(minutes=1))

        results = []

        for minute in time_range.range(timedelta(seconds=60)):
            ten_min_window_time_range = DateTimeRange(minute - timedelta(minutes=window_size), minute)
            delivery_times_in_range = [
                translation["duration"]
                for translation in translations 
                if translation["timestamp"] in ten_min_window_time_range
            ]

            avg_delivery_time = 0

            if len(delivery_times_in_range) > 0:
                avg_delivery_time = AverageTranslationTime.calculate_avg_delivery_time(delivery_times_in_range)
            
            results.append(
                {
                    "date": datetime.strftime(minute, "%Y-%m-%d %H:%M:%S"),
                    "average_delivery_time": avg_delivery_time,
                }
            )

        output_file = open("output_file_test.json", "w")
        json.dump(results, output_file)
        
        output_file.close()

    def calculate_avg_delivery_time(delivery_times: list) -> Optional[float]:
        
        if len(delivery_times) < 1:
            return None

        return sum(delivery_times)/len(delivery_times)

    def format_translation_results(translations: list) -> list:
        
        for unformatted_translation in translations:
            unformatted_timestamp = unformatted_translation["timestamp"]
            unformatted_duration = unformatted_translation["duration"]
            unformatted_translation["timestamp"] = AverageTranslationTime.convert_string_to_datetime(unformatted_timestamp)
            unformatted_translation["duration"] = int(unformatted_duration)
        
        return translations
    
    def convert_string_to_datetime(datetime_str: str) -> datetime:
        
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')

if __name__ == "__main__":
    AverageTranslationTime.calculate_avg_translation_time(input_file_name="input.json")