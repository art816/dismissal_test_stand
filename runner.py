import time
import resource

# Настройки для глубокой рекурсии)))
import sys
print(sys.setrecursionlimit(10_000_000))


# Заимпортить свои модуль
import my_try

time_start = time.perf_counter()

# Вызвать расчет здесь
my_try.create_graph()

time_elapsed = (time.perf_counter() - time_start)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
print ("%5.3f secs %5.1f MByte" % (time_elapsed,memMb))
