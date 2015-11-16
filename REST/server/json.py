from bottle import route, run

@route('/recipes/')
def recipes_list():
    return { "success" : False, "paths" : [], "error" : "list not implemented yet" }

@route('/recipes/<name>', method='GET')
def recipe_show( name="Mystery Recipe" ):
    return { "success" : False, "path" : "/PTH/TO/XML/"+name+".xml", "error" : "show not implemented yet" }

@route('/recipes/<name>', method='DELETE' )
def recipe_delete( name="Mystery Recipe" ):
    return { "success" : False, "error" : "delete not implemented yet" }

@route('/recipes/<name>', method='PUT')
def recipe_save( name="Mystery Recipe" ):
    return { "success" : False, "path" : "/PTH/TO/XML/"+name+".xml", "error" : "save not implemented yet" }

run(host='0.0.0.0', port=8082, debug=True)
