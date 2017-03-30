Intro:
	This project I made as a short final project for my High School astronomy class. The idea was to make a program that could detect stars with exoplanets using Kepler's api. I created the algorithm to find them using high school level astronomy so the results are not scientifically conclusive. 

Skills Exhibited:
-Python
-API Handling
-Data Analysis

How It Works:
	First a list of Kepler objects of interest are fetched from the Kepler api. A Kepler object of interest or koi is a star that Kepler has sufficient data on. The program then takes averages of the light output from the star. Finally it checks if there is a significant dip in light at any light measurement compared to the average. If there is one it is possible a planet passed between Kepler and the star, dropping the light output. The id# of stars where this happens is then printed into the console.