# Rock Paper Scissors

This is the boilerplate for the Rock Paper Scissors project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors


# Attribution

KM, 31.10.2024: I used https://medium.com/@sri.hartini/rock-paper-scissors-in-python-5173ab69ca7a as an inspiration to approach this exercise but copied none of the code. In particular I did not use a static pre-built dictionary with all possible permutations but are creating multiple dictionaries which are filled at run-time with actual opponents moves only. Also I added a (very simple) quorum algorithm instead of just trusting one exact pattern match. I am sure that by adding some more dictionaries for longer pattern patches the performance could increase a bit further but that there will be a turning point at which the performance will degrade