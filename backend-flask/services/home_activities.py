from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from flask import request
from lib.db import db
import json

tracer = trace.get_tracer("home.activitie")
class HomeActivities:
  def run(logger):
    logger.info("Home activities")
    with tracer.start_as_current_span("home-activities-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now",now.isoformat())
      #span.set_attribute("app.result_lenght",len(results))

    sql = db.template('activities','home')
    results = db.query_array_json(sql)
    return results
      