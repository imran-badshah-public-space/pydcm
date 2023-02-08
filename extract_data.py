import pydicom as dicom, argparse
import os
import logger
from tabulate import tabulate

def parse_args():
    parser = argparse.ArgumentParser(
        description="Extracts data from the first slice",
        usage="python3 extract_data.py -i input/case6 -s -u")
    parser.add_argument("-i", "--INPUT_PATH", metavar="",
                        required=True, help="Input path for which data of the first dcm will be extracted")
    parser.add_argument("-u", "--STUDY_INSTANCE_UID", metavar="", action=argparse.BooleanOptionalAction,
                        required=False, help="include this for specifically extracting Study Instance UID Attribute")
    parser.add_argument("-s", "--SERIES_INSTANCE_UID", metavar="", action=argparse.BooleanOptionalAction,
                        required=False, help="include this for specifically extracting Series Instance UID Attribute")
    parser.add_argument("-g", "--GROUP", metavar="", action=argparse.BooleanOptionalAction,
                        required=False, help="Group by Study Instance UID Attribute")

    args = parser.parse_args()
    for arg in vars(args):
        logger.black("{}\t: {}".format(arg, getattr(args, arg)))
    print('')
    return args

def print_data(target_path, specific_extracts):
    logger.info("\nprinting for " + target_path + "\n")
    ds = dicom.dcmread(target_path)
    for specific in specific_extracts:
        if specific == 'STUDY_INSTANCE_UID':
            print(ds[0x0020, 0x000D])
        if specific == 'SERIES_INSTANCE_UID':
            print(ds[0x0020, 0x000E])
    if len(specific_extracts) == 0:
        print(ds)

def construct_specific_extracts(args):
    specific_extracts = []
    if (args.STUDY_INSTANCE_UID):
        specific_extracts.append('STUDY_INSTANCE_UID')
    if (args.SERIES_INSTANCE_UID):
        specific_extracts.append('SERIES_INSTANCE_UID')
    return specific_extracts

def extract_data(args):
    # Specify the .dcm folder path
    input_path = args.INPUT_PATH
    specific_extracts = construct_specific_extracts(args)
    if (os.path.isdir(input_path)):
        for root, _dirs, files in os.walk(input_path):
            for name in files:
                print_data(os.path.join(root, name), specific_extracts)
    else:
        print_data(input_path, specific_extracts)        

def update_group(table_dict, target_path):
    ds = dicom.dcmread(target_path)
    try:
        table_dict[ds[0x0020, 0x000D][:]][0] += 1
        table_dict[ds[0x0020, 0x000D][:]][1].extend([target_path])
    except:
        table_dict[ds[0x0020, 0x000D][:]] = [1, [target_path]]
    return table_dict
     
"""
table:
study-uuid  |   occurances  |   file_path
"""
def group_data(args):
    input_path = args.INPUT_PATH
    
    table_dict = {}
    table = []
    headers = ["study-uuid", "occurances", "file_path"]

    if (os.path.isdir(input_path)):
        for root, _dirs, files in os.walk(input_path):
            for name in files:
                target_path = os.path.join(root, name)
                table_dict = update_group(table_dict, target_path)
    else:
        table_dict = update_group(table_dict, input_path)
    
    print("table_dict: ", table_dict)
    table = [ [k, table_dict.get(k)[0], '\n'.join(table_dict.get(k)[1])] for k in table_dict.keys() ]
    print(tabulate(table, headers, tablefmt="simple_grid"))

def main():
    args = parse_args()
    try:
        if (args.GROUP):
            group_data(args)
        else:
            extract_data(args)
    except Exception as e:
        logger.error("\nError extracting data: " + str(e))
    else:    
        logger.success("\nExtraction successful")

if __name__ == '__main__':
    main()
