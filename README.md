# Using Machine Learning to Predict the fire resistance of a building.
## Overview:
This project uses machine learning to predict the 
fire resistance of a building based on various features like building 
type, number of floors, wall type, construction material, and more. The 
goal is to provide predictions that help in the design and safety of 
buildings.

## Features:
- Building Type: Residential or Commercial
- Number of Floors
- Wall Type: Single or Double wall
- Area: Size of the building
- Construction Material: Concrete, Steel, Timber
- Paint Type: Fire-resistant or Standard paint
and others...

## Approach:
- Data Collection: The dataset includes features such as building type, number of floors, construction 
material, and fire resistance time (in hours).
- Preprocessing: Categorical variables are encoded, and data is scaled for machine learning models.
- Model: A Random Forest model is used to predict fire resistance based on the features.
- Evaluation: The model is evaluated using metrics like Mean Squared Error (MSE) and Root mean squared errror.

## Technologies Used:
- Machine Learning: Random Forest
- Web Framework: Flask
- Libraries: Pandas, Scikit-Learn, Flask
