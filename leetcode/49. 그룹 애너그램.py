# 1. sort와 딕셔너리를 이용해 같은 알파벳을 갖은것끼리 묶어준다.
# 2. 묶은것을 출력해준다.

def groupAnagrams(strs):    
        dict_words = {}
        # 1.
        for word in strs:
                sorted_word = "".join(sorted(word))
                if sorted_word in dict_words:
                        dict_words[sorted_word].append(word)
                else:   
                        dict_words[sorted_word] = [word]
        print(list(dict_words.values()))


strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)