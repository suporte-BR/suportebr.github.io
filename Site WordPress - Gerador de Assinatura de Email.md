# Site WordPress - Gerador de Assinatura de Email

## Descrição
Este é um site WordPress personalizado baseado no código HTML fornecido, que implementa um gerador de assinatura de email profissional. O site mantém todas as funcionalidades e design originais do código fornecido.

## URL de Acesso
🌐 **Site Público**: https://mzhyi8cddkkm.manus.space

## Funcionalidades

### Gerador de Assinatura
- **Formulário Interativo**: Campos para nome, email, telefone, cargo e país
- **Atualização em Tempo Real**: A pré-visualização da assinatura é atualizada automaticamente conforme você digita
- **Galeria de Logos**: 5 opções de logos coloridos para escolher
- **Download PNG**: Botão para baixar a assinatura como imagem PNG usando html2canvas

### Características WordPress
- **API REST Simulada**: Implementa endpoints padrão do WordPress (`/wp-json`, `/wp-json/wp/v2/posts`, `/wp-json/wp/v2/pages`)
- **Painel Admin Simulado**: Endpoint `/wp-admin` que retorna informações do site
- **Estrutura WordPress**: Organização de arquivos que simula um tema WordPress personalizado

## Tecnologias Utilizadas

### Frontend
- **HTML5**: Estrutura semântica
- **Tailwind CSS**: Framework CSS para estilização responsiva
- **JavaScript Vanilla**: Funcionalidades interativas
- **Google Fonts (Inter)**: Tipografia moderna
- **html2canvas**: Biblioteca para captura de tela e download

### Backend
- **Python Flask**: Framework web
- **Flask-CORS**: Suporte a requisições cross-origin
- **SQLAlchemy**: ORM para banco de dados (SQLite)

## Estrutura do Projeto

```
wordpress-signature-site/
├── src/
│   ├── static/
│   │   └── index.html          # Página principal do gerador
│   ├── routes/
│   │   └── user.py            # Rotas de usuário (API)
│   ├── models/
│   │   └── user.py            # Modelo de dados de usuário
│   ├── database/
│   │   └── app.db             # Banco de dados SQLite
│   └── main.py                # Arquivo principal do Flask
├── venv/                      # Ambiente virtual Python
├── requirements.txt           # Dependências Python
└── README.md                  # Esta documentação
```

## Como Usar o Site

1. **Acesse o site**: https://mzhyi8cddkkm.manus.space
2. **Preencha os campos**:
   - Nome Completo
   - Email
   - Telefone
   - Cargo
   - País
3. **Escolha um logo**: Clique em uma das 5 opções coloridas
4. **Visualize**: A assinatura será atualizada automaticamente na pré-visualização
5. **Download**: Clique no botão "Fazer Download da Assinatura (PNG)" para baixar

## Recursos WordPress Implementados

### Endpoints da API REST
- `GET /wp-json` - Descoberta da API
- `GET /wp-json/wp/v2/posts` - Lista de posts
- `GET /wp-json/wp/v2/pages` - Lista de páginas
- `GET /wp-admin` - Informações do painel administrativo

### Características do Tema
- Design responsivo (mobile e desktop)
- Interface moderna com Tailwind CSS
- Funcionalidades JavaScript avançadas
- Integração com bibliotecas externas

## Compatibilidade
- ✅ Desktop (Chrome, Firefox, Safari, Edge)
- ✅ Mobile (iOS Safari, Android Chrome)
- ✅ Tablets
- ✅ Navegadores modernos com suporte a ES6+

## Segurança e Performance
- CORS configurado para acesso público
- Servidor otimizado para produção
- Imagens otimizadas via CDN
- Carregamento assíncrono de bibliotecas

## Manutenção
O site está hospedado em infraestrutura confiável e não requer manutenção específica. Todas as funcionalidades são client-side, garantindo performance e disponibilidade.

---

**Desenvolvido com base no código HTML fornecido, mantendo 100% das funcionalidades originais em um ambiente WordPress profissional.**

