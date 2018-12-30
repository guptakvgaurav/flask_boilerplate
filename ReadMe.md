 ### How to run
 - setup environment variable.
 
    `source run_script.sh`   
 - Run the flask server.
 
    `flask run`
    
    
 ### Configuration
 
 - Use `local.py`,`prod.py`, `stage.py` for configuration. 
 
 ### Logging
 
 -  error.log and info.log files are used to dump the logs.
 
 ### This is how your views look like:
 `
 
    @user_blueprint.route('/<int:user_id>')
    @authenticator('Basic')
    @validator([get_user_validator])
    def get(user_id):
        """
        A get api which demonstrates the use of decorator chaining in Flask HTTP
        request. You can add as many decorators as you want.
        :param user_id:
        :return: json result.
        """
        # /user/12
        app.logger.info('[User] Start')
    return jsonify({'id': user_id})
`

### This is how your project looks like
`

    .
    ├── ReadMe.md
    ├── flaskr
    │   ├── __init__.py
    │   ├── apis
    │   │   ├── __init__.py
    │   │   ├── user.py
    │   │   └── validator.py
    │   ├── cmd.py
    │   ├── common
    │   │   ├── __init__.py
    │   │   ├── auth.py
    │   │   └── validator.py
    │   └── settings
    │       ├── __init__.py
    │       ├── base_config.py
    │       ├── local.py
    │       ├── prod.py
    │       └── stage.py
    ├── requirements.txt
    ├── run_script.sh
`