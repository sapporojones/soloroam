==============================================
EVE Offline Solo Roam:  A text adventure game 
==============================================

By Sapporo Jones 


Readme
======

For now set system origin and destination in the script itself at the top of soloroam.py.  Uses CCP ESI
to plot route and resolve system IDs to names.  


Changelog:
==========

0.1.0 - Initial release!

01/12/21 0.2.0 - 

Big update.  

- Added encounter system with 10 encounters that happen at random and all which alter the game in some way

- Added a rudimentary score system

- Added multithreading to the route list creation function so that with long routes the system doesn't take 50 years to make a route

- Fixed rat spawner so that there's a 50/50 chance of a rat spawn for every system except your origin system (previously it spawned for every system)

- Added 50/50 chance handler for encounter system.  Will likely tweak chance amount with exploration of longer routes.
