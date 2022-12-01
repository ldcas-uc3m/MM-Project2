# upload mappings (creates index)
curl -XPUT "localhost:9200/multimedia?pretty" -H "Content-Type: application/json" -d @scripts/mappings.json

# test one
# curl -s -XPOST "localhost:9200/multimedia/_doc/test1?pretty" -H "Content-Type: application/json" -d @data/test.json
# the id of the document was put as test1, if empty it's set as random
# curl -s -XDELETE "localhost:9200/multimedia/_doc/test1?pretty"

# upload documents
curl -s -XPOST "localhost:9200/multimedia/_doc/_bulk?pretty" -H "Content-Type: application/json"  --data-binary @data/bulk_data.json

# query1
# World	War II films produced from 1980 onwards
curl -XGET "localhost:9200/multimedia/_search?pretty" -H 'Content-Type: application/json' -d @scripts/query1.json

# query2
# Directors	with the most action films
curl -XGET "localhost:9200/multimedia/_search?pretty" -H 'Content-Type: application/json' -d @scripts/query2.json

# query3
# LGBTQ-themed films available in the collection. In addition to the listing, show the number of films by year
curl -XGET "localhost:9200/multimedia/_search?pretty" -H 'Content-Type: application/json' -d @scripts/query3.json

# query4
# LGBTQ-themed films available in the collection. In addition to the listing, show the number of films by year
curl -XGET "localhost:9200/multimedia/_search?pretty" -H 'Content-Type: application/json' -d @scripts/query3.json

# delete index
curl -XDELETE "localhost:9200/multimedia?pretty"