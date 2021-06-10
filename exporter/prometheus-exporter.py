import os
import random
from time import sleep
from redis import Redis
from prometheus_client import Counter, Gauge, start_http_server, Info

SAMPLE_FREQUENCY = int(os.getenv('SAMPLE_FREQUENCY', 60))   # sample values every this seconds

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    
    example_flags_metrics   = Info('flags', 'Flags')
    example_gauge           = Gauge('example_gauge', 'Example Gauge')
    example_counter         = Counter('loops_counter', 'Sample loops counter')

    redis = Redis(host='redis')
    # same keys as in redis/init_redis.sh
    flags = {
        'str_flag_alpha': '',
        'str_flag_beta' : '',
        'str_flag_gamma': '',
        'int_flag_delta': ''
    }

    # a loop for serving the metrics indefinietly
    while True:
        for flag in flags.keys():
            val = redis.get(flag)
            if not val:
                continue
            flags[flag] = val.decode('UTF-8')
        example_flags_metrics.info(flags)

        example_gauge.set(random.random())
        example_counter.inc()

        sleep(SAMPLE_FREQUENCY)
