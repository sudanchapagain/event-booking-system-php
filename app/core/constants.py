APP_NAME = "Chautari"
APP_DESCRIPTION = "Event booking and discovery system"
APP_VERSION = "0.1.0"

UPLOAD_DIR = "app/static/uploads"
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif"}

DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

ACCESS_TOKEN_EXPIRE_MINUTES = 30
COOKIE_NAME = "access_token"

DEFAULT_DB_URL = "sqlite+aiosqlite:///./sql_app.db"
