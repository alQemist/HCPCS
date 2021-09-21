class getCSV:

    import csv
    import requests

    url = "https://www4.palmettogba.com/pdac_dmecs/downloadQrtFeeSchedule.do?dateOfService=07%2F01%2F2021"
    response = requests.get(url)

    with open('data/hcpcs_codes.csv', 'w') as c:
        writer_hcpcs = csv.writer(c)
        for line in response.iter_lines():
            col = line.decode('utf-8').split(",")
            h = col[0]
            print(h)
            writer_hcpcs.writerow([h])


    with open('data/hcpcs_rates.csv', 'w') as f:
        writer = csv.writer(f)

        for line in response.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))