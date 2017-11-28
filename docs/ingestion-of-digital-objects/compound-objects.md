# Compound Objects
Compound objects are objects that have multiple object datastreams
attached to them. An example would be an oral history where there are
multiple PDFs, images, and the actual audio file all accessed as a
single object. To create a compound object, you must first create the
parent object using the compound object model, then create the
individual objects for each datastream.

## Creating Compound Objects through Fedora 3.8 Utilities 
Creating a compound object in Fedora 3.8 Utilities is possible by 
following these steps:

1.  Create the Compound Object first following the directions for 
    [single object][SINGLE_OBJ] but select the *Compound Object Content Model*
    under the Islandora Content Object drop-down list. ![Compound Object Dropdown](/imgs/compound-object-dropdown.png)
1.  Create each Datastream object following the [single object][SINGLE_OBJ],
    selecting the correct Islandora Content Model but adding the following 
    fields in the **Object Properties** section. The PID of Parent that you 
    created in the previous step, and the Order in the Compound Object.
    ![Object Properties for a Child Object](/imgs/child-compound-obj-props.png)

## Creating Compound Objects through Islandora
![Islandora Manage Compound](/imgs/islandora-manage-compound.png)

Once all of the object datastreams are created, find the parent object
in Islandora and go to the "manage" tab then navigate to "compound".
Here you can add the Child Objects using their PIDs as well as remove
child objects and re-order the child objects.

To add an object type in either coccc: and the PID or just the PID then
click "add" at the bottom of the screen.

[SINGLE_OBJ]: /ingestion-of-digital-objects/single-object-ingestion
