<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de Assinatura de Email</title>
    <style>
        :root {
            --primary-color: #000000;
            --secondary-color: #4a4a4a;
            --background-color: #f4f4f9;
            --widget-background: #ffffff;
            --border-color: #e0e0e0;
            --accent-color: #007bff;
            --font-family: 'Helvetica Neue', Arial, sans-serif;
        }

        body {
            font-family: var(--font-family);
            background-color: var(--background-color);
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            color: var(--primary-color);
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            width: 100%;
            max-width: 1200px;
        }

        .column {
            background-color: var(--widget-background);
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            padding: 25px;
            flex: 1;
            min-width: 320px;
        }
        
        h1, h2 {
            margin-top: 0;
            color: var(--primary-color);
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 10px;
        }

        h1 {
            font-size: 1.8em;
        }

        h2 {
            font-size: 1.4em;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            font-size: 0.9em;
            color: var(--secondary-color);
        }

        .form-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            font-size: 1em;
            box-sizing: border-box;
            transition: border-color 0.3s, box-shadow 0.3s;
        }

        .form-group input:focus {
            outline: none;
            border-color: var(--accent-color);
            box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.2);
        }

        .logo-selector {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
            gap: 15px;
        }

        .logo-option {
            cursor: pointer;
            border: 2px solid transparent;
            border-radius: 50%;
            padding: 5px;
            transition: border-color 0.3s, transform 0.2s;
            position: relative;
        }
        
        .logo-option img {
            width: 100%;
            height: auto;
            display: block;
            border-radius: 50%;
        }
        
        .logo-option input[type="radio"] {
            position: absolute;
            opacity: 0;
            width: 0;
            height: 0;
        }

        .logo-option input[type="radio"]:checked + img {
           border: 3px solid var(--accent-color);
           box-shadow: 0 0 10px rgba(0, 123, 255, 0.5);
        }
        
        .logo-option:hover img {
            transform: scale(1.05);
        }

        #preview-box {
            position: sticky;
            top: 20px;
        }

        #signature-preview {
            background-color: #fdfdfd;
            padding: 20px;
            border: 1px dashed var(--border-color);
            border-radius: 8px;
            min-height: 150px;
        }

        #copy-btn {
            display: block;
            width: 100%;
            padding: 15px;
            margin-top: 20px;
            background-color: var(--accent-color);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.2s;
        }

        #copy-btn:hover {
            background-color: #0056b3;
            transform: translateY(-2px);
        }

        @media (max-width: 900px) {
            .container {
                flex-direction: column;
            }
            #preview-box {
                position: static;
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="column" id="controls">
            <h1>Gerador de Assinatura</h1>
            
            <h2>1. Insira seus dados</h2>
            <div class="form-group">
                <label for="name">Nome Completo</label>
                <input type="text" id="name" placeholder="Seu Nome">
            </div>
            <div class="form-group">
                <label for="title">Cargo / Posição</label>
                <input type="text" id="title" placeholder="Sua Posição">
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" placeholder="seu.email@exemplo.com">
            </div>
            <div class="form-group">
                <label for="phone">Telefone</label>
                <input type="tel" id="phone" placeholder="+55 (11) 98765-4321">
            </div>

            <h2>2. Escolha o seu logo</h2>
            <div class="logo-selector">
                <label class="logo-option">
                    <input type="radio" name="logo" value="http://googleusercontent.com/file_content/4" checked>
                    <img src="http://googleusercontent.com/file_content/4" alt="Logo NotCo AI">
                </label>
                 <label class="logo-option">
                    <input type="radio" name="logo" value="http://googleusercontent.com/file_content/7">
                    <img src="http://googleusercontent.com/file_content/7" alt="Logo Chef & AI">
                </label>
                <label class="logo-option">
                    <input type="radio" name="logo" value="http://googleusercontent.com/file_content/1">
                    <img src="http://googleusercontent.com/file_content/1" alt="Logo Marketing">
                </label>
                <label class="logo-option">
                    <input type="radio" name="logo" value="http://googleusercontent.com/file_content/5">
                    <img src="http://googleusercontent.com/file_content/5" alt="Logo Sales">
                </label>
                <label class="logo-option">
                    <input type="radio" name="logo" value="http://googleusercontent.com/file_content/3">
                    <img src="http://googleusercontent.com/file_content/3" alt="Logo Operations">
                </label>
                <label class="logo-option">
                    <input type="radio" name="logo" value="http://googleusercontent.com/file_content/0">
                    <img src="http://googleusercontent.com/file_content/0" alt="Logo R&D">
                </label>
                <label class="logo-option">
                    <input type="radio" name="logo" value="http://googleusercontent.com/file_content/8">
                    <img src="http://googleusercontent.com/file_content/8" alt="Logo Finance">
                </label>
                 <label class="logo-option">
                    <input type="radio" name="logo" value="http://googleusercontent.com/file_content/6">
                    <img src="http://googleusercontent.com/file_content/6" alt="Logo People">
                </label>
                <label class="logo-option">
                    <input type="radio" name="logo" value="http://googleusercontent.com/file_content/2">
                    <img src="http://googleusercontent.com/file_content/2" alt="Logo Quality">
                </label>
            </div>
        </div>

        <div class="column" id="preview-box">
            <h2>3. Pré-visualização e Copiar</h2>
            <div id="signature-preview">
                </div>
            <button id="copy-btn">Copiar Assinatura</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const inputs = document.querySelectorAll('#controls input');
            const copyBtn = document.getElementById('copy-btn');

            function generateSignatureHTML() {
                const name = document.getElementById('name').value || 'Seu Nome';
                const title = document.getElementById('title').value || 'Sua Posição';
                const email = document.getElementById('email').value || 'seu.email@exemplo.com';
                const phone = document.getElementById('phone').value || '+55 (11) 98765-4321';
                const selectedLogo = document.querySelector('input[name="logo"]:checked').value;

                // Usamos uma tabela para máxima compatibilidade com clientes de e-mail
                return `
                    <table cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse; font-family: Arial, sans-serif; color: #333333;">
                        <tr>
                            <td style="padding-right: 15px; vertical-align: middle;">
                                <img src="${selectedLogo}" width="80" height="80" alt="logo" style="border-radius: 50%;">
                            </td>
                            <td style="border-left: 1px solid #cccccc; padding-left: 15px; vertical-align: middle;">
                                <p style="margin: 0; font-size: 14px; font-weight: bold; color: #000000;">${name}</p>
                                <p style="margin: 2px 0; font-size: 12px; color: #555555;">${title}</p>
                                <div style="margin-top: 8px; font-size: 12px; color: #555555;">
                                    <p style="margin: 2px 0;"><strong>E:</strong> <a href="mailto:${email}" style="color: #007bff; text-decoration: none;">${email}</a></p>
                                    <p style="margin: 2px 0;"><strong>T:</strong> ${phone}</p>
                                </div>
                            </td>
                        </tr>
                    </table>
                `;
            }

            function updatePreview() {
                const preview = document.getElementById('signature-preview');
                preview.innerHTML = generateSignatureHTML();
            }

            inputs.forEach(input => {
                input.addEventListener('input', updatePreview);
            });
            
            // Inicializar a preview
            updatePreview();

            copyBtn.addEventListener('click', () => {
                const signatureHtml = generateSignatureHTML();
                
                try {
                    // Usa a Clipboard API para copiar o HTML formatado
                    const blob = new Blob([signatureHtml], { type: 'text/html' });
                    const clipboardItem = new ClipboardItem({ 'text/html': blob });
                    navigator.clipboard.write([clipboardItem]).then(() => {
                        const originalText = copyBtn.textContent;
                        copyBtn.textContent = 'Copiado!';
                        copyBtn.style.backgroundColor = '#28a745';
                        setTimeout(() => {
                            copyBtn.textContent = originalText;
                            copyBtn.style.backgroundColor = 'var(--accent-color)';
                        }, 2000);
                    });
                } catch (err) {
                    console.error('Falha ao copiar HTML: ', err);
                    alert('Seu navegador não suporta a cópia de HTML. Tente copiar manualmente da área de pré-visualização.');
                }
            });
        });
    </script>
</body>
</html>
