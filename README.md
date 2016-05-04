## Spheres of Influence

This is a quick shot at making a library that will compute Delta V numbers
using python and best-practices with a class structure.

The goal is to answer questions asked in terms A->B trips. For instance,
"what is the velocity to escape Earth's gravity well starting at LEO at 
400 km altitude?"

You could put this into Google:

```
sqrt(2*G*(mass of Earth)/(radius of Earth))-sqrt(G*(mass of Earth)/((radius of Earth)+(400 km))
```

That will get your answer, but it's a simple quesiton.

### Sources

Planet data dump
http://nssdc.gsfc.nasa.gov/planetary/factsheet/

Moon data dump
 - orbital
   - http://www.windows2universe.org/our_solar_system/moons_table.html
 - physical
   - http://ssd.jpl.nasa.gov/?sat_phys_par

