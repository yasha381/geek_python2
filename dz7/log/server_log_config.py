import logging
import logging.handlers
server_log = logging.getLogger('server_log')
server_log.setLevel(logging.INFO)

fh = logging.FileHandler("../log/server.log")
fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)-10s %(name)s: %(message)s"))

server_log.addHandler(fh)
server_log.addHandler(logging.handlers.TimedRotatingFileHandler('../log/server.log', when='D', interval=1, backupCount=1))
