from bottle import route, run

@route('/')
def hello():
    return "Hello World!"

@route('/recipes/')
def recipes_list():
    return "LIST"

@route('/recipes/<name>', method='GET')
def recipe_show( name="Mystery Recipe" ):
    return "GET RECIPE " + name

@route('/recipes/<name>', method='DELETE' )
def recipe_delete( name="Mystery Recipe" ):
    return "DELETE RECIPE " + name

@route('/recipes/<name>', method='PUT')
def recipe_save( name="Mystery Recipe" ):
    return "SAVE RECIPE " + name

@route('/recipes/<name>', method='POST')
def recipe_save( name="Mystery Recipe" ):
    return "MODIFY RECIPE " + name


run(host='0.0.0.0', port=8082, debug=True)
