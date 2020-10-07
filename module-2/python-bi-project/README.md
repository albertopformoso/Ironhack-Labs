![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

## Objective
Advise a CEO of a video game studio with the search for a suitable work area in California with geolocation tools.

## User Story
As a CEO of a video game studio I want a new workspace in California, USA since my business has grown as well as the number of employees, so I need to relocate the headquarters in order to be able to place my employees in a wide place, easy to reach in any kind of transportation and with enough space to place new employees.

## Requirements
• Close to public transportation such as bus or subway.

• That the location is in California.

• Close to other video game studios, in the city where there are more studios.

## DoD
To provide an ideal area in California where offices are available, close to public transportation stations. With evidence such as maps with the location and price of the places and info plots.

## Process
1. I made a query from the companies.json database with pymongo retriving only the videogames companies in California.
2. Look for the city that has the most videogames company and easy public transportation.
3. Get a heatmap to locate the zone that has the most videogames studios and compare it with a map of the public transportation.
4. Pin all the videogames studios on the map to get a notion of the density.
5. Finding available offices in the selected city by webscrapping sites with offices rent service and filtering by size.
6. Extract the information from the site.
7. Get the latitude and longitude of the available offices by webscrapping google maps.
8. Cleaning data of available offices and exporting it to a csv.
9. Generate a map with the available offices pined and with the detail of street, size and price.
10. Generate a map with the videogames studios and the available offices for comparison.
11. Export an info table by street, occupancy and price.
12. Data visualization by interactive plots.

## Maps Description
• The blue pins are the occupied offices.

• The red pins are the available offices, and you can see the detail of the office if you click the pin.

• The heatmaps show the density of the zones of occupied offices.