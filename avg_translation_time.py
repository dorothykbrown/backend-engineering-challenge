import json
from datetimerange import DateTimeRange
from datetime import timedelta, datetime

class AverageTranslationTime:

    def calculate_avg_translation_time(input_file_name: str):
        file = open(input_file_name)
        translations = json.load(file)


        start_time = datetime.strptime(translations[0]["timestamp"], '%Y-%m-%d %H:%M:%S.%f').replace(second=0, microsecond=0)
        
        end_time = datetime.strptime(translations[-1]["timestamp"], '%Y-%m-%d %H:%M:%S.%f').replace(second=0, microsecond=0)

        # import pdb
        # pdb.set_trace()
        time_range = DateTimeRange(start_time, end_time + timedelta(minutes=1))

        results = []

        for minute in time_range.range(timedelta(seconds=60)):
            ten_min_window_time_range = DateTimeRange(minute - timedelta(minutes=10), minute)
            delivery_times_in_range = [
                int(translation["duration"]) 
                for translation in translations 
                if datetime.strptime(translation["timestamp"], '%Y-%m-%d %H:%M:%S.%f') in ten_min_window_time_range
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

    def calculate_avg_delivery_time(delivery_times: list) -> float:
        return sum(delivery_times)/len(delivery_times)

    

if __name__ == "__main__":
    AverageTranslationTime.calculate_avg_translation_time(input_file_name="input.json")