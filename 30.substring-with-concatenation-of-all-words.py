#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        ori_word_count = {}
        for word in words:
            ori_word_count[word] = ori_word_count.get(word, 0) + 1

        all_word_len = word_len * len(words)


        res = []
        for i in range(word_len):
            word_count = ori_word_count.copy()
            queue = []
            for j in range(i, len(s) - word_len + 1, word_len):
                cur_word = s[j:j + word_len]
                if word_count.get(cur_word, 0) > 0:
                    word_count[cur_word] -= 1
                    queue.append(cur_word)
                    if sum(word_count.values()) == 0:
                        res.append(j - all_word_len + word_len)
                        first_word = queue[0]
                        queue = queue[1:]
                        word_count[first_word] = word_count.get(first_word, 0) + 1
                else:
                    while(queue):
                        first_word = queue[0]
                        queue = queue[1:]
                        if cur_word == first_word:
                            queue.append(cur_word)
                            break
                        else:
                            word_count[first_word] = word_count.get(first_word, 0) + 1
        return res



                
        # word_len = len(words[0])
        # word_count = {}
        # for word in words:
        #     word_count[word] = word_count.get(word, 0) + 1
        # all_word_len = word_len * len(words)
        # res = []

        # for i in range(word_len):
        #     my_queue = []
        #     word_dict = word_count.copy()
        #     for j in range(i, len(s) - word_len + 1, word_len):
        #         word = s[j: j+word_len]
        #         if word_dict.get(word, 0) > 0:
        #             my_queue.append(word)
        #             word_dict[word] -= 1
        #             if sum(word_dict.values()) == 0:
        #                 res.append(j - all_word_len + word_len)
        #                 last_word = my_queue[0]
        #                 my_queue = my_queue[1:]
        #                 word_dict[last_word] = word_dict.get(last_word, 0) + 1
        #         else:
        #             while my_queue:
        #                 last_word = my_queue[0]
        #                 my_queue = my_queue[1:]
        #                 if word == last_word:
        #                     my_queue.append(last_word)
        #                     break
        #                 else:
        #                     word_dict[last_word] = word_dict.get(last_word, 0) + 1


        # return res












# @lc code=end

