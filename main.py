import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
from src.models.user import db
from src.routes.user import user_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Configurar CORS para permitir requisições de qualquer origem
CORS(app)

app.register_blueprint(user_bp, url_prefix='/api')

# uncomment if you need to use database
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

# Rotas WordPress simuladas
@app.route('/wp-json/wp/v2/posts')
def get_posts():
    """Simula a API REST do WordPress para posts"""
    return jsonify([
        {
            "id": 1,
            "title": {"rendered": "Gerador de Assinatura de Email"},
            "content": {"rendered": "Ferramenta para criar assinaturas profissionais de email"},
            "date": "2025-01-08T12:00:00",
            "slug": "gerador-assinatura-email"
        }
    ])

@app.route('/wp-json/wp/v2/pages')
def get_pages():
    """Simula a API REST do WordPress para páginas"""
    return jsonify([
        {
            "id": 1,
            "title": {"rendered": "Página Inicial"},
            "content": {"rendered": "Bem-vindo ao nosso gerador de assinatura de email"},
            "slug": "home"
        }
    ])

@app.route('/wp-admin')
def wp_admin():
    """Simula o painel administrativo do WordPress"""
    return jsonify({
        "message": "WordPress Admin Panel",
        "version": "6.4.2",
        "site_title": "Gerador de Assinatura - WordPress"
    })

@app.route('/wp-json')
def wp_json():
    """Simula a descoberta da API REST do WordPress"""
    return jsonify({
        "name": "Gerador de Assinatura WordPress",
        "description": "Site WordPress para geração de assinaturas de email",
        "url": request.url_root,
        "home": request.url_root,
        "namespaces": ["wp/v2"],
        "authentication": [],
        "routes": {
            "/wp/v2/posts": {"methods": ["GET"]},
            "/wp/v2/pages": {"methods": ["GET"]}
        }
    })

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
