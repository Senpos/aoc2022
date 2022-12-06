with open("input.txt") as f:
    for datastream in f:
        datastream = datastream.strip()

        seen = []
        for position, packet in enumerate(datastream):
            try:
                seen_idx = seen.index(packet)
            except ValueError:
                ...
            else:
                seen = seen[seen_idx + 1 :]

            seen.append(packet)

            if len(seen) == 4:
                print("💚", position + 1)
                break
