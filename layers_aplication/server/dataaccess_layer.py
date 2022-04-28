import operator

def check_file(file_name):
    try:
        file = open(file_name, "r")
        return file, True
    except:
        return "", False

def count_words(file):
    n = 5 #n = number of top words I want to return
    #read file
    lines = file.read().split()
    #create a dict to process
    words_dict = {}
    for line in lines:
        if line in words_dict.keys():
            words_dict[line]+=1
        else:
            words_dict[line]=0
    #create the message and return it
    msg = ''
    for i in range(0,n):
        msg += max(words_dict.items(), key=operator.itemgetter(1))[0] + ": " + str(max(words_dict.items(), key=operator.itemgetter(1))[1]) + "\n"
        words_dict.pop(max(words_dict.items(), key=operator.itemgetter(1))[0])
    file.close()
    return msg


