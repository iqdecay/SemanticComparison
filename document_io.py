# Load and save python object using the pickle module
import pickle
import os


def load(name, path):
    """Load an object stored in name.pkl pickle file in the obj folder"""
    print("Loading the object contained in obj/{}/{}.pkl ".format(path, name))
    try:
        with open("obj/{}/{}.pkl".format(path, name), 'rb') as f:
            print("Object contained in obj/{}/{}.pkl sucessfully loaded".format(path, name))
            return pickle.load(f)
    except FileNotFoundError:
        raise FileNotFoundError('No such file exists')


def save(name, content, path, overwrite=False):
    """Save object content in name.pkl file in the obj/path folder, and overwrite if the parameter is True"""
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
