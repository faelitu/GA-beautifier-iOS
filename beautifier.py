import urllib.parse
import json
import re

input = open('in.txt', 'r')

params_dict = {
    'v':            'Protocol Version',
    'tid':          'Web Property ID',
    'aip':          'Anonymize IP',
    'npa':          'Disabling Advertising Personalization',
    'ds':           'Data Source',
    'qt':           'Queue Time',
    'z':            'Cache Buster',
    'cid':          'Client ID',
    'uid':          'User ID',
    'sc':           'Session Control',
    'uip':          'User IP',
    'ua':           'User Agent',
    'geoid':        'User Geographical Location',
    'dr':           'Document Referrer',
    'cn':           'Campaign Name',
    'cs':           'Campaign Source',
    'cm':           'Campaign Medium',
    'ck':           'Campaign Keyword',
    'cc':           'Campaign Content',
    'ci':           'Campaign ID',
    'gclid':        'Google Ads ID',
    'dclid':        'Google Display Ads ID',
    'sr':           'Screen Resolution',
    'vp':           'Viewport Size',
    'de':           'Document Encoding',
    'sd':           'Screen Color Depth',
    'ul':           'User Language',
    'je':           'Is Java Enabled',
    'fl':           'Flash Version',
    't':            'Hit Type',
    'ni':           'Is Non-Interactive Hit',
    'dl':           'Document Location URL',
    'dh':           'Document Host Name',
    'dp':           'Document Path',
    'dt':           'Document Title',
    'cd':           'Screen Name',
    'cg0':          'Content Group 0',
    'linkid':       'Link ID',
    'an':           'Application Name',
    'aid':          'Application ID',
    'av':           'Application Version',
    'aiid':         'Application Installer ID',
    'ec':           'Event Category',
    'ea':           'Event Action',
    'el':           'Event Label',
    'ev':           'Event Value',
    'ti':           'Transaction ID',
    'ta':           'Transaction Affiliation',
    'tr':           'Transaction Revenue',
    'ts':           'Transaction Shipping',
    'tt':           'Transaction Tax',
    'in':           'Item Name',
    'ip':           'Item Price',
    'iq':           'Items Quantity',
    'ic':           'Item Code',
    'iv':           'Item Category',
    'pr0id':        'Product 0 SKU',
    'pr0nm':        'Product 0 Name',
    'pr0br':        'Product 0 Brand',
    'pr0ca':        'Product 0 Category',
    'pr0va':        'Product 0 Variant',
    'pr0pr':        'Product 0 Price',
    'pr0qt':        'Product 0 Quantity',
    'pr0cc':        'Product 0 Coupon Code',
    'pr0ps':        'Product 0 Position',
    'pr0cd1':       'Product 0 Custom Dimension 1',
    'pr0cm1':       'Product 0 Custom Metric 1',
    'pa':           'Product Action',
    'tcc':          'Transaction Coupon Code',
    'pal':          'Product Action List',
    'cos':          'Checkout Step',
    'col':          'Checkout Step Option',
    'il0nm':        'Product Impression List 0 Name',
    'il0pi1id':     'Product 1 Impression List 0 SKU',
    'il0pi1nm':     'Product 1 Impression List 0 Name',
    'il0pi1br':     'Product 1 Impression List 0 Brand',
    'il0pi1ca':     'Product 1 Impression List 0 Category',
    'il0pi1va':     'Product 1 Impression List 0 Variant',
    'il0pi1ps':     'Product 1 Impression List 0 Position',
    'il0pi1pr':     'Product 1 Impression List 0 Price',
    'il0pi1cd2':    'Product 1 Impression List 0 Custom Dimension 2',
    'il0pi1cm2':    'Product 1 Impression List 0 Custom Metric 2',
    'promo0id':     'Promotion 0 ID',
    'promo0nm':     'Promotion 0 Name',
    'promo0cr':     'Promotion 0 Creative',
    'promo0ps':     'Promotion 0 Position',
    'promoa':       'Promotion Action',
    'cu':           'Currency Code',
    'sn':           'Social Network',
    'sa':           'Social Action',
    'st':           'Social Action Target',
    'utc':          'User Timing Category',
    'utv':          'User Timing Variable Name',
    'utt':          'User Timing Time',
    'utl':          'User Timing Label',
    'plt':          'Page Load Time',
    'dns':          'DNS Time',
    'pdt':          'Page Download Time',
    'rrt':          'Redirect Response Time',
    'tcp':          'TCP Connect Time',
    'srt':          'Server Response Time',
    'dit':          'DOM Interactive Time',
    'clt':          'Content Load Time',
    'exd':          'Exception Description',
    'exf':          'Is Exception Fatal',
    'cd0':          'Custom Dimension 0',
    'cm0':          'Custom Metric 0'
}

batch = []
for hit in input:
    hit = hit.replace('%@\n', '')
    pars = hit.split('&')
    hit_obj = {}
    for par in pars:
        par = urllib.parse.unquote(par)
        if '=' not in par: par = par + '='
        if len(par.split('=')) < 2: par = par + 'None'
        [key_ga, value] = par.split('=')
        if not bool(re.search(r'\d', key_ga)):
            key_readable = params_dict.get(key_ga)
            if key_readable != None:
                hit_obj.update({key_readable: value})
            else:
                hit_obj.update({key_ga: value})
        else:
            chars = [char for char in key_ga]
            for i in range(0, len(chars)):
                if i < len(chars)-1 and chars[i].isnumeric() and chars[i+1].isnumeric():
                    chars[i] = chars[i] + chars.pop(i+1)
            numbers = [number for number in chars if number.isnumeric()]
            nums_dict = [str(num) for num in range(0, len(numbers))]
            chars_dict = []
            i = 0
            for char in chars:
                if not char.isnumeric():
                    chars_dict.append(char)
                else:
                    chars_dict.append(nums_dict[i])
                    i = i + 1
            key_dict = ''.join(chars_dict)
            key_readable = params_dict.get(key_dict)
            for i in range(0, len(numbers)):
                key_readable = key_readable.replace(nums_dict[i], numbers[i])
            hit_obj.update({key_readable: value})

            
    batch.append(hit_obj)

with open('out.json', 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=4)

print('DONE')