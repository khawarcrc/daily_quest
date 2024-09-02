def minnimumWaitingTime(quries):
    quries.sort()
    print(f"Sorted Quries : {quries}")
    totalWaitingTime = 0

    for idx, duration in enumerate(quries):

        # calculate the number of quries left after the current one
        quriesLeft = len(quries) - (idx + 1)
        print(
            f"Query {idx + 1} with duration {duration}: Quries left after this = {quriesLeft}"
        )
        totalWaitingTime += duration * quriesLeft
        print(f"current total waiting time: {totalWaitingTime}")

    return totalWaitingTime


quries = [3, 2, 1, 2, 6]
print(f"Minimum waiting time for quries {quries}: {minnimumWaitingTime(quries)}")
