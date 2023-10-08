interpolate.py does frame interpolation by blending frames together, it'd be more accurate to call it onionskin.py but oh well

matrix.py and prompability.py both use the prompts folder to gather results from txt files that have the format "(term1:weight), (term2:weight), (term3:weight)" as printed by interrogating deepbooru. ensure that you save each images' interrogation as a separate text file in prompts directory

mp4.py does a simple resize and append on images in a directory and turns it into an mp4. it's best to go in and change the settings to your desired form

makevid.bat and makevid.py work together to write a gif and mp4 file of the desired video at the desired resolution from a subdirectory to combine all images based on the value stored by their name. maketiled is similar but instead of changing the bat file, you need to modify the python file and it outputs a tiled video, it is suggested to understand the math before trying to modify this one







The HTML documents numbers and text:

Numbers generates a linear stepover for values between one number and the next with the stepover determining how many terms should be inbetween.







Text.html is a number pair generating javascript enabled document, it has complex operation methods so in order to describe it, I need to explain the mathematics mistakes I made along the way.

If you mess up and delete any of the terms not at the exact end of the created terms, you have to refresh and do it all again

The way it generates is it will place a number after the term, which means that in a prompt search and replace file you will want to use it in a stable diffusion animation where you don't need to control anything drastically. the format for the terms you would likely use would be something like this:

(sampletext:
) (sampletext:
) you can also add text here that won't be affected by the weights directly (sampletext:


...etc, while at the end it may add a comma on its own, it is best to use the separator text field at the bottom of the page something like this:


enter separator character:

),
or
>,

(for ending on a LORA)

there is the choice to use anything that uses weights such as LORAs which can be added inline like this:

) <lora:exampletext:
> <lora:exampletext:
> (exampletext:


notice that each proceeding line you start off with the character used to end the pair started on the preceeding one

If you mess up and delete any of the terms not at the exact end of the created terms, you have to refresh and do it all again

while keeping the separator the same works usually, this gets boring sometimes, always having to use prompts without commas with this script, so I recently discovered you can add these as the separator in order to circumvent the issue:


enter separator character:

)","
or
>","

and with that any commas without quotation marks surrounding them will be ignored by the prompt s/r in automatic 1111.

this is so far not anything compared to the math you need to do in order for it to generate anything useful..........

Here there be Dragons, wear your HazMat

The math is fairly straightforward, you divide up the length of the animation you want and then do a bit of math in order to get it to print what you want at the correct weights.

but how do you do that? what do the numbers mean? what's the frequency, kenneth? look at me, I am the captain now.


The way to get organized information out of this is math, I may have created a monster that requires seemingly arbitrary numbers in order to function but it is fairly straightforward. you start by determining the height (HGT) and amplitude (AMP) of the graph you want to make, generally it is best to start off with reccomended settings for LORA, reflecting the numbers the creators suggest, averaging them, and plugging in the resulting height and amplitude into the respective parts of the plotter, I may have not mentioned it earlier but if you mess up and delete any of the terms not at the exact end of the created terms, you have to refresh and do it all again.

for terms it is best to set the height to 1, the amplitude to less than 1, the frequency to less than .5 and the position is part of the speed guide I am going to provide now:

3600 frames:180 to shift 1 frame
totaling to a divisor in the pos
648000

the frequency for the phase 3600
100%:
.000555555555555555555555

50%:
.001122192524354102285098

33.33%
.001666666666666666666667

1200 frames:60 to shift 1 frames
totaling to a divisor in the pos
72000

the frequency for the phase 1200

100%
.001666666666666666666667

300:15
4500

100%
.006666666666666666666667

you may notice a shared concept that the divisor is equal to the stepover times the total frames, when using the position, you can use any arbitrary number in that but if you want to start everything at the cosine positions you divide the position divisor by 4 or 4/3 (multiply by 3/4), the script always starts at the neutral positionin the sine wave at 0 position.

you may have noticed that the frequency gets smaller the more frames you have, but what if you don't want an animation with just one frequency?

you multiply! if you want whole numbers of constituent freqs, you should multiply by whole numbers but you don't need to. in fact, you don't need to have frames match up with the base frequency at all, but I highly advise you do in order to use the intended purpose of generating a looping animation.

so .5 frq will generate a 4 term repeating animation, this will help demonstrate that the separation is wholely dependent on the number of frames, since 4 is the bare minimum to get a full phase, it is only fitting that it requires a position of 0.2 in order to advance 1 frame. 40 terms, however, require a frequency of .05 and a position of 2 in order to advance a frame, so you can guess what kind of pattern that will follow.