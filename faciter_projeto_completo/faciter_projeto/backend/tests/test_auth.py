def test_cadastro_e_login(client):
    r = client.post('/auth/cadastro', json={'nome':'Ana','email':'ana@email.com','senha':'123456'})
    assert r.status_code == 201
    r = client.post('/auth/login', json={'email':'ana@email.com','senha':'123456'})
    assert r.status_code == 200
    assert 'access_token' in r.json()

def test_login_com_senha_incorreta(client):
    client.post('/auth/cadastro', json={'nome':'Ana','email':'ana@email.com','senha':'123456'})
    r = client.post('/auth/login', json={'email':'ana@email.com','senha':'errada'})
    assert r.status_code == 401
