from fastapi import APIRouter
import time
import psutil
import threading

router = APIRouter(prefix="/blackrock/challenge/v1")


@router.get("/performance")
def performance():
    start_time = time.perf_counter()

    # Simulate lightweight workload (optional)
    time.sleep(0.001)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    # Format time as HH:mm:ss.SSS
    formatted_time = time.strftime("%H:%M:%S", time.gmtime(execution_time))
    milliseconds = int((execution_time % 1) * 1000)

    process = psutil.Process()
    memory = process.memory_info().rss / (1024 * 1024)
    threads = threading.active_count()

    return {
        "time": f"{formatted_time}.{milliseconds:03d}",
        "memory": f"{memory:.2f} MB",
        "threads": threads
    }