import maya
from apistar import App, Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes

def from_maya(m):
    return {
        'epoch': m.epoch,
        'slang_date': m.slang_date(),
        'slang_time': m.slang_time(),
        'iso8601': m.iso8601(),
        'rfc2822': m.rfc2822(),
        'rfc3339': m.rfc3339()
    }

def when(timestamp):
    return {'timestamp': from_maya(maya.when(timestamp))}

def parse(timestamp):
    return {'timestamp': from_maya(maya.parse(timestamp))}

def home():
    return {
        'now': from_maya(maya.now()),
        'urls': ['/', '/docs', '/when/:timestamp', '/parse/:timestamp']
        }

routes = [
    Route('/when/{timestamp}', 'GET', when),
    Route('/parse/{timestamp}', 'GET', parse),
    Route('/', 'GET', home),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]

app = App(routes=routes)
