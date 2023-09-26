#!/usr/bin/env python3

import os
import argparse

def main(input_dir, parameter_files, fixed_img, moving_img):
    #print(param_files)
    with open('t.txt', 'w') as fh:
        fh.writelines(f"{input_dir} \n {parameter_files} \n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Variable number of paths for reading ITKElastix files.')
    parser.add_argument('-i', '--input_dir', type=str)
    parser.add_argument('-p', '--parameter_files', type=str)
    parser.add_argument('-f', '--fixed_img', help='Path to fixed image', type=str)
    parser.add_argument('-m', '--moving_img', help='Path to moving image', type=str)
    
    args = parser.parse_args()
    main(args.input_dir, args.parameter_files, args.fixed_img, args.moving_img)
    #test_build_parameter_object(args.input_path)
       
#build_parameter_object(*param_files)
#parameter_object = itk.ParameterObject.New()
#parameter_object.ReadParameterFile()
