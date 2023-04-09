from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from flask import request
from lib.db import db

tracer = trace.get_tracer("home.activitie")
class HomeActivities:
  def run(logger):
    logger.info("Home activities")
    with tracer.start_as_current_span("home-activities-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now",now.isoformat())
      #span.set_attribute("app.result_lenght",len(results))

    result = db.query_array_json("""
        SELECT
          activities.uuid,
          users.display_name,
          users.handle,
          activities.message,
          activities.replies_count,
          activities.reposts_count,
          activities.likes_count,
          activities.reply_to_activity_uuid,
          activities.expires_at,
          activities.created_at
        FROM public.activities
        LEFT JOIN public.users ON users.uuid = activities.user_uuid
        ORDER BY activities.created_at DESC
        """)
      
    print(result)
    return result
      