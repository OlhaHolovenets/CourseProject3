import requests

key = '1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL'
ENDPOINT = 'http://164.92.218.36:8080/api'

def test_can_call_endpoint():
    response_call = requests.get(ENDPOINT, auth=(key, ''))
    assert response_call.status_code == 200
    print(response_call)


def test_can_create():
    payload = """<?xml version="1.0" encoding="UTF-8"?>
    <prestashop 
        xmlns:xlink="http://www.w3.org/1999/xlink">    
        <address>
            <id></id>
            <id_customer></id_customer>
            <id_manufacturer></id_manufacturer>
            <id_supplier></id_supplier>
            <id_warehouse></id_warehouse>
            <id_country xlink:href="http://164.92.218.36:8080/api/countries/1">1</id_country>
            <id_state></id_state>
            <alias>12</alias>
            <company></company>
            <lastname>hol</lastname>
            <firstname>olha</firstname>
            <vat_number></vat_number>
            <address1>Stepana Bandery ave 20</address1>
            <address2></address2>
            <postcode>04209</postcode>
            <city>Kyiv</city>
            <other></other>
            <phone></phone>
            <phone_mobile></phone_mobile>
            <dni></dni>
            <deleted></deleted>
            <date_add></date_add>
            <date_upd></date_upd>
        </address>
    </prestashop>"""
    response = requests.post(ENDPOINT+'/addresses', headers={'Content-Type': 'application/xml'},
                             auth=(key, ''), data=payload)
    assert response.status_code == 201
    print(response.text)
    global address_id
    address_id = response.text.split('id')[1][slice(10, -5)]
    print(address_id)
    assert address_id.isdigit(), "returned id was not correct"


def test_get_url():
    response_get = requests.get(ENDPOINT+'/addresses/'+address_id, auth=(key, ''))
    print(response_get.url)
    print(response_get.text)


def test_can_update():
    payload = f"""<?xml version="1.0" encoding="UTF-8"?>
    <prestashop 
        xmlns:xlink="http://www.w3.org/1999/xlink">    
        <address>
            <id>{address_id}</id>
            <id_customer></id_customer>
            <id_manufacturer></id_manufacturer>
            <id_supplier></id_supplier>
            <id_warehouse></id_warehouse>
            <id_country xlink:href="http://164.92.218.36:8080/api/countries/1">1</id_country>
            <id_state></id_state>
            <alias>12</alias>
            <company></company>
            <lastname>hol</lastname>
            <firstname>olha</firstname>
            <vat_number></vat_number>
            <address1>Khreshchatyk</address1>
            <address2></address2>
            <postcode>04209</postcode>
            <city>Kyiv</city>
            <other></other>
            <phone></phone>
            <phone_mobile></phone_mobile>
            <dni></dni>
            <deleted></deleted>
            <date_add></date_add>
            <date_upd></date_upd>
        </address>
    </prestashop>"""
    response = requests.put(ENDPOINT+'/addresses', headers={'Content-Type': 'application/xml'},
                            auth=(key, ''), data=payload)
    print(response.text)


def test_can_delete():
    response = requests.delete(ENDPOINT+'/addresses/'+address_id,
                               headers={'Content-Type': 'application/xml'}, auth=(key, ''))
    assert response.status_code == 200
    print(response.text)