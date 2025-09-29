
# xxxxxxxxxxxxxxxxxxxxxxxxx  unsolved  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def TOH(n, source, auxillary, destination, s, a, d):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Step 1: Move top n-1 disks from Source to Auxiliary using Destination
    TOH(n-1, source, destination, auxillary, s, a, d)

    # Step 2: Move the largest disk from Source to Destination
    print(f"Move disk {n} from {source} to {destination}")

    # Step 3: Move the n-1 disks from Auxiliary to Destination using Source
    TOH(n-1, auxillary, source, destination, s, a, d)

s = [3,2,1]
a = []
d = []

TOH(len(s), "S", "A", "D", s, a, d)