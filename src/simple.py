import json
import subprocess
import time
from pathlib import Path


def docker(*args):
    return subprocess.check_output(["docker", *args], text=True).strip()


logs = Path(__file__).resolve().parents[1] / "nis/artifacts" / time.strftime("%Y%m%d-%H%M%S")
logs.mkdir(parents=True)
(logs / "parties.json").write_text(json.dumps({
    "replicas": ["127.0.0.1"] * 4, "clients": ["127.0.0.1"],
}))
print(f"Logs: {logs}")

container = docker("run", "-d", "--platform", "linux/amd64",
                   "-v", f"{logs}:/run", "-e", "LD_LIBRARY_PATH=/usr/lib",
                   "--entrypoint", "sleep", "alea-bft:543786ef199a", "60")

try:
    for name, args in [
        ("replica0", "replica.jar 1 alea 0 4 1"),
        ("replica1", "replica.jar 1 alea 1 4 1"),
        ("replica2", "replica.jar 1 alea 2 4 1"),
        ("replica3", "replica.jar 1 alea 3 4 1"),
        ("client0", "client.jar 1 alea 0 4"),
    ]:
        docker("exec", "-d", container, "sh", "-c",
               f"echo $$ > /run/{name}.pid; exec java -Xms128M -Xmx512M -jar /alea/{args} "
               f"/run/parties.json /run/{name}.results > /run/{name}.log 2>&1")
    client_log = logs / "client0.log"
    for _ in range(30):
        if client_log.exists() and "Starting stress tests" in client_log.read_text():
            break
        time.sleep(1)
    else:
        raise RuntimeError("Client did not start; see logs")
    time.sleep(10)
    docker("exec", container, "sh", "-c", "kill -TERM $(cat /run/*.pid)")
    time.sleep(1)
    with (logs / "check.log").open("w") as report:
        for i in range(4):
            events = (logs / f"replica{i}.results").read_text().splitlines()
            accepted = sum(line.startswith("in,") for line in events)
            delivered = sum(line.startswith("out,") for line in events)
            line = f"replica{i}: accepted={accepted} delivered={delivered}"
            print(line)
            report.write(line + "\n")
            if not accepted or not delivered:
                raise RuntimeError("No requests processed; see logs")
finally:
    docker("rm", "-f", container)
