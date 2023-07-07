import html

def format_options(row):
    
    if row['type'] == 'select_word':
        answer = row['answer']
        onchange = f"myFunction('{answer}', 's{row.name}', 'p{row.name}')"
        html_open = f'<select class="form-select" id="s{row.name}" onchange="{onchange}"><option selected>–––</option>'
        html_close = '</select>'
        options = ''.join([f'<option value=\"{row["options"][i]}\">{row["options"][i]}</option>' 
                           for i in range(len(row['options']))])
        dropdown = html_open + options + html_close
        return dropdown
        
    if row['type'] == 'noun_phrases':
        answer = row['answer']
        onchange = f"myFunction('{answer}', 's{row.name}', 'p{row.name}')"
        phrase = f'<strong>{row["object"]}</strong> '
        html_open = f'<select class="form-select" id="s{row.name}" onchange="{onchange}"><option selected>–––</option>'
        html_close = '</select>'
        options = ''.join([f'<option value=\"{row["options"][i]}\">{row["options"][i]}</option>' 
                           for i in range(len(row['options']))])
        dropdown = phrase + html_open + options + html_close
        return dropdown
        
    if row['type'] == 'select_sent':
        answer = row['answer'].replace("'", '\&apos;').replace('"','\&quot;')
        # options = row['options']
        options = [opt.replace("'", '&apos;').replace('"','&quot;') for opt in row['options']]
        html_open = '<div class="form-check">'
        html_close = '</label></div>'
        input_class = f'input class="form-check-input" type="radio"'
        label_class = f'label class="form-check-label"'
        dropdown = ''.join([f'''{html_open}
                               <{input_class} id="r{row.name}-{i}" name="rname{row.name}" 
                                 onchange=\'myFunction(\"{answer}\", \"r{row.name}-{i}\", \"p{row.name}\")\'
                                 value=\"{options[i]}\">
                               <{label_class} for="r{row.name}-{i}">{row['options'][i]}
                               {html_close}'''
                            for i in range(len(row['options']))]) 
        return dropdown
        
    if row['type'] == 'missing_word':
        answer = row['answer']
        onchange = f"myFunction('{answer}', 't{row.name}', 'p{row.name}')"
        input_field = f'<input class="form-control" type="text" id="t{row.name}" onchange="{onchange}">'
        return input_field

