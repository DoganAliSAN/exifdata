#Learning Project - This code fist defines a function named view_exif that takes a file path as an input and prints out the EXIF metadata of the image file, including the GPS location if available. The user is prompted to enter the file path when the code is executed.
#DALIS

import pip 
pip.main(["install","exifread"])

import exifread
def view_exif(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                print(f"{tag:25}: {tags[tag]}")
        if 'GPS GPSLatitude' in tags.keys() and 'GPS GPSLongitude' in tags.keys():
            latitude = tags['GPS GPSLatitude'].values
            latitude_ref = tags['GPS GPSLatitudeRef'].values
            longitude = tags['GPS GPSLongitude'].values
            longitude_ref = tags['GPS GPSLongitudeRef'].values
            latitude = exifread.utils.dec_deg(latitude)
            longitude = exifread.utils.dec_deg(longitude)
            if latitude_ref.printable == 'S':
                latitude = -latitude
            if longitude_ref.printable == 'W':
                longitude = -longitude
            print(f"Location: {latitude}, {longitude}")

file_path = input("Enter the file path: ")
view_exif(file_path)
