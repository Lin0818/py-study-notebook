#function introspeftion
import bobo

@bobo.query('/')
def hello(person):
    return 'hello %s' % person
