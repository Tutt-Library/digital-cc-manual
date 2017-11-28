## Multiple object/Batch Ingestion

This tool is used for the ingestion of large collections with similar
meta-data such as the Glass Slides collection. The batch uploader does
not upload objects, it only creates the meta-data and the collection
objects.


## Create a Collection in Islandora
First you must use the Islandora interface to create a collection under
which the objects will be uploaded.

![Creating a Collection](/imgs/library-test-collection.png)

To do this log in to the Islandora interface and click home, then
navigate to the area you would like to create your collection. For
example: I navigated to the library test collection which is located
inside the academic departments and programs parent collection. Then
click "manage" which is one of the three tabs located under the
collection title and then “add an object to this collection.

Once there you will have the option to select a content model, click
"Islandora Collection Content Model" to create a new collection. Then
click next this brings me to a screen where I can create a collection.
You can skip the next two screens until you reach a form starting with
Collection Title. Fill this out giving as much detail about your
collection as possible. You will notice certain fields are marked with
\*, these fields are mandatory.

![Islandora Example URL](/imgs/islandora-url-example.png)

Once you created your collection, find the PID in the address bar
preceded by “coccc%3A”. that You will need this number to tell Fedora
where to create your objects.

## Batch Creator in Fedora Utilities
The next step is to go to the Fedora Utilities and click “Batch Creator”
on the left-hand menu. Here you enter your PID of the collection you
just created and then you choose the content model of the objects you
are creating in that collection. Then enter the number of objects you
would like to create and the title that you’re using for those objects.
Enter any information into these fields that is universal to all of the
objects you are uploading and when you’re finished click “add stub
records” which will add these records as objects without any actual file
attached to them to the collection you just created in Islandora. 

## Islandora Add Datastreams
Next, go back to the Islandora interface and navigate to the collection
that you created. It may be easier to keep both of these windows open in
tabs next to each other on your computer. Once you are there go into the
object you created and click “manage” and from manage click
“datastreams”.

![Islandora Manage Datastreams](/imgs/islandora-manage-datastreams.png)

Here you have the option to “add a data stream”.

![Islandora Add Datastreams](/imgs/islandora-add-datastream.png)

The Datastream ID should be JPEG for JPEGs, PDF for PDFs, mp4 for mp4s
and so on. The Datastream Label is generally the Object name and the
type of object, like in the example above. Then choose the file and
click “Upload” once the file is uploaded just “Add Datastream”. Once you
are finished adding the files to batch upload objects you’ll want to
Index the repository.

