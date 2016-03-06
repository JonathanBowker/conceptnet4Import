# conceptnet4Import
These two scripts prepare the raw conceptnet dump data for import into [Neo4j](http://www.neo4j.com) by formatting them to be read by Neo4j's import tool.

The Conceptnet DB can be downloaded as a set of CSV files from [conceptnet5.media.mit.edu](http://conceptnet5.media.mit.edu/downloads/current/)

Transform the raw files into Neo4j import tool friendly ones by running:
```
python cleanConceptnet.py all_conceptnet_parts.csv nodes.csv
python cleanRelsConceptnet.py all_conceptnet_parts.csv rels.csv
```
and then run the import tool:

```
<NEO_HOME>/bin/neo4j-import --into conceptnet-db --nodes nodes.csv --relationships rels.csv
```
