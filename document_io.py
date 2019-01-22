# Load and save python object using the pickle module
import pickle
import os


def load(name):
    """
    Load the object
    :param name: the complete path relative to the cwd in which the object
    is saved
    :return: None
    """
    cwd = os.getcwd()
    if name[-4:] == ".pkl":
        name = name[:-4]
    complete_path = "{}/{}.pkl".format(cwd, name)
    try:
        print("Loading the object contained in ", complete_path)
        with open(complete_path, 'rb') as f:
            print("Done")
            return pickle.load(f)
    except FileNotFoundError:
        raise FileNotFoundError('No such file exists')


def save(name, content, path, overwrite=False):
    """
    Save the object under pickle form
    :param name: the name under which the object will be saved
    :param content: the Python object that will be saved
    :param path: the path, relative to the cwd
    :param overwrite: if True, overwrite the existing file
    :return: None
    """
    # If the file exists, we can save the new version under a new name, or not save at all
    if name[-4:] == ".pkl":
        name = name[:-4]
    cwd = os.getcwd()
    complete_path = "{}/{}/{}.pkl".format(cwd, path, name)
    if overwrite:
        print("Saving the object under ", complete_path)
        with open(complete_path, 'wb') as f:
            pickle.dump(content, f, -1)
        print("Object saved successfully under ", complete_path)
        return None

    if os.path.exists(complete_path):
        choice = str(input("Do you want to overwrite the following file: {} ".format(complete_path)))
        if choice.lower() == "y":
            print("Saving the object under {}".format(complete_path))
            with open(complete_path, 'wb') as f:
                pickle.dump(content, f, -1)
            print("Object saved successfully under ", complete_path)
        else:
            new_name = input("Enter a new filename if you want to save, or 'N' to skip saving : ")
            if new_name.lower() != 'n':
                save(new_name, content, path, overwrite=True)
            else:
                print("No file saved !")
                return None
    else:
        save(name, content, path, overwrite=True)
