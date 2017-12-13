author: Jeremy Nelson
title: Fedora Commons 

# Fedora Commons 3.8    
Digital CC is currently running [Fedora 3.8](/basics/software-stack#fedora-repository-fedora-commonsorg)
digital repository. Fedora 3.8 has a number of different APIs and service points that
can be used for generating reports. The primary method of calculating the number of items ingested
into Digital CC is to use the Resource Index (RI) search that uses modified SPARQL queries.

## ACRL Metrics
In the [ACRL Annual Survey](https://acrl.countingopinions.com/) under the **Institutional Repositories**
section, the answer to question 50, *Items contributed to the institutional repository via uploads* is 
calculated using the following SPARQL query:

    SELECT DISTINCT ?s 
    WHERE {
        ?s <fedora-model:createdDate> ?date .
        FILTER(?date >= xsd:dateTime('2016-06-30T23:23:59.00Z'))
        FILTER(?date <= xsd:dateTime('2017-07-01T00:00:00.00Z'))
    }

### Fiscal Year 2016-2017
From running the previous query, the total number of digital objects added to Digital CC starting 
from June 30, 2016 to July 1, 2017 was 981.
