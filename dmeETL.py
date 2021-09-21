class dmeETL:
    import csv

    reload = 1

    if reload:

        with open('data/hcpcs_rates.csv', "r") as data:
            reader = csv.reader(data)
            header = next(reader)

            origheader = header[0:4]
            newheader = origheader + ["STATE","NR","R"]
            cols = header[4:len(header)-4]
            states = []

            for c in cols:
                s = c[0:2]
                if s not in states:
                    states.append(s)

            with open('data/pdac.csv', 'w', encoding='UTF8') as f:
                writer = csv.writer(f)

                # write the header
                writer.writerow(newheader)
                for line in reader:
                    for i, s in enumerate(states):
                        nrv = i * 2 + 4
                        rv = nrv + 2
                        newRow = line[0:4] + [s] + line[nrv:rv]
                        writer.writerow(newRow)