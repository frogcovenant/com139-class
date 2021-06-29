# Challenges
## Jos Stan's 2D Fluid Simulator
My first issue was understanding the code that was given to me. Since I couldn't understand the mathematical processes in the Jos Stan document, I decided to look for a video [sources](https://www.youtube.com/watch?v=alhpH6ECFvQ) and read a much simpler [document](https://mikeash.com/pyblog/fluid-simulation-for-dummies.html)

## Reading the data
At first I wasn't sure how to give the required arguments for the fluid animation to work. It took me some trial and error, researching and asking other students but I finally came up with an input file, that would let me pass the requirements needed (sources for velocity and density, as well as its corresponding values). Although I'm not familiar with JSON files, using them made it much easier for me to understand the relation of velocity with it's position and direction and the relation with the position of the color as well as its density.

## Object presence
This challenge was impossible for me to solve. Here's how I went around the problem:
1. I added new values in the JSON file for the new dictionary that would contain everything needed for creating an object. First I wanted to try a simple box object.
2. In order to check wheter my object was correctly placed on the grid, I added some color to it.

![box](https://github.com/frogcovenant/com139-class/blob/ss/Fluid_Sim/box_img.png "Box in grid")

3. Once I confirmed that it was placed properly, I tried calling the function responsible for setting boundaries and adding this box as one, however the result was unsatisfactory
![failure](https://github.com/frogcovenant/com139-class/blob/ss/Fluid_Sim/no_object.gif "No presence of the object")
