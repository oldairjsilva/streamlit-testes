import streamlit as st
import streamlit_authenticator as stauth
import bcrypt
from pathlib import Path
import yaml
from yaml import SafeLoader

# Função para gerar hash da senha
def generate_password_hash(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Configuração do YAML para usuários
config = {
    'credentials': {
        'usernames': {
            'johndoe': {
                'name': 'John Doe',
                'password': generate_password_hash('123')
            },
            'janedoe': {
                'name': 'Jane Doe',
                'password': generate_password_hash('456')
            }
        }
    },
    'cookie': {
        'name': 'auth_cookie',
        'key': 'random_key',
        'expiry_days': 30
    },
    'preauthorized': {
        'emails': []
    }
}

# Salvar o config no arquivo
config_path = Path('config.yaml')
with config_path.open('w') as config_file:
    yaml.dump(config, config_file, default_flow_style=False)

# Ler o config do arquivo
with config_path.open('r') as config_file:
    config = yaml.load(config_file, Loader=SafeLoader)

# Autenticação
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Widgets de login
name, authentication_status, username = authenticator.login('main')

if authentication_status:
    st.write(f'Bem-vindo {name}')
    authenticator.logout('Logout', 'sidebar')
elif authentication_status == False:
    st.error('Nome de usuário ou senha incorretos')
elif authentication_status == None:
    st.warning('Por favor, insira seu nome de usuário e senha')