#Implement the Tower of Hanoi Algorithm
def hanoi_solver(n):
    left = list(range(n, 0, -1))
    middle = []
    right = []

    result = []

    def move(disks, source, target, auxiliary, src_name, tgt_name, aux_name):
        if disks == 1:
            target.append(source.pop())
            result.append(f"{left} {middle} {right}")
            return

        move(disks - 1, source, auxiliary, target, src_name, aux_name, tgt_name)

        target.append(source.pop())
        result.append(f"{left} {middle} {right}")

        move(disks - 1, auxiliary, target, source, aux_name, tgt_name, src_name)

    # initial state
    result.append(f"{left} {middle} {right}")

    move(n, left, right, middle, "A", "C", "B")

    return "\n".join(result)
