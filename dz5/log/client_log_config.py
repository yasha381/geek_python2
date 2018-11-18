import logging
import logging.handlers
server_log = logging.getLogger('client_log')
server_log.setLevel(logging.INFO)

fh = logging.FileHandler("log/client.log")
fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)-10s %(name)s: %(message)s"))

server_log.addHandler(fh)
