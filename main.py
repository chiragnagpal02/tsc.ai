import streamlit as st
import json
from io import StringIO
import pandas as pd
import googletrans


welcome = st.container()
info = st.container()

file_uploads = st.container()

with st.sidebar:
    st.title("Tictag.")

with welcome:
    st.title("Tictag - [TSC.ai]")
    st.text("In this Project we will be processing the\nconversion of tsc.ai input files into our required output files")


with info:
    st.header("About Project")
    st.text("TSC.ai gives us raw JSON files and our purpose is to convert them\nto english files so that we can upload onto admin panel quickly and easily.")



with file_uploads:
    st.header("Upload JSON file below")

    # base_directory = st.text_input("Enter base Directory")
    text_contents = "Hello, My, Name, Is, Chirag, nagpal"

    input_column_1, input_column_2 = st.columns(2)

    
    input_column_1.header("Language CSV")
    input_column_2.header("English Translations")
    

    value1 = input_column_1.file_uploader("File Upload", key=1, type="json")
    input_column_1.button("Upload!", key=100)

    value2 = input_column_2.file_uploader("File Upload", key=2, type="json")
    input_column_2.button("Upload!", key=200)

    # json_data = json.loads(value1)
    # print(json_data)
    string_add_1 = ""
    if value1 is not None:
        
        stringio = StringIO(value1.getvalue().decode("utf-8"))
        for i in stringio:
            # data = json.loads(str(i))
            # print(data)
            string_add_1 += str(i)
    
        json_data = json.loads(string_add_1)
        final_list_portuguese = []
        
        for item in json_data:
                temp_list = []
                words_to_highlight = item['target_spans']
                
                reference_id =  item["ref_id"]
                # language = item['language']
                try:
                    text = item["text"]
                except:
                    text = item['paragraphs']

                for i in words_to_highlight:
                    start = i['start']
                    end = i['end']
                    new_text = text[0:start] + "[" + text[start:]
                    final_text = new_text[0:end+1] + "]" + new_text[end+1:]
                    # temp_list.append(final_text)
                    # if language == "es":
                    #     final_list_spanish.append([reference_id, final_text])
                    # else:
                    # final_list_spanish.append([reference_id, final_text])
                    final_list_portuguese.append([reference_id, final_text])

        # for i in final_list_portuguese:
        #     print(i)
        # print(len(final_list_spanish))
        print(final_list_portuguese)

        df1 = pd.DataFrame(final_list_portuguese)
        vari = df1.to_csv(encoding="utf-8", header=False, index=False)
        st.write(df1)
        st.download_button('Download Language CSV', data=vari, mime='text/csv')

    string_add_2 = ""
    if value2 is not None:
        
        stringio = StringIO(value2.getvalue().decode("utf-8"))
        for i in stringio:
            # data = json.loads(str(i))
            # print(data)
            string_add_2 += str(i)
    
        json_data = json.loads(string_add_2)
        final_list_portuguese = []
        
        for item in json_data:
                temp_list = []
                words_to_highlight = item['target_spans']
                
                reference_id =  item["ref_id"]
                # language = item['language']

                try:
                    text = item["text"]
                except:
                    text = item['paragraphs']

                for i in words_to_highlight:
                    start = i['start']
                    end = i['end']
                    new_text = text[0:start] + "[" + text[start:]
                    final_text = new_text[0:end+1] + "]" + new_text[end+1:]
                    # temp_list.append(final_text)
                    # if language == "es":
                    #     final_list_spanish.append([reference_id, final_text])
                    # else:
                    # final_list_spanish.append([reference_id, final_text])
                    final_list_portuguese.append([reference_id, final_text])

        # for i in final_list_portuguese:
        #     print(i)
        # print(len(final_list_spanish))
        print(final_list_portuguese)

        one_column_csv = [i[1] for i in final_list_portuguese]
        count = 0
        english_translations_spanish_2500_3000 = []
        my_bar = st.progress(0)
        # cnt = 100/len(one_column_csv)
        st.write(f"Total Items to translate : {len(one_column_csv)}")
        st.write("Working ....")

        for j in one_column_csv:
            sentence = j
            translator = googletrans.Translator()

            #text1 = "LA HABANA, 2 sep (Reuters) - Cuba tachó de intervencionista e ilegal la financiación por parte de [Estados Unidos] de programas que buscan la promoción de la democracia"" que tienen en realidad como objetivo fomentar los disturbios para derrocar al gobierno de la isla, cuando la nación insular se enfrenta a su peor crisis económica en décadas, dijo el viernes el viceministro de Asuntos Exteriores cubano."

            english_translations_spanish_2500_3000.append(translator.translate(sentence).text)
            count += 1


            # my_bar.progress(cnt + (100/len(one_column_csv)))
        st.write(f"Done! Completed Translations for {len(one_column_csv)} items!")

        df1 = pd.DataFrame(english_translations_spanish_2500_3000)
        vari = df1.to_csv(encoding="utf-8", header=False, index=False)
        st.write(df1)
        st.download_button('Download English CSV', data=vari, mime='text/csv')
                
            
        
            


        

        
            

            

    

    
    

    
