import streamlit as st

select_options = [ 
    [['was', 'is']],
    [['stood', 'were standing']],
    [['fell', 'had fallen'], ['wiped','were wiping']],
    [['came', 'come'], ['filled', 'had filled'], ['had fallen', 'was falling']]
]
    
answers = [
    [1],
    [0],
    [1,0],
    [0,1,0]
]
  
sentences = [
    'THE BUZZ IN THE STREET _____ like the humming of flies.',
    'Photographers _____ massed behind barriers patrolled by police, their long-snouted cameras poised, their breath rising like steam.',
    'Snow _____ steadily on to hats and shoulders; gloved fingers _____ lenses clear.',
    'From time to time there _____ outbreaks of desultory clicking, as the watchers _____ the waiting time by snapping the white canvas tent in the middle of the road, the entrance to the tall red-brick apartment block behind it, and the balcony on the top floor from which the body _____.'
]

st.header('Генератор упражнений по английскому')
st.subheader('Вставьте текст для создания упражнения')

st.text_area('nolabel', label_visibility="hidden")

'---'

st.subheader('Выберите правильные варианты пропущенных слов:')

res = [0,0,0,0,0]

for i in range(len(sentences)):
    col1, col2 = st.columns(2)
    with col1:
        st.write('')
        st.write('')
        st.write(str(sentences[i]))

    with col2:
        for k in range(len(select_options[i])):
            option = select_options[i][k]
            answ = st.selectbox('nolabel', 
                                   ['–––'] + option, 
                                   key = str(i) + '_'.join(option),
                                   label_visibility="hidden")
        if answ == '–––':
            pass
        elif answ == option[answers[i][k]]:
            st.success('', icon="✅")
            res[i] = 1
        else:
            st.error('', icon="😟")
            res[i] = 0
    '---'

if sum(res) == len(sentences):
    st.success('Успех!')
    st.balloons()
    