# coding:
import main_model
import text_2_vec
import document_reading

vector_file_name = main_model.model_name + '_vectorized'
if __name__ == "__main__":
    model = text_2_vec.load_model(main_model.model_name)
    file = document_reading.load(main_model.save_name, "text_processed")
    for string in []:
        file.pop(string)
    key_list = []
    value_list = []
    for key, value in file.items():
        key_list.append(key)
        value_list.append(value)
    text_2_vec.save_to_memory(key_list=key_list, value_list=value_list, filename=vector_file_name, w2v_model=model)
