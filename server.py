from flask import Flask,render_template,request,jsonify,make_response
import os
import folium
import requests
import validators
import script
import socket as s
import ipaddress

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/getMap')
def getMap():
    url = request.args['ip']

    message = ''
    error = ''
    valid_url = validators.url(url)
    if valid_url==True:
        print("Url is valid")
        message = 'Url is valid.'
        url = url.split('://')[1].split('/')[0]
        print(url)
        ip_add = s.gethostbyname(url)
        print('The IP Address of ' + url + ' is: '  + ip_add)
        rec = script.IpTracker(ip_add)
    else:
        try:
            ip = ipaddress.ip_address(url)
            print('{} is a correct IP {} address.'.format(ip, ip.version))
            rec = script.IpTracker(ip)
        except ValueError:
            error = 'Please enter a valid IP/URL'
    
    res = {}
    if len(error.strip()) != 0:
        res['error'] = error
        return jsonify(res)
    else:    
        start_coords = (rec.latitude, rec.longitude)
        folium_map = folium.Map(location=start_coords, zoom_start=14)

        folium.Marker(location=start_coords,popup="<i>Marker here<i>",tooltip="Latitude {}\nLongitude {}".format(rec.latitude,rec.longitude)).add_to(folium_map)
        cmap = folium_map._repr_html_()
        
        return jsonify({
            'map':cmap,
            'Country_short':rec.country_short,
            'Country_long': rec.country_long,
            'Region': rec.region,
            'City':rec.city,
            'ISP':rec.isp,
            'Domain':rec.domain,
            'Zipcode':rec.zipcode,
            'Timezone': rec.timezone
        })

@app.route('/ping')
def pinger():
    url = request.args['ip']
    message = ''
    error = ''
    valid_url = validators.url(url)
    if valid_url==True:
        print("Url is valid")
        message = 'Url is valid.'
        url = url.split('://')[1].split('/')[0]
        print(url)
        ip_add = s.gethostbyname(url)
        print('The IP Address of ' + url + ' is: '  + ip_add)
        script.pinger(ip_add)
    else:
        try:
            ip = ipaddress.ip_address(url)
            print('{} is a correct IP {} address.'.format(ip, ip.version))
            script.pinger(ip)
        except ValueError:
            error = 'Please enter a valid IP/URL'
    
    res={}
    if len(error.strip()) != 0:
        res['error'] = error
    else:
        res['message'] = message
    
    return jsonify(res)


@app.route('/subdomains')
def subdomains():
    url = request.args['ip']
    message = ''
    error = ''
    valid_url = validators.url(url)
    if valid_url==True:
        print("Url is valid")
        message = 'Url is valid.'
        script.subdomain(url)
    else:
        # try:
        #     ip = ipaddress.ip_address(url)
        #     print('{} is a correct IP {} address.'.format(ip, ip.version))
        # except ValueError:
        #     print('address/netmask is invalid')
        print("Invalid url")
        error = 'Please Try Entering a Valid Domain.'
    
    res={}
    if len(error.strip()) != 0:
        res['error'] = error
    else:
        res['message'] = message
    
    return jsonify(res)

@app.route('/portScanner')
def portScanner():
    url = request.args['ip']
    message = ''
    error = ''
    valid_url = validators.url(url)
    if valid_url==True:
        print("Url is valid")
        message = 'Url is valid.'
        url = url.split('://')[1].split('/')[0]
        print(url)
        ip_add = s.gethostbyname(url)
        print('The IP Address of ' + url + ' is: '  + ip_add)
        script.portScanner(ip_add)
    else:
        try:
            ip = ipaddress.ip_address(url)
            print('{} is a correct IP {} address.'.format(ip, ip.version))
            script.portScanner(ip)
        except ValueError:
            error = 'Please enter a valid IP/URL'
    
    res={}
    if len(error.strip()) != 0:
        res['error'] = error
    else:
        res['message'] = message
    
    return jsonify(res)


@app.route('/hopCounter')
def hopCounter():
    url = request.args['ip']
    message = ''
    error = ''
    valid_url = validators.url(url)
    if valid_url==True:
        print("Url is valid")
        message = 'Url is valid.'
        url = url.split('://')[1].split('/')[0]
        print(url)
        ip_add = s.gethostbyname(url)
        print('The IP Address of ' + url + ' is: '  + ip_add)
        script.hopCounter(ip_add)
    else:
        try:
            ip = ipaddress.ip_address(url)
            print('{} is a correct IP {} address.'.format(ip, ip.version))
            script.hopCounter(ip) 
        except ValueError:
            error = 'Please enter a valid IP/URL'
    
    res={}
    if len(error.strip()) != 0:
        res['error'] = error
    else:
        res['message'] = message
    
    return jsonify(res)

@app.route('/ipDns')
def ipDns():

    url = request.args['ip']
    message = ''
    error = ''
    valid_url = validators.url(url)
    if valid_url==True:
        print("Url is valid")
        message = 'Url is valid.'
        url = url.split('://')[1].split('/')[0]
        print(url)
        ip_add = s.gethostbyname(url)
        print('The IP Address of ' + url + ' is: '  + ip_add)
        script.ipDns(ip_add)
    else:
        try:
            ip = ipaddress.ip_address(url)
            print('{} is a correct IP {} address.'.format(ip, ip.version))
            script.ipDns(ip) 
        except ValueError:
            error = 'Please enter a valid IP/URL'
    
    res={}
    if len(error.strip()) != 0:
        res['error'] = error
    else:
        res['message'] = message
    
    return jsonify(res)

@app.route('/arp')
def arp():

    url = request.args['ip']
    message = ''
    error = ''
    valid_url = validators.url(url)
    if valid_url==True:
        print("Url is valid")
        message = 'Url is valid.'
        url = url.split('://')[1].split('/')[0]
        print(url)
        ip_add = s.gethostbyname(url)
        print('The IP Address of ' + url + ' is: '  + ip_add)
        script.arp(ip_add)
    else:
        try:
            ip = ipaddress.ip_address(url)
            print('{} is a correct IP {} address.'.format(ip, ip.version))
            script.arp(ip) 
        except ValueError:
            error = 'Please enter a valid IP/URL'
    
    res={}
    if len(error.strip()) != 0:
        res['error'] = error
    else:
        res['message'] = message
    
    return jsonify(res)

if __name__ =='__main__':
    app.run(debug=True)