import time
NUM_RUNS = 1000
class time_see:
    def __init__(self, func, num_runs = 100):
        self.start = 0
        self.num_runs = num_runs
        self.func = func
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__ (self, *args, **kwargs):
        avg_time = (time.time() - self.start) / self.num_runs
        print("Среднее время выполнения, мкс = %.5f" % (avg_time * 1_000_000))
def res(param=1000): #функция для проверки работы декоратора
    for i in range(1, param):
        a = i**2 
with time_see(res, NUM_RUNS) as ts:
    for i in range(NUM_RUNS):
        res()
