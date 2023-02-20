import requests

key = '1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL'
ENDPOINT = 'http://164.92.218.36:8080/api'

def test_can_call_endpoint():
    response_call = requests.get(ENDPOINT, auth=(key, ''))
    assert response_call.status_code == 200
    print(response_call)


def test_can_create():
    body = """<?xml version="1.0" encoding="UTF-8"?>
    <prestashop 
        xmlns:xlink="http://www.w3.org/1999/xlink">
        <category>
            <id_parent>0</id_parent>
            <active>0</active>
            <id_shop_default></id_shop_default>
            <is_root_category></is_root_category>
            <position></position>
            <date_add></date_add>
            <date_upd></date_upd>
            <name><language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Bags</language></name>
            <link_rewrite>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
            </link_rewrite>
            <description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
            </description>
            <meta_title>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
            </meta_title>
            <meta_description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
            </meta_description>
            <meta_keywords>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
            </meta_keywords>
            <associations>
            <categories nodeType="category" api="categories"/>
            <products nodeType="product" api="products"/>
            </associations>
        </category>
    </prestashop>"""
    response = requests.post(ENDPOINT+'/categories', headers={'Content-Type': 'application/xml'},
                             auth=(key, ''), data=body)
    assert response.status_code == 201
    print(response.text)
    global category_id
    category_id = response.text.split('id')[1][slice(10, -5)]
    print(category_id)
    assert category_id.isdigit(), "returned id was not correct"


def test_get_url():
    response_get = requests.get(ENDPOINT+'/categories/'+category_id, auth=(key, ''))
    print(response_get.url)
    print(response_get.text)


def test_can_update():
    body = f"""<?xml version="1.0" encoding="UTF-8"?>
    <prestashop x
        mlns:xlink="http://www.w3.org/1999/xlink">
        <category>
            <id>{category_id}</id>
            <id_parent>0</id_parent>
            <active>0</active>
            <id_shop_default></id_shop_default>
            <is_root_category></is_root_category>
            <position></position>
            <date_add></date_add>
            <date_upd></date_upd>
            <name><language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Backpacks</language></name>
            <link_rewrite>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
            </link_rewrite>
            <description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Backpacks for travelling</language>
            </description>
            <meta_title>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
            </meta_title>
            <meta_description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
            </meta_description>
            <meta_keywords>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
            </meta_keywords>
            <associations>
            <categories nodeType="category" api="categories"/>
            <products nodeType="product" api="products"/>
            </associations>
        </category>
    </prestashop>"""
    response = requests.put(ENDPOINT+'/categories', headers={'Content-Type': 'application/xml'},
                            auth=(key, ''), data=body)
    assert response.status_code == 405
    print(response.text)


def test_can_delete():
    response = requests.delete(ENDPOINT+'/categories/'+category_id,
                               headers={'Content-Type': 'application/xml'}, auth=(key, ''))
    assert response.status_code == 405
    print(response.text)