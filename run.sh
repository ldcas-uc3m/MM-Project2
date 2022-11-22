# upload mappings (creates index)
curl -X PUT "localhost:9200/multimedia?pretty" -H "Content-Type: application/json" -d @mappings.json
# create indexes
curl -s -H "Content-Type: application/json" -XPOST
"localhost:9200/multimedia/_doc/_bulk?pretty" --data-binary @bulk-data.json

# query1
curl -XPOST "localhost:9200/multimedia/_doc?pretty" -H 'Content-Type: application/json' -d @query1.json

# delete index
curl -XDELETE "localhost:9200/multimedia?pretty"