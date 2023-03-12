# UOCIS322 - Project 6 #
Continuation of the Brevet time calculator but now refactoring out MongoDB calls to utilize a RESTful API.

## Overview

A continuation of the brevet calculator now with a RESTful API. By refactoring our code we can limit direct contact between the webpage and the database. This also allows us to allow calls to the database using our new API without relying on the webpage itself. In order to setup API, the data schema property was introduced. Also introduced to using Postman in order to test and debug API calls.


### ACP controle times

This project consists of a web application that is based on RUSA's online calculator. Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders). When using the webapp, you are presented with a grid in which to enter either your mile or distance markers. At the top there is a drop down for the overall brevit distance, as well as the starting date/time. Once a control has been typed into a submission field, the webapp will update and provide correspondiong opening and closing control times.

This webapp is based on and utilized the calculator found here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html).

### ACP Brevet Algorithm

In order to calculate the individual opening and closing brevet times, there is an algorithm that can be used along with a corresponding chart of maximum and minimum speeds. Essentially the algorithm takes a given control location, and the end brevet distance. From there the mathematical algorithm divides the given control distance by the minimum/maximum speed, with the integer portion of the result being the hours. For the minutes, you take the remainder and multiply by 60 then round. Finally one just has to take the new time and add it to the original start time to determine the corresponding brevits. There are additional edge cases to look out for which are accounted for such as having a control under 60km, having a start time early on end before any late arrivals begin, and having a control slightly over the final ending brevet distance. All of these are explained further and noted on [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator).  

### API Docoumentation
	
* GET `http://API:PORT/api/brevets` will display all brevets stored in the database.
* GET `http://API:PORT/api/brevet/ID` will display brevet with id `ID`.
* POST `http://API:PORT/api/brevets` will insert brevet object in request into the database.
* DELETE `http://API:PORT/api/brevet/ID` will delete brevet with id `ID`.
* PUT `http://API:PORT/api/brevet/ID` will update brevet with id `ID` with object in request.

## Student:

NameL Jacob Burke

School Email: jburke2@uoregon.edu

Personal Email: jwburke256@gmail.com

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
