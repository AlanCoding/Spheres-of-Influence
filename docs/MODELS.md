## Development of Models

This document is a soundboard for the models that might ultimately be
necessary for a Django conception of this idea.

### Static Models

Some models should absolutely be pre-loaded. Obviously, planets, moons,
asteroids, and other physical data should be taken to be static. (I'm
putting time aside for the forseeable future)

 - Astronomical Objects
   - planets
   - moons
   - asteroids

### Instantiated Objects

These objects can be created (and sometimes destroyed).

 - Locations
   - Angular coordinates
   - Altitude (if not surface)
   - Associated astronomical object
 - Ships
 - Components
   - Ship foreign key (if attached)
 - Resources
 - Trip segment
   - Delta V (calculated)
 - Complete trip
   - M2M relationship with trip segments
   - status: ongoing, failed, completed
   - delimitated by refueling or docking stops
   - Foreign key ship
