
import logging
class Login:
    """Gerencia o processo de login."""
    def __init__(self, username, password):
        self.username = username
        self.password = password

    async def login(self, page):
        try:
            logging.info("Iniciando login...")
            await page.fill('input[name="username"]', self.username)
            await page.fill('input[name="password"]', self.password)
            await page.click('.btn.btn-block.btn-success')
            await page.wait_for_load_state('networkidle')  
            if "login" in page.url:  
                logging.error("Login não realizado. Verifique suas credenciais.")
            else:
                logging.info("Login realizado com sucesso.")
                
        except Exception as e:
            logging.error(f"Erro durante o login: {e}")
            raise