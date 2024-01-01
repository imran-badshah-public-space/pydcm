import pydicom as dicom, cv2, argparse
import os

"""
Adapted from https://medium.com/@vivek8981/dicom-to-jpg-and-extract-all-patients-information-using-python-5e6dd1f1a07d
"""

def parse_args():
    parser = argparse.ArgumentParser(
        description="DICOM to Image (only JPG for now) converter",
        usage="python3 main.py -i input-path -o output-path")
    parser.add_argument("-i", "--INPUT_PATH", metavar="",
                        required=True, help="Input path for which all dcms will be converted into jpgs")
    parser.add_argument("-o", "--OUTPUT_PATH", metavar="",
                        required=True, help="Output path to store jpgs")
    args = parser.parse_args()
    for arg in vars(args):
        print("{}\t: {}".format(arg, getattr(args, arg)))
    return args

def convertToJPG(args):
    # Specify the .dcm folder path
    folder_path = args.INPUT_PATH
    # Specify the output jpg/png folder path
    jpg_folder_path = args.OUTPUT_PATH
    images_path = os.listdir(folder_path)
    for n, image in enumerate(images_path):
        ds = dicom.dcmread(os.path.join(folder_path, image))
        if n == 1:
            print(ds)
        pixel_array = ds.pixel_array
        normalized_pixel_array = cv2.normalize(pixel_array, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        image = image.replace('.dcm', '.jpg')
        cv2.imwrite(os.path.join(jpg_folder_path, image), normalized_pixel_array)
        if n % 10 == 0:
            print('{} image converted'.format(n))

def main():
    args = parse_args()
    try:
        convertToJPG(args)
    except Exception as e:
        print("Error converting to JPG: " + str(e))
    else:    
        print("Conversion successful")

if __name__ == '__main__':
    main()
