#importar
import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image, ImageDraw
import time
import base64
from streamlit_modal import Modal
import random
                
# imagem de fundo
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image):
    bin_str = get_base64_of_bin_file(image)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url('data:image/png;base64,%s');
        background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
background_image_path = "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\fundo.png"
set_background(background_image_path)

#Criar colunas
col1, col2,col11,col22= st.columns(4)
col3, col4= st.columns(2)
col5, col6, col7, col8= st.columns(4)
cola, colb, colc= st.columns(3)

#Variáveis
if 'rerun' not in st.session_state:
    st.session_state['rerun'] = 0

if 'tirar' not in st.session_state:
    st.session_state['tirar'] = 0
if 'tirar1' not in st.session_state:
    st.session_state['tirar1'] = 0


if 'Nivel1' not in st.session_state:
    st.session_state['Nivel1'] = 0
if 'Nivel3' not in st.session_state:
    st.session_state['Nivel3'] = 0
if 'Nivel5' not in st.session_state:
    st.session_state['Nivel5'] = 0
if 'Nivel7' not in st.session_state:
    st.session_state['Nivel7'] = 0
if 'Nivel2' not in st.session_state:
    st.session_state['Nivel2'] = 0
if 'Nivel4' not in st.session_state:
    st.session_state['Nivel4'] = 0
if 'Nivel6' not in st.session_state:
    st.session_state['Nivel6'] = 0
    
if 'menu' not in st.session_state:
    st.session_state['menu'] = 0
if 'menu1' not in st.session_state:
    st.session_state['menu1'] = 1

#Número de diferenças que se começa
if 'ndicas' not in st.session_state:
    st.session_state['ndicas'] = 3

#logotipo
with col1:
    logo= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\logo.jpg"
    logo1 = Image.open(logo)
    new_size2 = (40, 30)
    logo_imagem = logo1.resize(new_size2)
    st.image(logo_imagem)

#Título
with col3:
    if st.session_state['tirar'] == 0:
        st.title("Spot n' Shot")
        st.write("Niveis:")
        
#Botão "AJUDA"
if st.session_state['menu1'] == 1:
    if st.session_state['tirar'] == 0:
            if st.button("Ajuda"):
                
                st.title("Ajuda")
                st.write("O jogo Spot n' Shot é um jogo no qual o seu objetivo é encontrar as diferenças das imagens")
                st.write("No jogo à medida que avançamos no nível a dificuldade do jogo aumenta, aumentando a dificuldade das diferenças e as dicas não sendo tão óbvias")
                st.write("Consegue-se dicas encontrando todas as diferenças do nível em menos da metade do tempo dado")
                st.write("Se não conseguir encontrar todas as diferenças no tempo dado perde")
                if st.button("Voltar"):
                    st.experimental_rerun()

#Botão "Nível 1"            
if st.session_state['menu1'] == 1:
    if st.session_state['tirar'] == 0:
        with col5:
            if st.button("1"):
                st.session_state['Nivel5'] = 1
                st.session_state['tirar'] = 1
                st.experimental_rerun()
            
    if st.session_state['Nivel5'] == 1:
        if 'começar' not in st.session_state:
            st.session_state['começar'] = 0

        if st.session_state['tirar1'] == 0:
            if st.button("Começar"):
                st.session_state['começar']=1
                st.session_state['tirar1'] = 1
                st.session_state['random']=random.randint(0,1)
                
        if st.session_state['começar']==1:
            if st.session_state['random']==0:
                with col1:
                    st.title("Nivel 1")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                if 'achou5' not in st.session_state:
                    st.session_state['achou5'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0
                if 'diferença5' not in st.session_state:
                    st.session_state['diferença5'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0
                with col1:    
                    st.write("clique aqui:")
                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel5o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 400)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")
                    
                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel5a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>75 and valor["x"]<105 and valor["y"]>233 and valor["y"]<243:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>232 and valor["x"]<252 and valor["y"]>247 and valor["y"]<272:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>162 and valor["x"]<175 and valor["y"]>78 and valor["y"]<99:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>224 and valor["x"]<238 and valor["y"]>82 and valor["y"]<95:
                        st.session_state['diferença4'] = 1
                        
                    if valor["x"]>60 and valor["x"]<77 and valor["y"]>30 and valor["y"]<40:
                        st.session_state['diferença5'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 89, 237 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 242, 263  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 169, 89  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 232, 88  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                            
                    if st.session_state['diferença5']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 69, 35  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou5']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou5']=st.session_state['achou5']+1

                with col4:
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/5")
                    
                if st.session_state['diferenças_achadas']==5:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                st.write("Falta alguma coisa no casaco do menino")
                            elif st.session_state['achou2']==0:
                                st.write("Falta alguma coisa no vestido da menina")
                            elif st.session_state['achou3']==0:
                                st.write("Falta uma orelha na menina")
                            elif st.session_state['achou4']==0:
                                st.write("Falta uma sobrancelha na menina")
                            elif st.session_state['achou5']==0:
                                st.write("Falta alguma coisa no chapéu do menino")
                            
                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['achou5'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['diferença5'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()

                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel5'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel5'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel5'] = 0
                            st.session_state['Nivel2'] = 1
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()
                            
                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                            st.success("perdeu")
                    
        if st.session_state['começar']==1:
            if st.session_state['random']==1:
                with col1:
                    st.title("Nivel 1")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                if 'achou5' not in st.session_state:
                    st.session_state['achou5'] = 0
                if 'achou6' not in st.session_state:
                    st.session_state['achou6'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0
                if 'diferença5' not in st.session_state:
                    st.session_state['diferença5'] = 0
                if 'diferença6' not in st.session_state:
                    st.session_state['diferença6'] = 0
                    
                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0
                    
                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel6o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 300)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel6a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>167 and valor["x"]<188 and valor["y"]>20 and valor["y"]<54:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>197 and valor["x"]<215 and valor["y"]>23 and valor["y"]<44:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>226 and valor["x"]<236 and valor["y"]>54 and valor["y"]<62:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>50 and valor["x"]<70 and valor["y"]>65 and valor["y"]<85:
                        st.session_state['diferença4'] = 1
                        
                    if valor["x"]>82 and valor["x"]<94 and valor["y"]>131 and valor["y"]<142:
                        st.session_state['diferença5'] = 1
                        
                    if valor["x"]>96 and valor["x"]<111 and valor["y"]>237 and valor["y"]<255:
                        st.session_state['diferença6'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 177, 38
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 206, 33  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 231, 59  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 60, 75  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                            
                    if st.session_state['diferença5']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 87, 137  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou5']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou5']=st.session_state['achou5']+1

                    if st.session_state['diferença6']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 103, 246  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou6']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou6']=st.session_state['achou6']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/6")
                    
                if st.session_state['diferenças_achadas']==6:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                st.write("Olhe para os cornos da rena")
                            elif st.session_state['achou2']==0:
                                st.write("Olhe para o gorro de natal")
                            elif st.session_state['achou3']==0:
                                st.write("Olhe para as estrelas")
                            elif st.session_state['achou4']==0:
                                st.write("Olhe para o coração")
                            elif st.session_state['achou5']==0:
                                st.write("Falta uma estrela")
                            elif st.session_state['achou6']==0:
                                st.write("Olhe para a caixa de presente")
                            
                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['achou5'] = 0
                        st.session_state['achou6'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['diferença5'] = 0
                        st.session_state['diferença6'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()
                        
                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel5'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel5'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel5'] = 0
                            st.session_state['Nivel2'] = 1
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")

if st.session_state['menu1'] == 1:
    if st.session_state['tirar'] == 0:
        with col6:
            if st.button("2"):
                st.session_state['Nivel2'] = 1
                st.session_state['tirar'] = 1
                st.experimental_rerun()
        
    if st.session_state['Nivel2'] == 1:
        if 'começar' not in st.session_state:
            st.session_state['começar'] = 0

        if st.session_state['tirar1'] == 0:
            if st.button("Começar"):
                st.session_state['começar']=1
                st.session_state['tirar1'] = 1
                st.session_state['random']=random.randint(0,1)
                
        if st.session_state['começar']==1:
            if st.session_state['random']==0:    
                with col1:
                    st.title("Nivel 2")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0    

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                if 'achou5' not in st.session_state:
                    st.session_state['achou5'] = 0
                if 'achou6' not in st.session_state:
                    st.session_state['achou6'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0
                if 'diferença5' not in st.session_state:
                    st.session_state['diferença5'] = 0
                if 'diferença6' not in st.session_state:
                    st.session_state['diferença6'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0
                    
                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel13o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (240, 300)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel13a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>49 and valor["x"]<63 and valor["y"]>58 and valor["y"]<72:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>58 and valor["x"]<100 and valor["y"]>79 and valor["y"]<110:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>114 and valor["x"]<138 and valor["y"]>161 and valor["y"]<176:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>136 and valor["x"]<168 and valor["y"]>201 and valor["y"]<221:
                        st.session_state['diferença4'] = 1
                        
                    if valor["x"]>111 and valor["x"]<128 and valor["y"]>252 and valor["y"]<263:
                        st.session_state['diferença5'] = 1
                        
                    if valor["x"]>198 and valor["x"]<212 and valor["y"]>262 and valor["y"]<275:
                        st.session_state['diferença6'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 55, 65
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 65, 82  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 126, 168  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 150, 211  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                            
                    if st.session_state['diferença5']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 120, 258 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou5']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou5']=st.session_state['achou5']+1

                    if st.session_state['diferença6']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 205, 269 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou6']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou6']=st.session_state['achou6']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/6")
                    
                if st.session_state['diferenças_achadas']==6:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                dica.write("")
                            elif st.session_state['achou2']==0:
                                dica.write("")
                            elif st.session_state['achou3']==0:
                                dica.write("")
                            elif st.session_state['achou4']==0:
                                dica.write("")
                            elif st.session_state['achou5']==0:
                                dica.write("")
                            elif st.session_state['achou6']==0:
                                dica.write("")

                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['achou5'] = 0
                        st.session_state['achou6'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['diferença5'] = 0
                        st.session_state['diferença6'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()
                        
                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel2'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel2'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel2'] = 0
                            st.session_state['Nivel4'] = 1
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()
               
                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")

            if st.session_state['random']==1:            
                with col1:
                    st.title("Nivel 2")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                if 'achou5' not in st.session_state:
                    st.session_state['achou5'] = 0
                if 'achou6' not in st.session_state:
                    st.session_state['achou6'] = 0
                if 'achou7' not in st.session_state:
                    st.session_state['achou7'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0
                if 'diferença5' not in st.session_state:
                    st.session_state['diferença5'] = 0
                if 'diferença6' not in st.session_state:
                    st.session_state['diferença6'] = 0
                if 'diferença7' not in st.session_state:
                    st.session_state['diferença7'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0

                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel14o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 400)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel14a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>113 and valor["x"]<140 and valor["y"]>138 and valor["y"]<148:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>179 and valor["x"]<197 and valor["y"]>171 and valor["y"]<182:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>118 and valor["x"]<154 and valor["y"]>218 and valor["y"]<237:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>250 and valor["x"]<275 and valor["y"]>127 and valor["y"]<159:
                        st.session_state['diferença4'] = 1
                        
                    if valor["x"]>164 and valor["x"]<186 and valor["y"]>198 and valor["y"]<215:
                        st.session_state['diferença5'] = 1
                        
                    if valor["x"]>136 and valor["x"]<153 and valor["y"]>273 and valor["y"]<283 or valor["x"]>203 and valor["x"]<220 and valor["y"]>240 and valor["y"]<250:
                        st.session_state['diferença6'] = 1

                    if valor["x"]>118 and valor["x"]<207 and valor["y"]>363 and valor["y"]<390:
                        st.session_state['diferença7'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 127, 154
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 188, 176  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 134, 227  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 260, 135  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                            
                    if st.session_state['diferença5']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 175, 208  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou5']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou5']=st.session_state['achou5']+1

                    if st.session_state['diferença6']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 144,278 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou6']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou6']=st.session_state['achou6']+1

                    if st.session_state['diferença7']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 150,380  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou7']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou7']=st.session_state['achou7']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/7")
                    
                if st.session_state['diferenças_achadas']==7:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                st.write("")
                            elif st.session_state['achou2']==0:
                                st.write("")
                            elif st.session_state['achou3']==0:
                                st.write("")
                            elif st.session_state['achou4']==0:
                                st.write("")
                            elif st.session_state['achou5']==0:
                                st.write("")
                            elif st.session_state['achou6']==0:
                                st.write("")
                            elif st.session_state['achou7']==0:
                                st.write("")  
                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                            
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['achou5'] = 0
                        st.session_state['achou6'] = 0
                        st.session_state['achou7'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['diferença5'] = 0
                        st.session_state['diferença6'] = 0
                        st.session_state['diferença7'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()
                
                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel2'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel2'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel2'] = 0
                            st.session_state['Nivel4'] = 1
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()
        
                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")
                            

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")

if st.session_state['menu1'] == 1:
    if st.session_state['tirar'] == 0:
        with col7:
            if st.button("3"):
                st.session_state['Nivel4'] = 1
                st.session_state['tirar'] = 1
                st.experimental_rerun()
        
    if st.session_state['Nivel4'] == 1:
        if 'começar' not in st.session_state:
            st.session_state['começar'] = 0

        if st.session_state['tirar1'] == 0:
            if st.button("Começar"):
                st.session_state['começar']=1
                st.session_state['tirar1'] = 1
                st.session_state['random']=random.randint(0,1)
                
        if st.session_state['começar']==1:
            if st.session_state['random']==0:    
                with col1:
                    st.title("Nivel 3")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0    

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                if 'achou5' not in st.session_state:
                    st.session_state['achou5'] = 0
                if 'achou6' not in st.session_state:
                    st.session_state['achou6'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0
                if 'diferença5' not in st.session_state:
                    st.session_state['diferença5'] = 0
                if 'diferença6' not in st.session_state:
                    st.session_state['diferença6'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0
                    
                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel12o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 300)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel12a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>91 and valor["x"]<168 and valor["y"]>124 and valor["y"]<147:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>118 and valor["x"]<135 and valor["y"]>168 and valor["y"]<182:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>35 and valor["x"]<52 and valor["y"]>278 and valor["y"]<292:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>171 and valor["x"]<186 and valor["y"]>249 and valor["y"]<268:
                        st.session_state['diferença4'] = 1
                        
                    if valor["x"]>186 and valor["x"]<200 and valor["y"]>192 and valor["y"]<206:
                        st.session_state['diferença5'] = 1
                        
                    if valor["x"]>250 and valor["x"]<266 and valor["y"]>226 and valor["y"]<235:
                        st.session_state['diferença6'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 125, 135
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 127, 175  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 44, 285  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 178, 258  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                            
                    if st.session_state['diferença5']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 193, 199 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou5']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou5']=st.session_state['achou5']+1

                    if st.session_state['diferença6']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 258, 230 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou6']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou6']=st.session_state['achou6']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/6")
                    
                if st.session_state['diferenças_achadas']==6:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                dica.write("")
                            elif st.session_state['achou2']==0:
                                dica.write("")
                            elif st.session_state['achou3']==0:
                                dica.write("")
                            elif st.session_state['achou4']==0:
                                dica.write("")
                            elif st.session_state['achou5']==0:
                                dica.write("")
                            elif st.session_state['achou6']==0:
                                dica.write("")

                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['achou5'] = 0
                        st.session_state['achou6'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['diferença5'] = 0
                        st.session_state['diferença6'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()
                        
                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel4'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel4'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel4'] = 0
                            st.session_state['Nivel3'] = 1
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()
               
                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")

            if st.session_state['random']==1:            
                with col1:
                    st.title("Nivel 3")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                if 'achou5' not in st.session_state:
                    st.session_state['achou5'] = 0
                if 'achou6' not in st.session_state:
                    st.session_state['achou6'] = 0
                if 'achou7' not in st.session_state:
                    st.session_state['achou7'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0
                if 'diferença5' not in st.session_state:
                    st.session_state['diferença5'] = 0
                if 'diferença6' not in st.session_state:
                    st.session_state['diferença6'] = 0
                if 'diferença7' not in st.session_state:
                    st.session_state['diferença7'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0

                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel11o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 300)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel11a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>108 and valor["x"]<126 and valor["y"]>33 and valor["y"]<54:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>93 and valor["x"]<119 and valor["y"]>66 and valor["y"]<103:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>195 and valor["x"]<215 and valor["y"]>184 and valor["y"]<200:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>78 and valor["x"]<97 and valor["y"]>99 and valor["y"]<122:
                        st.session_state['diferença4'] = 1
                        
                    if valor["x"]>134 and valor["x"]<147 and valor["y"]>144 and valor["y"]<161:
                        st.session_state['diferença5'] = 1
                        
                    if valor["x"]>199 and valor["x"]<213 and valor["y"]>137 and valor["y"]<151:
                        st.session_state['diferença6'] = 1

                    if valor["x"]>134 and valor["x"]<154 and valor["y"]>188 and valor["y"]<215:
                        st.session_state['diferença7'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 117, 44
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 110, 84  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 205, 192  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 88, 111  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                            
                    if st.session_state['diferença5']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 140, 151  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou5']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou5']=st.session_state['achou5']+1

                    if st.session_state['diferença6']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 207,145 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou6']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou6']=st.session_state['achou6']+1

                    if st.session_state['diferença7']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 143,199  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou7']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou7']=st.session_state['achou7']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/7")
                    
                if st.session_state['diferenças_achadas']==7:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                st.write("")
                            elif st.session_state['achou2']==0:
                                st.write("")
                            elif st.session_state['achou3']==0:
                                st.write("")
                            elif st.session_state['achou4']==0:
                                st.write("")
                            elif st.session_state['achou5']==0:
                                st.write("")
                            elif st.session_state['achou6']==0:
                                st.write("")
                            elif st.session_state['achou7']==0:
                                st.write("")  
                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                            
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['achou5'] = 0
                        st.session_state['achou6'] = 0
                        st.session_state['achou7'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['diferença5'] = 0
                        st.session_state['diferença6'] = 0
                        st.session_state['diferença7'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()
                
                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel4'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel4'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel4'] = 0
                            st.session_state['Nivel3'] = 1
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()
        
                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")
                            

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")

if st.session_state['menu1'] == 1:
    if st.session_state['tirar'] == 0:
        with col5:
            if st.button("4"):
                st.session_state['Nivel3'] = 1
                st.session_state['tirar'] = 1
                st.experimental_rerun()
                
    if st.session_state['Nivel3'] == 1:
        if 'começar' not in st.session_state:
            st.session_state['começar'] = 0

        if st.session_state['tirar1'] == 0:
            if st.button("Começar"):
                st.session_state['começar']=1
                st.session_state['tirar1'] = 1
                st.session_state['random']=random.randint(0,1)
                
        if st.session_state['começar']==1:
            if st.session_state['random']==0:   
            
                with col1:
                    st.title("Nivel 4")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0
             
                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel3o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 400)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel3a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>115 and valor["x"]<132 and valor["y"]>104 and valor["y"]<138:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>173 and valor["x"]<193 and valor["y"]>144 and valor["y"]<155:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>284 and valor["x"]<300 and valor["y"]>143 and valor["y"]<161:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>205 and valor["x"]<216 and valor["y"]>111 and valor["y"]<124:
                        st.session_state['diferença4'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 125, 120 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 182, 147  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 292, 153  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 210, 116  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/4")
                    
                if st.session_state['diferenças_achadas']==4:
                    st.session_state['win']=1
                    
                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                st.write("Falta-lhe um brinco")
                            elif st.session_state['achou2']==0:
                                st.write("Olhe para os olhos do gato")
                            elif st.session_state['achou3']==0:
                                st.write("Falta luz num prédio")
                            elif st.session_state['achou4']==0:
                                st.write("Falta-lhe uma sobrancelha")    
                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()

                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel3'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel3'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel3'] = 0
                            st.session_state['Nivel6'] = 1
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")
                          
            if st.session_state['random']==1:
                with col1:
                    st.title("Nivel 4")
                    
                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0

                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel4o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 400)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel4a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>37 and valor["x"]<59 and valor["y"]>147 and valor["y"]<167:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>208 and valor["x"]<229 and valor["y"]>70 and valor["y"]<91:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>250 and valor["x"]<262 and valor["y"]>170 and valor["y"]<187:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>244 and valor["x"]<298 and valor["y"]>270 and valor["y"]<280:
                        st.session_state['diferença4'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 48, 157 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 218, 80  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 256, 179  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 270, 275  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/4")
                    
                if st.session_state['diferenças_achadas']==4:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                st.write("Falta sardas ao Freddy")
                            elif st.session_state['achou2']==0:
                                st.write("Falta cabelo ao Foxy")
                            elif st.session_state['achou3']==0:
                                st.write("A vela está de outra cor")
                            elif st.session_state['achou4']==0:
                                st.write("Faltam as tarraxas na guitarra")
                            
                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                with cola:         
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()
                        
                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel3'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()
                            
                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel3'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel3'] = 0
                            st.session_state['Nivel6'] = 1
                            st.session_state['começar4']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")   

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")

if st.session_state['menu1'] == 1:
    if st.session_state['tirar'] == 0:
        with col6:
            if st.button("5"):
                st.session_state['Nivel6'] = 1
                st.session_state['tirar'] = 1
                st.experimental_rerun()
        
    if st.session_state['Nivel6'] == 1:
        if 'começar' not in st.session_state:
            st.session_state['começar'] = 0

        if st.session_state['tirar1'] == 0:
            if st.button("Começar"):
                st.session_state['começar'] = 1
                st.session_state['tirar1'] = 1
                st.session_state['random']=random.randint(0,1)
                
        if st.session_state['começar']==1:
            if st.session_state['random']==0:    
                with col1:
                    st.title("Nivel 5")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                if 'achou5' not in st.session_state:
                    st.session_state['achou5'] = 0
                if 'achou6' not in st.session_state:
                    st.session_state['achou6'] = 0
                if 'achou7' not in st.session_state:
                    st.session_state['achou7'] = 0
                if 'achou8' not in st.session_state:
                    st.session_state['achou8'] = 0
                if 'achou9' not in st.session_state:
                    st.session_state['achou9'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0
                if 'diferença5' not in st.session_state:
                    st.session_state['diferença5'] = 0
                if 'diferença6' not in st.session_state:
                    st.session_state['diferença6'] = 0
                if 'diferença7' not in st.session_state:
                    st.session_state['diferença7'] = 0
                if 'diferença8' not in st.session_state:
                    st.session_state['diferença8'] = 0
                if 'diferença9' not in st.session_state:
                    st.session_state['diferença9'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0

                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel10o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 370)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel10a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>48 and valor["x"]<72 and valor["y"]>30 and valor["y"]<52:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>127 and valor["x"]<149 and valor["y"]>45 and valor["y"]<77:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>208 and valor["x"]<225 and valor["y"]>100 and valor["y"]<109:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>253 and valor["x"]<271 and valor["y"]>119 and valor["y"]<130:
                        st.session_state['diferença4'] = 1
                        
                    if valor["x"]>131 and valor["x"]<148 and valor["y"]>151 and valor["y"]<165:
                        st.session_state['diferença5'] = 1
                        
                    if valor["x"]>168 and valor["x"]<188 and valor["y"]>229 and valor["y"]<247:
                        st.session_state['diferença6'] = 1

                    if valor["x"]>189 and valor["x"]<220 and valor["y"]>332 and valor["y"]<347:
                        st.session_state['diferença7'] = 1

                    if valor["x"]>13 and valor["x"]<48 and valor["y"]>163 and valor["y"]<195:
                        st.session_state['diferença8'] = 1

                    if valor["x"]>75 and valor["x"]<89 and valor["y"]>184 and valor["y"]<210:
                        st.session_state['diferença9'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 67, 42
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 140, 54  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 217, 105  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 260, 122
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                            
                    if st.session_state['diferença5']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 139, 155 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou5']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou5']=st.session_state['achou5']+1

                    if st.session_state['diferença6']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 179,246 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou6']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou6']=st.session_state['achou6']+1

                    if st.session_state['diferença7']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 201,341  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou7']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou7']=st.session_state['achou7']+1

                    if st.session_state['diferença8']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 33,178  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou8']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou8']=st.session_state['achou8']+1

                    if st.session_state['diferença9']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 84,199  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou9']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou9']=st.session_state['achou9']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/9")
                    
                if st.session_state['diferenças_achadas']==9:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                st.write("")
                            elif st.session_state['achou2']==0:
                                st.write("")
                            elif st.session_state['achou3']==0:
                                st.write("")
                            elif st.session_state['achou4']==0:
                                st.write("")
                            elif st.session_state['achou5']==0:
                                st.write("")
                            elif st.session_state['achou6']==0:
                                st.write("")
                            elif st.session_state['achou7']==0:
                                st.write("")
                            elif st.session_state['achou8']==0:
                                st.write("")
                            elif st.session_state['achou9']==0:
                                st.write("")
                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                            
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['achou5'] = 0
                        st.session_state['achou6'] = 0
                        st.session_state['achou7'] = 0
                        st.session_state['achou8'] = 0
                        st.session_state['achou9'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['diferença5'] = 0
                        st.session_state['diferença6'] = 0
                        st.session_state['diferença7'] = 0
                        st.session_state['diferença8'] = 0
                        st.session_state['diferença9'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()
                
                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['achou8'] = 0
                            st.session_state['achou9'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['diferença8'] = 0
                            st.session_state['diferença9'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel6'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['achou8'] = 0
                            st.session_state['achou9'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['diferença8'] = 0
                            st.session_state['diferença9'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel6'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel6'] = 0
                            st.session_state['Nivel7'] = 1
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['achou8'] = 0
                            st.session_state['achou9'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['diferença8'] = 0
                            st.session_state['diferença9'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()
        
                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")
                            

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")

            if st.session_state['random']==1:            
                with col1:
                    st.title("Nivel 5")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                if 'achou5' not in st.session_state:
                    st.session_state['achou5'] = 0
                if 'achou6' not in st.session_state:
                    st.session_state['achou6'] = 0
                if 'achou7' not in st.session_state:
                    st.session_state['achou7'] = 0
                if 'achou8' not in st.session_state:
                    st.session_state['achou8'] = 0
                if 'achou9' not in st.session_state:
                    st.session_state['achou9'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0
                if 'diferença5' not in st.session_state:
                    st.session_state['diferença5'] = 0
                if 'diferença6' not in st.session_state:
                    st.session_state['diferença6'] = 0
                if 'diferença7' not in st.session_state:
                    st.session_state['diferença7'] = 0
                if 'diferença8' not in st.session_state:
                    st.session_state['diferença8'] = 0
                if 'diferença9' not in st.session_state:
                    st.session_state['diferença9'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0

                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel9o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 370)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel9a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>22 and valor["x"]<45 and valor["y"]>185 and valor["y"]<196:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>1 and valor["x"]<21 and valor["y"]>213 and valor["y"]<222:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>93 and valor["x"]<107 and valor["y"]>201 and valor["y"]<210:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>168 and valor["x"]<180 and valor["y"]>188 and valor["y"]<198:
                        st.session_state['diferença4'] = 1
                        
                    if valor["x"]>214 and valor["x"]<226 and valor["y"]>117 and valor["y"]<130:
                        st.session_state['diferença5'] = 1
                        
                    if valor["x"]>223 and valor["x"]<236 and valor["y"]>219 and valor["y"]<252:
                        st.session_state['diferença6'] = 1

                    if valor["x"]>94 and valor["x"]<155 and valor["y"]>318 and valor["y"]<367:
                        st.session_state['diferença7'] = 1

                    if valor["x"]>6 and valor["x"]<28 and valor["y"]>321 and valor["y"]<332:
                        st.session_state['diferença8'] = 1

                    if valor["x"]>5 and valor["x"]<18 and valor["y"]>115 and valor["y"]<134:
                        st.session_state['diferença9'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 24, 189
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 6, 218  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 99, 206  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 173, 195
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                            
                    if st.session_state['diferença5']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 219, 122  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou5']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou5']=st.session_state['achou5']+1

                    if st.session_state['diferença6']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 228,246 
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou6']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou6']=st.session_state['achou6']+1

                    if st.session_state['diferença7']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 103,328  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou7']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou7']=st.session_state['achou7']+1
                    if st.session_state['diferença7']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 145,359  
                        raio = 10
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)

                    if st.session_state['diferença8']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 18,325  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou8']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou8']=st.session_state['achou8']+1
                            
                    if st.session_state['diferença9']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 11,125  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou9']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou9']=st.session_state['achou9']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/9")
                    
                if st.session_state['diferenças_achadas']==9:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                st.write("")
                            elif st.session_state['achou2']==0:
                                st.write("")
                            elif st.session_state['achou3']==0:
                                st.write("")
                            elif st.session_state['achou4']==0:
                                st.write("")
                            elif st.session_state['achou5']==0:
                                st.write("")
                            elif st.session_state['achou6']==0:
                                st.write("")
                            elif st.session_state['achou7']==0:
                                st.write("")
                            elif st.session_state['achou8']==0:
                                st.write("")
                            elif st.session_state['achou9']==0:
                                st.write("")
                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                            
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['achou5'] = 0
                        st.session_state['achou6'] = 0
                        st.session_state['achou7'] = 0
                        st.session_state['achou8'] = 0
                        st.session_state['achou9'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['diferença5'] = 0
                        st.session_state['diferença6'] = 0
                        st.session_state['diferença7'] = 0
                        st.session_state['diferença8'] = 0
                        st.session_state['diferença9'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()
                
                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['achou8'] = 0
                            st.session_state['achou9'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['diferença8'] = 0
                            st.session_state['diferença9'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel6'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['achou8'] = 0
                            st.session_state['achou9'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['diferença8'] = 0
                            st.session_state['diferença9'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel6'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel6'] = 0
                            st.session_state['Nivel7'] = 1
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['achou8'] = 0
                            st.session_state['achou9'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['diferença8'] = 0
                            st.session_state['diferença9'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()
        
                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")
                            

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")

if st.session_state['menu1'] == 1:
    if st.session_state['tirar'] == 0:
        with col7:
            if st.button("6"):
                st.session_state['Nivel7'] = 1
                st.session_state['tirar'] = 1
                st.experimental_rerun()
        
    if st.session_state['Nivel7'] == 1:
        if 'começar' not in st.session_state:
            st.session_state['começar'] = 0

        if st.session_state['tirar1'] == 0:
            if st.button("Começar"):
                st.session_state['começar']=1
                st.session_state['tirar1'] = 1
                st.session_state['random']=random.randint(0,1)
                
        if st.session_state['começar']==1:
            if st.session_state['random']==0:    
                with col1:
                    st.title("Nivel 6")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0    

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                if 'achou5' not in st.session_state:
                    st.session_state['achou5'] = 0
                if 'achou6' not in st.session_state:
                    st.session_state['achou6'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0
                if 'diferença5' not in st.session_state:
                    st.session_state['diferença5'] = 0
                if 'diferença6' not in st.session_state:
                    st.session_state['diferença6'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0
                    
                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel7o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 300)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel7a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>236 and valor["x"]<246 and valor["y"]>18 and valor["y"]<25:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>147 and valor["x"]<163 and valor["y"]>125 and valor["y"]<135:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>146 and valor["x"]<166 and valor["y"]>191 and valor["y"]<204:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>164 and valor["x"]<174 and valor["y"]>244 and valor["y"]<254:
                        st.session_state['diferença4'] = 1
                        
                    if valor["x"]>56 and valor["x"]<86 and valor["y"]>25 and valor["y"]<34:
                        st.session_state['diferença5'] = 1
                        
                    if valor["x"]>236 and valor["x"]<255 and valor["y"]>155 and valor["y"]<173:
                        st.session_state['diferença6'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 241, 21
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 154, 130  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 154, 201  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 169, 249  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                            
                    if st.session_state['diferença5']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 60, 30  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou5']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou5']=st.session_state['achou5']+1

                    if st.session_state['diferença6']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 245, 164  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou6']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou6']=st.session_state['achou6']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/6")
                    
                if st.session_state['diferenças_achadas']==6:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndica1']>0:
                            if st.session_state['achou1']==0:
                                st.write("Falta alguma coisa no 3ºgato")
                            elif st.session_state['achou2']==0:
                                st.write("Falta alguma coisa no 5ºgato")
                            elif st.session_state['achou3']==0:
                                st.write("Falta alguma coisa no 8ºgato")
                            elif st.session_state['achou4']==0:
                                st.write("Falta alguma coisa no 11ºgato")
                            elif st.session_state['achou5']==0:
                                st.write("Olhe para o primeiro gato branco")
                            elif st.session_state['achou6']==0:
                                st.write("Falta alguma coisa no 9ºgato")

                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['achou5'] = 0
                        st.session_state['achou6'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['diferença5'] = 0
                        st.session_state['diferença6'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()
                        
                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel7'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel7'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel7'] = 0
                            st.session_state['Nivel1'] = 1
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()
               
                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")

            if st.session_state['random']==1:            
                with col1:
                    st.title("Nivel 6")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                if 'achou5' not in st.session_state:
                    st.session_state['achou5'] = 0
                if 'achou6' not in st.session_state:
                    st.session_state['achou6'] = 0
                if 'achou7' not in st.session_state:
                    st.session_state['achou7'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0
                if 'diferença5' not in st.session_state:
                    st.session_state['diferença5'] = 0
                if 'diferença6' not in st.session_state:
                    st.session_state['diferença6'] = 0
                if 'diferença7' not in st.session_state:
                    st.session_state['diferença7'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0

                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel8o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 400)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel8a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>202 and valor["x"]<214 and valor["y"]>41 and valor["y"]<53:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>170 and valor["x"]<182 and valor["y"]>123 and valor["y"]<135:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>136 and valor["x"]<144 and valor["y"]>177 and valor["y"]<185:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>216 and valor["x"]<233 and valor["y"]>325 and valor["y"]<357:
                        st.session_state['diferença4'] = 1
                        
                    if valor["x"]>271 and valor["x"]<300 and valor["y"]>307 and valor["y"]<375:
                        st.session_state['diferença5'] = 1
                        
                    if valor["x"]>50 and valor["x"]<66 and valor["y"]>216 and valor["y"]<227:
                        st.session_state['diferença6'] = 1
                        
                    if valor["x"]>280 and valor["x"]<296 and valor["y"]>47 and valor["y"]<72:
                        st.session_state['diferença7'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 208, 47
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 176, 129  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 139, 181  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 224, 343  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                            
                    if st.session_state['diferença5']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 285, 340  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou5']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou5']=st.session_state['achou5']+1

                    if st.session_state['diferença6']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 61,221  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou6']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou6']=st.session_state['achou6']+1

                    if st.session_state['diferença7']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 288,60  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou7']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou7']=st.session_state['achou7']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/7")
                    
                if st.session_state['diferenças_achadas']==7:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                st.write("Falta o sorriso na 3ªbolacha")
                            elif st.session_state['achou2']==0:
                                st.write("No canto superior direito falta um botão na bolacha")
                            elif st.session_state['achou3']==0:
                                st.write("Falta um olho na 10ºbolacha")
                            elif st.session_state['achou4']==0:
                                st.write("Falta desenhos na penúltima bolacha")
                            elif st.session_state['achou5']==0:
                                st.write("No canto inferior direito o formato da bolacha é diferente")
                            elif st.session_state['achou6']==0:
                                st.write("Falta um botão na 9ªbolacha")
                            elif st.session_state['achou7']==0:
                                st.write("Falta um botão na 4ªbolacha")
                                
                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                            
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['achou5'] = 0
                        st.session_state['achou6'] = 0
                        st.session_state['achou7'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['diferença5'] = 0
                        st.session_state['diferença6'] = 0
                        st.session_state['diferença7'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()
                
                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel7'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel7'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with colc:
                        if st.button("PROXIMO"):
                            st.session_state['Nivel7'] = 0
                            st.session_state['Nivel1'] = 1
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['achou5'] = 0
                            st.session_state['achou6'] = 0
                            st.session_state['achou7'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['diferença5'] = 0
                            st.session_state['diferença6'] = 0
                            st.session_state['diferença7'] = 0
                            st.session_state['ndica1'] = 0
                            st.experimental_rerun()
        
                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")

                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")
                            

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")
                    
if st.session_state['menu1'] == 1:
    if st.session_state['tirar'] == 0:
        with col5:
            if st.button("7"):
                st.session_state['Nivel1'] = 1
                st.session_state['tirar'] = 1
                st.experimental_rerun()
                
    if st.session_state['Nivel1'] == 1:
        #Botão "Começar"        
        if 'começar1' not in st.session_state:
            st.session_state['começar1'] = 0

        if st.session_state['tirar1'] == 0:
            if st.button("Começar"):
                st.session_state['começar1']=1
                st.session_state['tirar1'] = 1
                st.session_state['random']=random.randint(0,1)

        if st.session_state['começar1']==1:
            if st.session_state['random']==0:
                #Tílulo    
                with col1:
                    st.title("Nivel 7")

                #Variaveis guardadas   
                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0
                if 'dica' not in st.session_state:
                    st.session_state['dica'] = 0

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0
                    
                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0

                #Imagem original
                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel1o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (275, 375)
                resized_image = original_image1.resize(new_size)

                    
                with col3:
                    #coordenadas    
                    valor = streamlit_image_coordinates(resized_image, key="pil")
                    
                    #Imagem alterada
                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel1a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                #Coordenadas das diferenças    
                else:
                    if valor["x"]>90 and valor["x"]<117 and valor["y"]>192 and valor["y"]<222:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>117 and valor["x"]<127 and valor["y"]>85 and valor["y"]<100:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>160 and valor["x"]<220 and valor["y"]>65 and valor["y"]<80:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>120 and valor["x"]<130 and valor["y"]>145 and valor["y"]<155:
                        st.session_state['diferença4'] = 1
                        
                #Coordenadas dos círculos        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 100, 200  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 120, 90  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 190, 72  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 125, 150  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                            
                #Mostrar imagem alterada                            
                with col4:    
                    st.image(resized_image2)
                    
                #Diferenças achadas
                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/4")
                    
                #Ganhar  
                if st.session_state['diferenças_achadas']==4:
                    st.session_state['win']=1
                    
                #Usar dica
                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                                
                    #Dicas        
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:
                            if st.session_state['achou1']==0:
                                st.write("Olhe para as calças")
                            elif st.session_state['achou2']==0:
                                st.write("Olhe para o colar")
                            elif st.session_state['achou3']==0:
                                st.write("Olhe para as escadas")
                            elif st.session_state['achou4']==0:
                                st.write("Olhe para a barriga")    
                        else :
                            st.write("Não tem dicas")    
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                #Recomeçar
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar1'] = 0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()

                #MENU            
                if st.session_state['win']==0: 
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar1']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel1'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()
                    

                #Mostra que ganhou    
                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")
                #Reinicia        
                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar1']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel1'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()
                               
                #Tempo
                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        #Perder
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        #Ganhar dica
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")

                #Mostrar que perdeu    
                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                            st.success("perdeu")
        

            if st.session_state['random']==1:  
                with col1:
                    st.title("Nivel 7")

                if 'usadica' not in st.session_state:
                    st.session_state['usadica'] = 0

                if 'tempo' not in st.session_state:
                    st.session_state['tempo'] = 1*60

                if 'diferenças_achadas' not in st.session_state:
                    st.session_state['diferenças_achadas'] = 0 
                    
                if 'achou1' not in st.session_state:
                    st.session_state['achou1'] = 0
                if 'achou2' not in st.session_state:
                    st.session_state['achou2'] = 0
                if 'achou3' not in st.session_state:
                    st.session_state['achou3'] = 0
                if 'achou4' not in st.session_state:
                    st.session_state['achou4'] = 0
                    
                if 'win' not in st.session_state:
                    st.session_state['win'] = 0

                if 'lose' not in st.session_state:
                    st.session_state['lose'] = 0
                    
                if 'diferença1' not in st.session_state:
                    st.session_state['diferença1'] = 0
                if 'diferença2' not in st.session_state:
                    st.session_state['diferença2'] = 0
                if 'diferença3' not in st.session_state:
                    st.session_state['diferença3'] = 0
                if 'diferença4' not in st.session_state:
                    st.session_state['diferença4'] = 0

                if 'ndica1' not in st.session_state:
                    st.session_state['ndica1'] = 0

                imagem1= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel2o.jpg"
                original_image1 = Image.open(imagem1)
                new_size = (300, 375)
                resized_image = original_image1.resize(new_size)
                    
                with col3:
                    valor = streamlit_image_coordinates(resized_image, key="pil")

                    imagem2= "C:\\Users\\dinis\\OneDrive\\Ambiente de Trabalho\\jogo_das_diferencas\\Nivel2a.jpg"
                    original_image2 = Image.open(imagem2)
                    resized_image2 = original_image2.resize(new_size)
                    
                if valor is None:
                    st.write("")
                    
                else:
                    if valor["x"]>175 and valor["x"]<200 and valor["y"]>295 and valor["y"]<305:
                        st.session_state['diferença1'] = 1
                        
                    if valor["x"]>110 and valor["x"]<126 and valor["y"]>265 and valor["y"]<277:
                        st.session_state['diferença2'] = 1
                        
                    if valor["x"]>222 and valor["x"]<235 and valor["y"]>250 and valor["y"]<260:
                        st.session_state['diferença3'] = 1
                        
                    if valor["x"]>180 and valor["x"]<195 and valor["y"]>85 and valor["y"]<105:
                        st.session_state['diferença4'] = 1
                        
                if st.session_state['lose'] == 0:
                    if st.session_state['diferença1']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 187, 300  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou1']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou1']=st.session_state['achou1']+1
                            
                    if st.session_state['diferença2']==1:     
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 120, 270  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou2']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou2']=st.session_state['achou2']+1

                    if st.session_state['diferença3']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 230, 255  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou3']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou3']=st.session_state['achou3']+1
                            
                    if st.session_state['diferença4']==1:
                        draw = ImageDraw.Draw(resized_image2)
                        x, y = 190, 95  
                        raio = 10  
                        draw.ellipse([(x - raio, y - raio), (x + raio, y + raio)], outline="green", width=2)
                        if st.session_state['achou4']==0:
                            st.session_state['diferenças_achadas']=st.session_state['diferenças_achadas']+1
                            st.session_state['achou4']=st.session_state['achou4']+1
                                    
                with col4:    
                    st.image(resized_image2)

                with col5: 
                    st.write("Diferenças",st.session_state['diferenças_achadas'],"/4")
                    
                if st.session_state['diferenças_achadas']==4:
                    st.session_state['win']=1

                with col5:
                    if st.session_state['win']==0:
                        st.write("Dicas:",st.session_state['ndicas'])
                        if st.session_state['usadica']==0:
                            if st.button("Usar dica"):
                                st.session_state['usadica']=1
                                st.experimental_rerun()
                            
                    if st.session_state['usadica']==1:    
                        if st.session_state['ndicas']>0:    
                            if st.session_state['achou1']==0:
                                st.write("Falta a marca da mota na parte de baixo da mota")
                            elif st.session_state['achou2']==0:
                                st.write("Falta uma marca perto da roda traseira")
                            elif st.session_state['achou3']==0:
                                st.write("Falta uma marca perto da roda dianteira")
                            elif st.session_state['achou4']==0:
                                st.write("Falta alguma coisa na coluna")
                            
                            
                        else :
                            st.write("Não tem dicas")
                            
                        if st.session_state['ndicas']>0 and st.session_state['ndica1']==0:
                            st.session_state['ndicas']=st.session_state['ndicas']-1
                            st.session_state['ndica1']=1
                with cola:
                    if st.button("recomeçar"):
                        st.session_state['começar1']=0
                        st.session_state['tirar1'] = 0
                        st.session_state['usadica'] = 0
                        st.session_state['dica'] = 0
                        st.session_state['tempo'] = 1*60
                        st.session_state['diferenças_achadas'] = 0 
                        st.session_state['achou1'] = 0
                        st.session_state['achou2'] = 0
                        st.session_state['achou3'] = 0
                        st.session_state['achou4'] = 0
                        st.session_state['win'] = 0
                        st.session_state['lose'] = 0
                        st.session_state['diferença1'] = 0
                        st.session_state['diferença2'] = 0
                        st.session_state['diferença3'] = 0
                        st.session_state['diferença4'] = 0
                        st.session_state['ndica1'] = 0
                        st.experimental_rerun()
                        
                if st.session_state['win']==0:
                    with col22:
                        if st.button("MENU"):
                            st.session_state['começar']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel1'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()
                        
                if st.session_state['win']==1:
                    with colb:
                        if st.button("MENU"):
                            st.session_state['começar1']=0
                            st.session_state['tirar1'] = 0
                            st.session_state['usadica'] = 0
                            st.session_state['dica'] = 0
                            st.session_state['tempo'] = 1*60
                            st.session_state['diferenças_achadas'] = 0 
                            st.session_state['achou1'] = 0
                            st.session_state['achou2'] = 0
                            st.session_state['achou3'] = 0
                            st.session_state['achou4'] = 0
                            st.session_state['win'] = 0
                            st.session_state['lose'] = 0
                            st.session_state['diferença1'] = 0
                            st.session_state['diferença2'] = 0
                            st.session_state['diferença3'] = 0
                            st.session_state['diferença4'] = 0
                            st.session_state['ndica1'] = 0
                            st.session_state['menu1'] = 1
                            st.session_state['Nivel1'] = 0
                            st.session_state['tirar'] = 0
                            st.experimental_rerun()

                if st.session_state['win']==1:
                    with col5:
                        st.success("ganhou")
                        
                with col8:
                    if st.session_state['win']==0:
                        ph = st.empty()
                        for secs in range(st.session_state['tempo'],0,-1):
                            st.session_state['tempo']=st.session_state['tempo']-1
                            mm = secs//60
                            ss = secs%60
                            ph.write(f"{mm:02d}:{ss:02d}")
                            time.sleep(1)
                            st.experimental_rerun()
                        st.session_state['lose'] = 1
                    else:
                        mm = st.session_state['tempo']//60
                        ss = st.session_state['tempo']%60
                        st.write(f"{mm:02d}:{ss:02d}")
                        if st.session_state['tempo']>30:
                            st.session_state['ndicas']=st.session_state['ndicas']+1    
                            st.success("+1 dica")

                if st.session_state['win']== 0 and st.session_state['lose']== 1:
                    with col5:
                        st.success("perdeu")

