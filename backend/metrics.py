import time

class Metrics:
    def __init__(self):
        self.requests = 0
        self.latency = 0

    def start(self):
        self.requests += 1
        return time.time()

    def end(self, s):
        self.latency += time.time() - s

    def stats(self):
        return {
            "requests": self.requests,
            "avg_latency": round(self.latency / max(1, self.requests), 2)
        }

metrics = Metrics()
