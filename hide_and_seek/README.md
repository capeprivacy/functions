# Hide and seek
This function is meant to go hand in hand with a webapp that hosts 
a GUI for interacting with this function. 

## Function breakdown
The function takes 2 inputs via the semantic connect/invoke. 

One of the inputs is expected to be encrypted while the other one represents
the users' own location. 

It doesn't really matter which location data is passed in first as the function
does not distinguish between the two locations, after receiving two inputs, 
the function will return a value. 


# Setup
## Fetch dependencies for function
Fetch depdencies before deploy:
```
pip install -r requirements.txt --target seek/
```