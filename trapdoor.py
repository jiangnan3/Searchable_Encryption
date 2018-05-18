from Crypto.Cipher import AES
from Crypto.Hash import MD5


def build_trapdoor(MK, keyword):
    keyword_index = MD5.new()
    keyword_index.update(str(keyword))
    ECB_cipher = AES.new(MK, AES.MODE_ECB)
    return ECB_cipher.encrypt(keyword_index.digest())

if __name__ == "__main__":

    keyword = raw_input("Please input the keyword you want to search:  ")

    master_key_file_name = raw_input("Please input the file stored the master key:  ")
    master_key = open(master_key_file_name).read()
    if len(master_key) > 16:
        print "the length of master key is larger than 16 bytes, only the first 16 bytes are used"
        master_key = bytes(master_key[:16])


    trapdoor_file = open(keyword + "_trapdoor", "w+")
    trapdoor_of_keyword = build_trapdoor(master_key, keyword)
    trapdoor_file.write(trapdoor_of_keyword)
    trapdoor_file.close()