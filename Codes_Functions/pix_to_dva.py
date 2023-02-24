from math import atan2, degrees
#### Arguments
# h = 19           # Monitor height in cm
# d = 57           # Distance between monitor and participant in cm
# r = 1080 #1920x1080          # Vertical resolution of the monitor
# size_in_px = 100 # The stimulus size in pixels
## Calculate the number of degrees that correspond to a single pixel. This will
## generally be a very small value, something like 0.03.
# deg_per_px = degrees(atan2(.5 * h, d)) / (.5 * r)
# print(f'{deg_per_px} degrees correspond to a single pixel')
## Calculate the size of the stimulus in degrees
# size_in_deg = size_in_px * deg_per_px
# print(f'The size of the stimulus is {size_in_px} pixels and {size_in_deg} visual degrees')
# History
# Omer Faruk Yildiran 11 2022
# ENS-PSL LSP 

def pix_to_dva(size_in_pix=100,h=19,d=57,r=1080):
    # Calculate the number of degrees that correspond to a single pixel. This will
    # generally be a very small value, something like 0.03.
    deg_per_px = degrees(atan2(.5 * h, d)) / (.5 * r)
    print(f'{deg_per_px} degrees correspond to a single pixel')
    # Calculate the size of the stimulus in degrees
    size_in_deg = size_in_pix * deg_per_px
    return size_in_deg