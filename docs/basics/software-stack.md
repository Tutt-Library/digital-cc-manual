author: Jeremy Nelson

# Digital CC Software Stack
Digital CC is the public institutional repository for 
[Colorado College](https://www.coloradocollege.edu).

## History
The beginnings of Colorado College's digital repository was as a founding
member of the Colorado Alliance of Research Libraries' (CARL) pilot
*Alliance Digital Repository* or ADR in the early 2000s. The ADR 
initially used one of the earliest front-ends to Fedora and required
some specific limitations in design that is still reflected in the 
current design of collections in Digital CC.

Later in 2010-2012, the Alliance sought out decided to implement Islandora
for the remaining members that still participating in the ADR. In 2015, 
the Alliance discontinued the ADR service resulting in Colorado College
assuming full hosting/support for the exported content from Fedora.

## Current Infrastructure
The current infrastructure of Digital CC is based on a front-end that
was forked from the Aristotle Discovery Layer and migrated to [Flask][FLK] 

### Virtual Machines and Docker

### Fedora Repository - [fedora-commons.org][FEDORA]
Digital CC's backend is a [Fedora 3.8][FEDORA38] digital repository running

### Islandora - [islandora.ca][ISLAND]
[Islandora][ISLAND] is an open-source digital repository front-end, 
based on [Drupal](https://www.drupal.org/),to a [Fedora 3.8][FEDORA38] 
backend repository. Islandora also uses a [Solr](http://lucene.apache.org/solr/)
index and adds a management layer for digital objects stored in Fedora.

### ElasticSearch - [elastic.co][ES]

### Flask - [flask.pocoo.org][FLK]

## Future Plans - BIBCAT Publisher

[ES]: https://www.elastic.co/
[FEDORA]: http://fedora-commons.org/
[FEDORA38]: https://wiki.duraspace.org/display/FEDORA38/Fedora+3.8+Documentation
[FLK]: http://flask.pocoo.org
[ISLAND]: https://islandora.ca/
