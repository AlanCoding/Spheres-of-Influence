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

## Goals

 - A python library that will take two locations and find the Delta V between them
 - Network resource flow calculator - a numerical illustration of [Hop's vision](http://hopsblog-hop.blogspot.com/2013/09/one-legged-stools.html)
 - Simple website (likely client-side scripting) that can calculate the first goal with selection boxes

I believe all these are very highly attainable, although they will push my own
limits to some degree (part of the point). Thus, I want to distinguish them
from the next set of goals.

 - discrete simulations with time-domain actions within the network model
 - A text-based website where users can make accounts and input data to create their own
   network-defined resource flow numbers
   - Ability to share this with a link
 - A time-based website where users can build their time-domain actions in the
   discrete simulation

