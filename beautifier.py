import urllib.parse

params_file = open('parameters.txt', 'r')
input = open('in.txt', 'r')
output = open('out.txt', 'a')

for line_in in input:
    line_in = urllib.parse.unquote(line_in)
    hits = [hit + '@\n\n\n' for hit in line_in.split('@')]
    for i in range(0, len(hits)):
        hits[i] = ['=' + par + '\n' for par in hits[i].split('&')]

    params = []
    for param in params_file:
        [enc, dec] = param.split('=')
        enc = enc + '='
        dec = dec.replace('\n', '') + ' = '
        params.append([enc, dec])

    for param in params:
        [enc, dec] = param
        for i in range(0, len(hits)):
            for j in range(0, len(hits[i])):
                if enc.find('<number>') == -1:
                    hits[i][j] = hits[i][j].replace('='+enc, dec)

                elif hits[i][j].startswith('='+enc.split('<number>')[0]) \
                        and hits[i][j][len(enc.split('<number>')[0]) + 1].isnumeric() \
                        and enc.find('<number2>') == -1:
                    enc_split = enc.split('<number>')
                    number = hits[i][j].replace('='+enc_split[0], '')[0]
                    if hits[i][j].replace('='+enc_split[0], '')[1].isnumeric():
                        number = number + hits[i][j].replace('='+enc_split[0], '')[1]
                        if hits[i][j].replace('='+enc_split[0], '')[2].isnumeric():
                            number = number + hits[i][j].replace('='+enc_split[0], '')[2]
                    hits[i][j] = hits[i][j].replace('='+(enc.replace('<number>', number)), dec.replace('<number>', number))
                
                elif hits[i][j].startswith('='+enc.split('<number>')[0]) \
                        and hits[i][j][len(enc.split('<number>')[0]) + 1].isnumeric() \
                        and enc.find('<number2>') != -1 \
                        and ''.join([i for i in hits[i][j] if not i.isdigit()])[3:5] == enc.split('<number>')[1][:2] \
                        and enc.find('<number3>') == -1:
                    enc_split = enc.split('<number>')
                    number = hits[i][j].replace('='+enc_split[0], '')[0]
                    if hits[i][j].replace('='+enc_split[0], '')[1].isnumeric():
                        number = number + hits[i][j].replace('='+enc_split[0], '')[1]
                        if hits[i][j].replace('='+enc_split[0], '')[2].isnumeric():
                            number = number + hits[i][j].replace('='+enc_split[0], '')[2]
                    number2 = hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0]), '')[0]
                    if hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0]), '')[1].isnumeric():
                        number2 = number2 + hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0]), '')[1]
                        if hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0]), '')[2].isnumeric():
                            number2 = number2 + hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0]), '')[2]
                    hits[i][j] = hits[i][j].replace('='+(enc.replace('<number>', number).replace('<number2>', number2)), dec.replace('<number>', number).replace('<number2>', number2))

                elif hits[i][j].startswith('='+enc.split('<number>')[0]) \
                        and hits[i][j][len(enc.split('<number>')[0]) + 1].isnumeric() \
                        and enc.find('<number2>') != -1 \
                        and ''.join([i for i in hits[i][j] if not i.isdigit()])[3:5] == enc.split('<number>')[1][:2] \
                        and enc.find('<number3>') != -1 \
                        and ''.join([i for i in hits[i][j] if not i.isdigit()])[5:7] == enc.split('<number2>')[1][:2]:
                    enc_split = enc.split('<number>')
                    number = hits[i][j].replace('='+enc_split[0], '')[0]
                    if hits[i][j].replace('='+enc_split[0], '')[1].isnumeric():
                        number = number + hits[i][j].replace('='+enc_split[0], '')[1]
                        if hits[i][j].replace('='+enc_split[0], '')[2].isnumeric():
                            number = number + hits[i][j].replace('='+enc_split[0], '')[2]
                    number2 = hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0]), '')[0]
                    if hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0]), '')[1].isnumeric():
                        number2 = number2 + hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0]), '')[1]
                        if hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0]), '')[2].isnumeric():
                            number2 = number2 + hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0]), '')[2]
                    enc_split2 = enc.split('<number2>')
                    number3 = hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0])+number2+(enc_split2[1].split('<number3>')[0]), '')[0]
                    if hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0])+number2+(enc_split2[1].split('<number3>')[0]), '')[1].isnumeric():
                        number3 = number3 + hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0])+number2+(enc_split2[1].split('<number3>')[0]), '')[1]
                        if hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0])+number2+(enc_split2[1].split('<number3>')[0]), '')[2].isnumeric():
                            number3 = number3 + hits[i][j].replace('='+enc_split[0]+number+(enc_split[1].split('<number2>')[0])+number2+(enc_split2[1].split('<number3>')[0]), '')[2]
                    hits[i][j] = hits[i][j].replace('='+(enc.replace('<number>', number).replace('<number2>', number2).replace('<number3>', number3)), dec.replace('<number>', number).replace('<number2>', number2).replace('<number3>', number3))

    for hit in hits:
        for param in hit:
            output.write(param)

print('DONE')