# BUILD BURGER SIM!

## Demo
Demo Video: <https://youtu.be/b10PtrTKB40>

## GitHub Repository
GitHub Repo: <https://github.com/OllieCarson/final_project.git>

## Description
Build Burger Sim is a burger making game about trying to support yourself while trying to follow your dreams. 
Also about how the industry isn't doing too well, and how the majority will struggle to find jobs.

My coding took a lot of trial and error, and deleting big chunks of code when something didn't work out.
I even had to change some of my goals as I could not figure out how to achieve them. 

AS it stands, my code functions like this: randomly generate a series of 6 ingredient images from the receipt subfolder and place them on the order ticket.
Each ingredient on the order ticket corresponds to the same ingredient in the burger_build folder, excluding the top bun.
The full size ingredient goes along the top of the screen until the space bar is pressed, then it falls onto the bottom buns hit box.
this is repeated 6 times before the top bun is spawned, Originally I tried to make it so the top bun could be spawned before that with it just being a max of 6, but after hours of trying to make that work, I decided that it always being 6 was fine.
After the top bun spawns, it pauses and then goes to the next round, with the "art fund" jar being slightly fuller. Orginally, I wanted to give a score depending on how it was compared to "the perfect burger" and give the money based on that, but that was too complex to successfully implement for my level. So now it progresses as the burger is built.
There are 5 stages of jar progression, and once it reaches the final stage, the game ends.

All of the images in the project were made by me, and the ones not in subfolders are there to be more easily called and not included in the randomization.

If I were to start this project again I'd say to reel in the scope a tad for being such a beginner. I have coded larger projects in the past, but it was through programs like Unity that took care of much of the heavy lifting. I am not a very good skilled programmer.