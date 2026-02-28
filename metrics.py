class ComputeMeter:
    def __init__(self):
        self.sentry_cycles = 0
        self.active_cycles = 0

    def update_sentry(self):
        self.sentry_cycles += 1

    def update_active(self):
        self.active_cycles += 1

    def get_compute_ratio(self):
        total = self.sentry_cycles + self.active_cycles
        if total == 0:
            return 0
        return self.active_cycles / total