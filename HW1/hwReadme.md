### Changes
1.) I made all variables in functions camel case as this is what I am used to
2.) Added an optional parameter to simulategame so that it can be used with or without visuals; default is without

### Optional Tasks
1.) Added the optional 10 yard standard down, so that every 10 yards gained will reset the downs

### Execution
Execution is done best in a seperate file by calling the `simulategame` function. Below are a couple of snippets of code:
- To run without visuals: `print(fsim.simulategame(5, 75, (0,25), 75, (0,25)))`.
- To run with visuals: `print(fsim.simulategame(5, 75, (0,25), 75, (0,25), fsim.drive_depicted))`.

The numerical parameters can be changed to whatever, though no protection is done against data out of bounds or incorrect data types.