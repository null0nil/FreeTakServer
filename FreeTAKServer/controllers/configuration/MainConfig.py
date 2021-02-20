import os
currentPath = os.path.dirname(os.path.abspath(__file__))
from pathlib import Path


class MainConfig:
    """
    this is the main configuration file and is the only one which
    should need to be changed
    """
    # this is the port to which clients will connect
    CoTServicePort = int(os.getenv('FTS_COT_PORT', 8087))

    SSLCoTServicePort = int(os.getenv('FTS_SSLCOT_PORT', 8089))

    # this needs to be changed for private data packages to work
    DataPackageServiceDefaultIP = str(os.getenv('FTS_DP_ADDRESS', "0.0.0.0"))

    # User Connection package IP needs to be set to the IP which is used when creating the connection in your tak device
    UserConnectionIP = str(os.getenv('FTS_USER_ADDRESS', "0.0.0.0"))

    # python_version = 'python3.8'
    # userpath = '/usr/local/lib/'
    # TC 2021-02-20 (Sat) --

    # api port
    APIPort = os.getenv('FTS_API_PORT', 19023)

    # Federation port
    FederationPort = os.getenv('FTS_FED_PORT', 9000)

    # api IP
    APIIP = os.getenv('FTS_API_ADDRESS', '0.0.0.0')

    # allowed ip's to access CLI commands
    AllowedCLIIPs = ['127.0.0.1']

    # IP for CLI to access
    CLIIP = '127.0.0.1'

    # whether or not to save CoT's to the DB
    SaveCoTToDB = bool(os.getenv('FTS_COT_TO_DB', True))

    # this should be set before startup
    # DBFilePath = str(os.getenv('FTS_DB_PATH', r'/root/FTSDataBase.db'))
    DBFilePath = str(r'/tmp/FTSDataBase.db') # TC 2021-02-20 (Sat) --

    # the version information of the server (recommended to leave as default)
    version = 'FreeTAKServer-1.5.10 RC 1'

    # MainPath = str(Path(fr'{userpath}{python_version}/dist-packages/FreeTAKServer'))
    # TC 2021-02-20 (Sat) --
    thisFileParts = str(Path(__file__).parent.absolute()).split('/')
    idxEnd = thisFileParts.index("FreeTAKServer") + 1
    MainPath = "/".join(thisFileParts[:idxEnd])

    ExCheckMainPath = str(Path(fr'{MainPath}/ExCheck'))

    ExCheckFilePath = str(Path(fr'{MainPath}/ExCheck/template'))

    ExCheckChecklistFilePath = str(Path(fr'{MainPath}/ExCheck/checklist'))

    DataPackageFilePath = str(Path(fr'{MainPath}/FreeTAKServerDataPackageFolder'))

    # format of API message header should be {Authentication: Bearer 'TOKEN'}
    from uuid import uuid4
    id = str(uuid4())

    nodeID = os.getenv('FTS_NODE_ID', f"FreeTAKServer-{id}")

    # set to None if you don't want a message sent
    ConnectionMessage = f'Welcome to FreeTAKServer {version}. The Parrot is not dead. It’s just resting'

    certsPath = os.getenv('FTS_CERTS_PATH', fr'{MainPath}/certs')

    keyDir = str(Path(fr'{certsPath}/pubserver.key'))

    pemDir = str(Path(fr'{certsPath}/pubserver.pem')) # or crt

    unencryptedKey = str(Path(fr'{certsPath}/pubserver.key.unencrypted'))

    p12Dir = str(Path(fr'{certsPath}/pubserver.p12'))

    CA = str(Path(fr'{certsPath}/ca.pem'))
    CAkey = str(Path(fr'{certsPath}/ca.key'))

    federationCert = str(Path(fr'{certsPath}/pubserver.pem'))
    federationKey = str(Path(fr'{certsPath}/pubserver.key'))
    federationKeyPassword = str(os.getenv('FTS_FED_PASSWORD','defaultpass'))
    
    # location to backup client packages
    clientPackages = str(Path(fr'{MainPath}/certs/ClientPackages'))

    password = str(os.getenv('FTS_PASSWORD', 'defaultpass'))

    websocketkey = os.getenv('FTS_WEBSOCKET_KEY', "YourWebsocketKey")
