const API='http://127.0.0.1:8000';
const token=()=>localStorage.getItem('faciter_token');
const headers=()=>({ 'Content-Type':'application/json', ...(token()?{'Authorization':`Bearer ${token()}`}:{}) });
const money=v=>Number(v).toLocaleString('pt-BR',{style:'currency',currency:'BRL'});

async function request(url, options={}){ const r=await fetch(API+url,{...options,headers:{...headers(),...(options.headers||{})}}); const data=r.status===204?null:await r.json(); if(!r.ok) throw new Error(data?.detail||'Erro na requisição'); return data; }

const login=document.querySelector('#loginForm');
if(login) login.addEventListener('submit',async e=>{e.preventDefault();const msg=document.querySelector('#msg');try{const data=await request('/auth/login',{method:'POST',body:JSON.stringify({email:email.value,senha:senha.value})});localStorage.setItem('faciter_token',data.access_token);location.href='imoveis.html';}catch(err){msg.textContent=err.message;}});

const cadastro=document.querySelector('#cadastroForm');
if(cadastro) cadastro.addEventListener('submit',async e=>{e.preventDefault();const msg=document.querySelector('#msg');try{await request('/auth/cadastro',{method:'POST',body:JSON.stringify({nome:nome.value,email:email.value,senha:senha.value,tipo:tipo.value})});msg.textContent='Cadastro realizado!';setTimeout(()=>location.href='login.html',700);}catch(err){msg.textContent=err.message;}});

async function carregarImoveis(){const lista=document.querySelector('#lista');if(!lista)return;try{const qs=new URLSearchParams();if(cidade.value)qs.set('cidade',cidade.value);if(tipo.value)qs.set('tipo',tipo.value);const itens=await request('/imoveis?'+qs);lista.innerHTML=itens.length?itens.map(i=>`<article class="property"><span>${i.tipo}</span><h3>${i.titulo}</h3><p>${i.cidade} - ${i.estado}</p><p>${i.quartos} quartos · ${i.banheiros} banheiros</p><strong>${money(i.preco)}</strong><p>${i.descricao}</p></article>`).join(''):'<p>Nenhum imóvel encontrado.</p>';}catch(err){lista.innerHTML=`<p>${err.message}. Verifique se a API está ligada.</p>`;}}
if(document.querySelector('#lista')){carregarImoveis();document.querySelector('#buscar').onclick=carregarImoveis;}

const form=document.querySelector('#imovelForm');
if(form) form.addEventListener('submit',async e=>{e.preventDefault();const msg=document.querySelector('#msg');try{await request('/imoveis',{method:'POST',body:JSON.stringify({titulo:titulo.value,preco:Number(preco.value),tipo:tipo.value,cidade:cidade.value,estado:estado.value.toUpperCase(),endereco:endereco.value,quartos:Number(quartos.value||0),banheiros:Number(banheiros.value||0),descricao:descricao.value})});msg.textContent='Imóvel cadastrado com sucesso!';form.reset();}catch(err){msg.textContent=err.message;}});

const user=document.querySelector('#usuario');if(user) request('/auth/me').then(u=>user.textContent=`Olá, ${u.nome}! Sua conta é do tipo ${u.tipo}.`).catch(()=>location.href='login.html');
document.querySelectorAll('#logout').forEach(b=>b.onclick=()=>{localStorage.removeItem('faciter_token');location.href='index.html';});
