To run this code enter the name of the input file and desired window size into the command line in the following format:

python3 avg_translation_time.py --input_file input.json --window_size 10

There is also a --help argument that can be used as follows:

python3 avg_translation_time.py --help

If you'd like to use an input file other than the one provided in this repository, just fork this repository and add the desired input file to the project directory and run the command above with the desired input arguments.

To run tests, you can run the following command from the command line:

python3 test_avg_translation_time.py 

Note: The test_calculate_avg_translation_time test function uses the translation stream in the "input.json" file, specifies a 10 minute window and compares the output to the expected results in "expected_output_test.json", so please do not edit either of these files.