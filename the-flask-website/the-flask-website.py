from app import app

from app import database
from app.models import User,Posts

@app.shell_context_processor
def make_shell_context():
    return {'database':database,'User':User,'Posts':Posts}
