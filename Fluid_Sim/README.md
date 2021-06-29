# Configuration
The program accepts a JSON file with the following format:

```
{
    "colors":[
        {
            "cmap":,
            "color":
        }
    ],
    "densities":[
        {
            "position":{
                "x1":,
                "x2":,
                "y1":,
                "y2":
            },
            "density":
        }
    ],
    "objects":[
        {
            "position":{
                "x":,
                "y":
            },
            "shape":{
                "cols":,
                "rows":
            }
        }
    ],
    "velocities":[
        {
            "position":{
                "x1":,
                "x2":,
                "y1":,
                "y2":
            },
            "direction": [,],
            "behavior": ""
        }
    ]
}
```
## colors
**cmap** takes an integer from 0 to 69 to select a cmap among the ones found in the palette.py file.
**color** takes an integer from 0 to 4 to select a color among the ones found in the palette.py file.

## densities
**position** takes the arrangement of x and y values for position (x1, x2, y1, y2). This will define the position of the density inside the grid.
**density** takes the value for the density applied to its corresponding position.

## objects
**Failed to implement objects, this step can be ommited (the keys and its values where defined anyways).**
**position** takes x, y values. This will define the position of the object inside the grid.
**shape** takes cols and rows. This will define the height and width.

## velocities
**position** takes the arrangement of x and y values for position (x1, x2, y1, y2). This will define the position of the velocity force inside the grid.
**direction** takes a list for the velocity direction (x, y).
**behavior** takes a string for the behavior of the velocity force. The choices for velocity are: 'normal', 'spiral', 'zigzag_horizontal', 'zigzag_vertical'.

# Run
Run the program along with the JSON configuration file (taken as sys.argv[1])

```
python .\fluid.py .\config.json
```
