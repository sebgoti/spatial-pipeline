#!/usr/bin/env python 

import os
import numpy as np
import itk
import argparse
import tifffile as tiff

#import registrator

def main(input_dir, param_files, fixed_img, moving_img):
    #print(parameterFiles_list)
    #registrator_object = registrator.Registrator(param_files, moving_img)
    #registrator_object._print_successful()
    param_object = build_parameter_object(input_dir, param_files)
    result_transform_parameters = learn_transform(fixed_img, moving_img, param_object)
    save_transform_parameters(result_transform_parameters, param_files, moving_img)
    #test_build_parameter_object(input_dir)
#input_dir = "/Users/segonzal/Documents/Repositories/nf-training/elastix_parameter_files"

#param_files = [os.path.join(input_dir, f"elastix_parameters_2D.{i}.txt") for i in range(4)]
def test_build_parameter_object(input_dir):
    print(os.listdir(input_dir))
    
def read_image(img_path):
        return itk.imread(img_path, itk.F)



def build_parameter_object(input_dir, parameter_files_str):
    param_list = parameter_files_str.split(',')
    parameter_dict = {k: os.path.join(input_dir, k) for k in param_list}
    print(parameter_dict)
    parameter_object = itk.ParameterObject.New()
    parameter_object.ReadParameterFile(list(parameter_dict.values()))
    #for i, parameter in enumerate(param_list):
    #    parameter_object.WriteParameterFile(parameter_object.GetParameterMap(i), parameter.split('.')[0]+'_result.txt')
    return parameter_object

def learn_transform(fix, mov, param_object):
    result_image, result_transform_parameters = itk.elastix_registration_method(
        read_image(fix),
        read_image(mov),
        parameter_object = param_object,
        log_to_console=False)
    #total_transformations = len(parameter_files)
    #tiff.imwrite('result.tiff', np.asarray(result_image))
    return result_transform_parameters
    

def save_transform_parameters(result_transform_parameters, parameter_files_str, round_id):
    param_list = parameter_files_str.split(',')
    for i, param_file in enumerate(param_list):
        result_transform_parameters.WriteParameterFile(
            result_transform_parameters.GetParameterMap(i),
            f"round_{round_id}_transformation_{i}.txt"
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Variable number of paths for reading ITKElastix files.')
    parser.add_argument('-i', '--input_path', type=str)
    parser.add_argument('-p', '--parameter_files', type=str)
    parser.add_argument('-f', '--fixed_img', help='Path of fixed/reference file')
    parser.add_argument('-m', '--moving_img', help='Path of moving file')
    
    args = parser.parse_args()
    main(args.input_path, 
         args.parameter_files,
         args.fixed_img,
         args.moving_img)
    #test_build_parameter_object(args.input_path)
       
#build_parameter_object(*param_files)
#parameter_object = itk.ParameterObject.New()
#parameter_object.ReadParameterFile()