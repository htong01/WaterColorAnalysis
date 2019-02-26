run("Fit Spline", "straighten"); 
getSelectionCoordinates(x, y); 
values = getProfile(); 

for (i=0; i<values.length; i++)
  print(x[i],y[i]);
