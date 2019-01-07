 ### How to run
 - setup environment variable.
 
    `source run_script.sh`   
 - Run the flask server.
 
    `flask run`
    
 ### Objective
 We are building this boilerplate such that it: 
 
 - Provide minimalistic layout to develop a webservice.
 - Provide well defined structure for common tasks like authentication and 
 validation.
 - Provide a mechanism for environment specific configuration/settings.
 - To have an open layout for enhancement. Ex - DB support 
    
    
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
    .
    ├── celery_worker.py       # celery worker(subscriber)
    ├── flaskr
    │   ├── apis
    │   │   ├── __init__.py
    │   │   ├── user.py        # http resource
    │   │   └── validator.py
    │   ├── cmd.py
    │   ├── common
    │   │   ├── auth.py        # authenticator
    │   │   ├── __init__.py
    │   │   └── validator.py   
    │   ├── __init__.py        # Web app initializer
    │   ├── settings           # env setings
    │   │   ├── base_config.py
    │   │   ├── __init__.py
    │   │   ├── local.py
    │   │   ├── prod.py
    │   │   └── stage.py
    │   └── tasks
    │       ├── big_task.py   # celery task
    │       └── __init__.py
    ├── requirements.txt
    └── run_script.sh         # pre-hook (set env variable)
