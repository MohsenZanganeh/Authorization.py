from event_handler.user_functions import register_permission

functions = {
    'user': {
        'register_permission': register_permission
    }
}
def event_handler(Topic,key,value):
    functions[Topic].get(key)(value)


