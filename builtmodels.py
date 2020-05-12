from loadJson import load_json_data
from createSVM import create_SVM_Model
if __name__ == "__main__":
    data_path = " data.json"
    print("\n --- CREATING SVM ---")
    create_SVM_Model(load_json_data(data_path))
