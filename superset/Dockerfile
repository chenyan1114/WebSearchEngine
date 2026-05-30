# Superset image + Postgres driver (the base image ships without psycopg2).
# 5.x runs from a uv-managed venv at /app/.venv, so install into that.
FROM apache/superset:5.0.0
USER root
RUN uv pip install --python /app/.venv/bin/python psycopg2-binary
USER superset
