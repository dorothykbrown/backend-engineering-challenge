import json
import sys
from typing import Optional
from datetimerange import DateTimeRange
from datetime import timedelta, datetime
import argparse

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

        output_file = open("output_test.json", "w")
        json.dump(results, output_file)
        
        file.close()
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
    parser = argparse.ArgumentParser(
        prog="AverageTranslationTime",
        description="Calculates the average translation time within the specified window of time",
        epilog="And that's how you'd calculate the average translation time with a sliding window!"
    )

    # unbabel_cli --input_file events.json --window_size 10
    parser.add_argument("--input_file", dest="input_file", nargs=1, required=True, help="The input file with translation stream in JSON format")
    parser.add_argument("--window_size", dest="window_size", nargs=1, type=int, required=True, help="The size of the time window in minutes")
    
    args = parser.parse_args(sys.argv[1:])
    [input_file_name] = args.input_file
    [window_size] = args.window_size

    AverageTranslationTime.calculate_avg_translation_time(
        input_file_name=input_file_name,
        window_size=window_size
    )