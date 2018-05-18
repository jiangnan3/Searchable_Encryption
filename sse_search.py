import pandas as pd
from Crypto.Cipher import AES
from Crypto.Hash import MD5
import time

def build_codeword(ID, trapdoor):
    ID_index = MD5.new()
    ID_index.update(str(ID))
    ECB_cipher = AES.new(trapdoor, AES.MODE_ECB)
    return ECB_cipher.encrypt(ID_index.digest()).encode("hex")

def search_index(document, trapdoor):
    search_result = []
    data_index = pd.read_csv(document)
    data_index = data_index.values
    start_time = time.time()
    for row in range(data_index.shape[0]):
        if build_codeword(row, trapdoor) in data_index[row]:
            search_result.append(row)

    print time.time() - start_time
    return search_result

if __name__ == "__main__":

    index_file_name = raw_input("Please input the index file you want to search:  ")
    keyword_trapdoor = raw_input("Please input the file stored the trapdoor you want to search:  ")
    keyword_trapdoor = open(keyword_trapdoor).read().strip()
    search_result = search_index(index_file_name, keyword_trapdoor)
    print "The identifiers of files that contain the keyword are: \n", search_result



