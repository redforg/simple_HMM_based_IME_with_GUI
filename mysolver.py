# encoding=utf-8
import pickle
from os import path
from viterbis import viterbi_algo


class MySolver(object):
    def __init__(self, filename=r"./HMM_IME.pkl"):
        self.loaded = False
        if path.exists(filename):
            self.loaded = True
            with open(filename, "rb") as f:
                x = pickle.load(f)
            self.params = x

    def solve(self, input_str):
        if not self.loaded:
            return []
        obs = input_str.split(" ")
        tmp_ob = []
        for i in obs:
            if self.params.encode_pinyin.get(i) is None:
                break
            else:
                tmp_ob.append(i)
        obs = tmp_ob
        ans = []

        if len(obs) > 1:
            tmp_candidate = self.__solve(obs)
            if tmp_candidate is not None:
                ans = ans + tmp_candidate
            for i in obs:
                print(i)
                tmp_candidate = self.__solve([i])
                if tmp_candidate is not None:
                    ans = ans + tmp_candidate
        elif len(obs) == 1:
            tmp_candidate = self.__solve(obs)
            if tmp_candidate is not None:
                ans = ans + tmp_candidate

        return ans

    def __solve(self, obs):

        x = viterbi_algo(self.params, observations=obs)
        return x
