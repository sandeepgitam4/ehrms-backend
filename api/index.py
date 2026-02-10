import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import app

# Vercel handler
def handler(request, context):
    from mangum import Mangum
    asgi_handler = Mangum(app, lifespan="off")
    return asgi_handler(request, context)
