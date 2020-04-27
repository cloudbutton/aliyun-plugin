import sys
import os
from pywren_ibm_cloud.utils import version_str


PYTHON_RUNTIME = 'python3'
RUNTIME_TIMEOUT_DEFAULT = 600    # Default: 600 s => 10 minutes
RUNTIME_TIMEOUT_MAX = 600        # Platform maximum
RUNTIME_MEMORY_DEFAULT = 256
RUNTIME_MEMORY_MAX = 1536
MAX_CONCURRENT_WORKERS = 100     # Platform maximum

SERVICE_NAME = 'pywren-runtime'
HANDLER_FOLDER_LOCATION = os.path.join(os.getcwd(), 'pywren_handler_aliyun')



def load_config(config_data=None):

    this_version_str = version_str(sys.version_info)
    if this_version_str != '3.6':
        raise Exception('The functions backend Aliyun Function Compute currently'
                        ' only supports Python version 3.6.X and the local Python'
                        'version is {}'.format(this_version_str))

    if 'runtime' not in config_data['pywren']:
        config_data['pywren']['runtime'] = 'default'

    if 'runtime_memory' in config_data['pywren']:
        if config_data['pywren']['runtime_memory'] > RUNTIME_MEMORY_MAX:
            config_data['pywren']['runtime_memory'] = RUNTIME_MEMORY_MAX
    else:
        config_data['pywren']['runtime_memory'] = RUNTIME_MEMORY_DEFAULT

    if 'runtime_timeout' in config_data['pywren']:
        if config_data['pywren']['runtime_timeout'] > RUNTIME_TIMEOUT_MAX:
            config_data['pywren']['runtime_timeout'] = RUNTIME_TIMEOUT_MAX
    else:
        config_data['pywren']['runtime_timeout'] = RUNTIME_TIMEOUT_DEFAULT

    if 'workers' in config_data['pywren']:
        if config_data['pywren']['workers'] > MAX_CONCURRENT_WORKERS:
            config_data['pywren']['workers'] = MAX_CONCURRENT_WORKERS
    else:
        config_data['pywren']['workers'] = MAX_CONCURRENT_WORKERS


    if 'aliyun_fc' not in config_data:
        raise Exception("aliyun_fc section is mandatory in the configuration")

    required_parameters = ('endpoint', 'access_key_id', 'access_key_secret')

    if set(required_parameters) > set(config_data['aliyun_fc']):
        raise Exception('You must provide {} to access to Aliyun Function Compute '\
                        .format(required_parameters))
