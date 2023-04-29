import streamlit as st

st.title('Olá, Heleno!!')


st.sidebar.title('Menu Aplicações')
pagina_selecionada = st.sidebar.selectbox('Selecione que aplicação você quer usar', ['Leitor', 'Removedor'])

if pagina_selecionada == 'Leitor':

    st.write('Esse projeto surgiu de um problema que eu estava passando por conta da preguiça de ter que acessar a minha IDE para visualizar o script de um programa.')
    st.write('Como estou manipulando esses arquivos o tempo inteiro e estou 100% do tempo com o navegador aberto, pensei: "Por que não criar uma aplicação que mostra o código para mim apenas upando o meu arquivo"?')
    st.write('Acabei me empolgando um pouco e adicionei a opção de upar imagens e vídeos/áudios, mas a função principal ainda é ler scripts.')

    arquivo = st.file_uploader (
    'Vamos lá! Upe seu arquivo aqui!',
type = ['py', 'jpg','png','wav', 'js','txt', 'css']
)

    if arquivo:
        print(arquivo.type)
        match arquivo.type.split('/'):
            case 'image', _:
                st.image(arquivo)
            case 'text', 'css':
                st.code(arquivo.read().decode())
            case 'text', 'x-python':
                st.code(arquivo.read().decode())
            case 'audio', _:
                st.audio(arquivo)
                st.video(arquivo)

elif pagina_selecionada == 'Removedor':
    st.write('Sobre esse não tem muito o que dizer, na verdade, é mais um lugar pra fugir dos anúncios dos sites de remover fundo :)')
    st.write('Ainda estou desenvolvendo, mas não vai dar tempo até a entrega do trabalho :(')
    st.write(' Logo estará por aqui!!')
