# Load and save python object using the pickle module
import pickle
import os


def load(name, path):
    """
    Return the object contained in the file
    :param name: the name the file is saved under, without the .pkl extension
    :param path: the folder the file is in
    :return: the object contained in the file
    """
    print("Loading the object contained in obj/{}/{}.pkl ".format(path, name))
    try:
        with open("obj/{}/{}.pkl".format(path, name), 'rb') as f:
            print("Done")
            return pickle.load(f)
    except FileNotFoundError:
        raise FileNotFoundError('No such file exists')


def save(name, content, path, overwrite=False):
    """
    Save an object under the provided name in the folder "path", and overwrite the file if the file already exists
    :param name: under which the object will be saved
    :param content: the object that will be saved
    :param path: the folder in which it will be saved
    :param overwrite: force overwriting of already-existing files
    :return: None
    """
    # If the file exists, we can save the new version under a new name, or not save at all
    if overwrite or not os.path.exists("obj/{}/{}.pkl".format(path, name)):
        print("Saving the object under obj/{}/{}.pkl".format(path, name))
        with open("obj/{}/{}.pkl".format(path, name), 'wb') as f:
            pickle.dump(content, f, -1)
        print("Object saved successfully under obj/{}/{}.pkl".format(path, name))
        return None

    else:
        choice = str(input("Do you want to overwrite the following file: obj/{}/{}.pkl (Y/N) ? ".format(path, name)))
        if choice.lower() == "y":
            save(name, content, path, overwrite=True)
        else:
            new_name = input("Enter a new filename if you want to save, or 'N' to skip saving : ")
            if new_name.lower() != 'n':
                save(new_name, content, path, overwrite=True)
            else:
                print("No file saved !")
                return None
