with open("history.out") as f:
    data = f.read().split("\n")

clean = []
for cmd in data:
    cmd = cmd.strip().split(" ")
    cmd = " ".join(cmd[1:]).strip()
    print(cmd)
    clean.append(cmd)

final = list(set(clean))

print(sorted(final))

with open("history.txt", "w") as f:
    for cmd in sorted(final):
        f.write(f"{cmd}\n")
