from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Text, Date

# creates a global connection to elastic search
connections.create_connection()


# defines what needs to index in elastic search
class TextIndex():
    title = Text()
    tag = Text()
    link = Text()
    date = Date()

    class Meta:
        # name of index. Will be used in search
        index = 'text-index'
