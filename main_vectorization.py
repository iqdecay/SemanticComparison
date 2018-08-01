import main_text_treatment
import text_2_vec
import document_io
import main_model

save_name = main_text_treatment.save_name
vector_file_name = save_name + '_vectorized_1000'
if __name__ == "__main__":
    model = text_2_vec.load_model('obj/models/{}'.format(save_name+'_model_1000'))
    file = document_io.load(main_model.save_name, "text_processed")
    for string in []:
        file.pop(string)
    key_list = []
    value_list = []
    for key, value in file.items():
        key_list.append(key)
        value_list.append(value)
    text_2_vec.save_to_memory(key_list=key_list, value_list=value_list, filename=vector_file_name, w2v_model=model)
