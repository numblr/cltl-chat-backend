import abc

from cltl.chatui.api import Utterance


class ChatProcessor(abc.ABC):
    def process(self, utterance: Utterance):
        NotImplementedError("")