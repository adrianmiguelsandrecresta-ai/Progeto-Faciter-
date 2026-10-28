def token(client, email='ana@email.com'):
    client.post('/auth/cadastro', json={'nome':'Ana','email':email,'senha':'123456'})
    return client.post('/auth/login', json={'email':email,'senha':'123456'}).json()['access_token']

def imovel():
    return {'titulo':'Casa Faciter','descricao':'Casa confortável para família','preco':350000,'tipo':'casa','cidade':'Bauru','estado':'SP','endereco':'Rua Exemplo, 100','quartos':3,'banheiros':2}

def test_crud_imovel(client):
    t = token(client); h={'Authorization':f'Bearer {t}'}
    r=client.post('/imoveis',json=imovel(),headers=h); assert r.status_code==201
    item=r.json(); assert item['cidade']=='Bauru'
    assert client.get('/imoveis').status_code==200
    item['preco']=360000
    assert client.put(f"/imoveis/{item['id']}",json=item,headers=h).status_code==200
    assert client.delete(f"/imoveis/{item['id']}",headers=h).status_code==204

def test_nao_pode_alterar_imovel_de_outro_usuario(client):
    t1=token(client); t2=token(client,'bruno@email.com')
    r=client.post('/imoveis',json=imovel(),headers={'Authorization':f'Bearer {t1}'})
    iid=r.json()['id']
    r=client.put(f'/imoveis/{iid}',json=imovel(),headers={'Authorization':f'Bearer {t2}'})
    assert r.status_code==403
