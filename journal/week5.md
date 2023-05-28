# Week 5 — DynamoDB and Serverless Caching

- was able to Boto3 which is AWS python SDK into our application
- was able to fix the Flask' object has no attribute 'before_first_request' by commenting out that code and by adding with app.app_context(): and intending the def_init_rollbar(): function as shown bellow 
```
# Rollbar---------------
rollbar_access_token = os.getenv('ROLLBAR_ACCESS_TOKEN')
#@app.before_first_request
with app.app_context():
  def init_rollbar():
      """init rollbar module"""
      rollbar.init(
          # access token
          rollbar_access_token,
          # environment name
          'production',
          # server root directory, makes tracebacks prettier
          root=os.path.dirname(os.path.realpath(__file__)),
          # flask already sets up logging
          allow_logging_basic_config=False)

      # send exceptions from `app` to rollbar, using flask's signal system.
      got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

```




---
##  AWS Postgree RDS

- aws-postgre-RDS
![aws-postgre-RDS](assets/aws-postgre-RDS.png)
