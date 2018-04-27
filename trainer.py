# encoding=utf-8

import numpy as np
import pickle
import re


class Trainer(object):
    def __init__(self):
        self.total_hanzi = 10000
        self.total_pinyin = 500
        self.encode_hanzi = {}
        self.encode_pinyin = {}
        self.decode_hanzi = {}
        self.decode_pinyin = {}
        self.trans_mat = np.zeros((self.total_hanzi, self.total_hanzi))
        self.gen_mat = np.zeros((self.total_hanzi, self.total_pinyin))
        self.hanzi_fre = np.zeros(self.total_hanzi)
        self.pinyin2hanzi = {}

    def __read_pinyin(self, path):
        with open(path, encoding="utf-8") as f:
            idx_hanzi = 0
            idx_pinyin = 0
            for line in f.readlines():
                pinyin = line.split(":")[0]
                self.encode_pinyin.update({pinyin: idx_pinyin})
                idx_pinyin = idx_pinyin + 1

                hanzis = line.split(":")[1].replace("\n", "")

                for hanzi in hanzis:
                    if self.encode_hanzi.get(hanzi) is None:
                        self.encode_hanzi.update({hanzi: idx_hanzi})
                        idx_hanzi = idx_hanzi + 1
                    tmp_idx_pinyin = self.encode_pinyin[pinyin]
                    tmp_idx_hanzi = self.encode_hanzi[hanzi]
                    self.gen_mat[tmp_idx_hanzi, tmp_idx_pinyin] = self.gen_mat[tmp_idx_hanzi, tmp_idx_pinyin] + 1
                    if self.pinyin2hanzi.get(tmp_idx_pinyin) is None:
                        self.pinyin2hanzi.update({tmp_idx_pinyin: [tmp_idx_hanzi]})
                    else:
                        self.pinyin2hanzi[tmp_idx_pinyin].append(tmp_idx_hanzi)

        # Crop the matrix
        self.total_hanzi = idx_hanzi
        self.total_pinyin = idx_pinyin
        self.trans_mat = self.trans_mat[0:self.total_hanzi, 0:self.total_hanzi]
        self.gen_mat = self.gen_mat[0:self.total_hanzi, 0:self.total_pinyin]

        # Normalize
        self.gen_mat /= np.sum(self.gen_mat, axis=1).reshape((-1, 1))

    def __read_trans(self, path):
        with open(path, encoding="utf-8") as f:

            for line in f.readlines():
                lamps = re.split(r"|。|（|）|，|：|”|“|、", line)
                for lamp in lamps:
                    words_last = [x for x in lamp]
                    words_last.pop(-1)
                    words = words_last[1:]
                    words_last.pop(-1)
                    assert (len(words_last) == len(words))

                    for i in range(len(words_last)):
                        idx_last = self.encode_hanzi.get(words_last[i])
                        idx_now = self.encode_hanzi.get(words[i])
                        if idx_last is None or idx_now is None:
                            continue
                        self.trans_mat[idx_last, idx_now] = self.trans_mat[idx_last, idx_now] + 1
                        self.hanzi_fre[idx_now] = self.hanzi_fre[idx_now] + 1

            # Normalize
            self.trans_mat /= np.sum(self.trans_mat, axis=1).transpose()
            self.hanzi_fre /= np.sum(self.hanzi_fre)

            # construct decode hash table
            for k, v in self.encode_hanzi.items():
                self.decode_hanzi.update({v: k})
            for k, v in self.encode_pinyin.items():
                self.decode_pinyin.update({v: k})

    def train(self, ma_biao, yu_liao):
        self.__read_pinyin(ma_biao)
        self.__read_trans(yu_liao)

    def save_model(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)
