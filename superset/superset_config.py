import os

# Superset application secret. Override via SUPERSET_SECRET_KEY for anything
# that is not a throwaway local instance.
SECRET_KEY = os.environ.get(
    "SUPERSET_SECRET_KEY", "dev-only-change-me-please-rotate-0123456789abcd"
)

# Superset's own metadata store (NOT metricdb). Points at the local
# superset_db container defined in docker-compose.yml.
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SUPERSET_METADATA_URI",
    "postgresql+psycopg2://superset:superset@superset_db:5432/superset",
)

# metricdb is read-only for us, so never let the SQL editor mutate it.
PREVENT_UNSAFE_DB_CONNECTIONS = False
SQLLAB_CTAS_NO_LIMIT = True

FEATURE_FLAGS = {
    "DASHBOARD_RBAC": False,
}
