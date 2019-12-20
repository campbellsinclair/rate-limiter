import collections
import time


class RateLimiter:
    def __init__(self, max_calls, period, burst=True):
        if not burst:
            period = period / max_calls
            max_calls = 1

        self.period = period
        self.call_times = collections.deque([0] * max_calls)  # oldest at start, newest at end

    def __call__(self, func, *args, **kwargs):
        oldest_time = self.call_times.popleft()
        sleep_time = max(self.period - (time.time() - oldest_time), 0)
        
        time.sleep(sleep_time)
        
        return_value = func(*args, **kwargs)
        self.call_times.append(time.time())
        
        return return_value
