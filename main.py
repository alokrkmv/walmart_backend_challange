import argparse
from pathlib import Path

from readfile import readfile
from movietheater import movie_theater
from writer import write_to_file
import test_script
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=Path)

    p = parser.parse_args()
    # print(p.file_path, type(p.file_path), p.file_path.exists())
    input_file = open(p.file_path, 'r')
    input_data = readfile.parse_file(input_file)
    # Create the object of Main Class and call the make_reservation function for
    # reserving seats in the theater
    movie_theater_obj = movie_theater.Main(input_data)
    final_reservations = movie_theater_obj.make_reservation()
    # Write the final result to the output file
    write_to_file.writer(final_reservations)
    print("Program executed successfully !!! Please check the output file in the dataset folder")

    print("Running test scripts")
    print("+++++++++++++++++++++++++++++")
    test_script_obj = test_script.TestScript(input_data, final_reservations)
    test_script_obj.run_test()
    print("Test scripts executed successfully")

    
    

    