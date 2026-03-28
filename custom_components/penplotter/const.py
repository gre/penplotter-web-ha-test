import ssl

DOMAIN = "penplotter"
DEFAULT_PORT = 4443
SCAN_INTERVAL_SECONDS = 5

SSL_CONTEXT = ssl.create_default_context()
SSL_CONTEXT.check_hostname = False
SSL_CONTEXT.verify_mode = ssl.CERT_NONE
