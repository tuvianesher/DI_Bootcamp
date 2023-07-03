interpolate.py does frame interpolation by blending frames together, it'd be more accurate to call it onionskin.py but oh well

matrix.py and prompability.py both use the prompts folder to gather results from txt files that have the format "(term1:weight), (term2:weight), (term3:weight)" as printed by interrogating deepbooru. ensure that you save each images' interrogation as a separate text file in prompts directory

mp4.py does a simple resize and append on images in a directory and turns it into an mp4. it's best to go in and change the settings to your desired form