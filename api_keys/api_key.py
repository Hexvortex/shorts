import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the API keys from the text file
config.read('api_keys.txt')

# Access the API keys using the corresponding section and key names
chatgpt_api_key = config.get('API_KEYS', 'CHATGPT_API_KEY')
AUTHORIZATION = config.get('API_KEYS', 'AUTHORIZATION')
X_USER_ID = config.get('API_KEYS', 'X_USER_ID')
PEXELS_API_KEY = config.get('API_KEYS', 'PEXELS_API_KEY')

 
