import streamlit as st

tasks = [ 
    {'sentence': 'THE BUZZ IN THE STREET _____ like the humming of flies.',
     'options' : [['was', 'is']], 
     'answers' : ['was'],
     'result'  : [''],
     'total'   : 0
    },
    
    {'sentence': 'Photographers _____ massed behind barriers patrolled by police, their long-snouted cameras poised, their breath rising like steam.',
     'options' : [['stood', 'were standing']], 
     'answers' : ['were standing'],
     'result'  : [''],
     'total'   : 0
    },
    
    {'sentence': 'Snow _____ steadily on to hats and shoulders; gloved fingers _____ lenses clear.',
     'options' : [['fell', 'had fallen'], ['wiped','were wiping']], 
     'answers' : ['fell', 'were wiping'],
     'result'  : ['', ''],
     'total'   : 0
    },
    
    {'sentence': 'From time to time there _____ outbreaks of desultory clicking, as the watchers _____ the waiting time by snapping the white canvas tent in the middle of the road, the entrance to the tall red-brick apartment block behind it, and the balcony on the top floor from which the body _____.',
     'options' : [['came', 'come'], ['filled', 'had filled'], ['had fallen', 'was falling']],
     'answers' : ['came', 'filled', 'had fallen'],
     'result'  : ['', '', ''],
     'total'   : 0
    }
]
    
st.header('Генератор упражнений по английскому')
st.subheader('Вставьте текст для создания упражнения')

st.text_area('nolabel', label_visibility="hidden")

'---'

st.subheader('Выберите правильные варианты пропущенных слов:')

for task in tasks:
    col1, col2 = st.columns(2)
    with col1:
        st.write('')
        st.write(str(task['sentence']))
        
    with col2:
        for i in range(len(task['options'])):
            option = task['options'][i]
            task['result'][i] = st.selectbox('nolabel', 
                                             ['–––'] + option, 
                                             label_visibility="hidden")
            if task['result'][i] == '–––':
                pass
            elif task['result'][i] == task['answers'][i]:
                st.success('', icon="✅")
            else:
                st.error('', icon="😟")
    task['total'] = task['result'] == task['answers']    
    '---'        

total_sum = sum(task['total'] for task in tasks)

if total_sum == len(tasks):
    st.success('Успех!')
    st.balloons()
    