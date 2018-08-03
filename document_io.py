# Load and save python object using the pickle module
import pickle
import os


def load(name, path):
    """
    Load the object
    :param name: the name under which the object is saved
    :param path: the subfolder of "obj" in which the object is saved
    :return: None
    """
    try:
        print("Loading the object contained in obj/{}/{}.pkl ".format(path, name))
        with open("obj/{}/{}.pkl".format(path, name), 'rb') as f:
            print("Done")
            return pickle.load(f)
    except FileNotFoundError:
        raise FileNotFoundError('No such file exists')


def save(name, content, path, overwrite=False):
    """
    Save the object under pickle form
    :param name: the name under which the object will be saved
    :param content: the Python object that will be saved
    :param path: the subfolder of "obj" in which the object will be saved
    :param overwrite: if True, overwrite the existing file
    :return: None
    """
    # If the file exists, we can save the new version under a new name, or not save at all
    if overwrite:
        print("Saving the object under obj/{}/{}.pkl".format(path, name))
        with open("obj/{}/{}.pkl".format(path, name), 'wb') as f:
            pickle.dump(content, f, -1)
        print("Object saved successfully under obj/{}/{}.pkl".format(path, name))
        return None

    if os.path.exists("obj/{}/{}.pkl".format(path, name)):
        choice = str(input("Do you want to overwrite the following file: obj/{}/{}.pkl (Y/N) ? ".format(path, name)))
        if choice.lower() == "y":
            print("Saving the object under obj/{}/{}.pkl".format(path, name))
            with open("obj/{}/{}.pkl".format(path, name), 'wb') as f:
                pickle.dump(content, f, -1)
            print("Object saved successfully under obj/{}/{}.pkl".format(path, name))
        else:
            new_name = input("Enter a new filename if you want to save, or 'N' to skip saving : ")
            if new_name.lower() != 'n':
                save(new_name, content, path, overwrite=True)
            else:
                print("No file saved !")
                return None
    else:
        print("Saving the object under obj/{}/{}.pkl".format(path, name))
        with open("obj/{}/{}.pkl".format(path, name), 'wb') as f:
            pickle.dump(content, f, -1)
        print("Object saved successfully under obj/{}/{}.pkl".format(path, name))
