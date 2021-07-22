import abc

from cltl.chatui.api import Utterance


class ReverseChatProcessor(abc.ABC):
    def process(self, utterance: Utterance):
        return Utterance(utterance.chat_id, utterance.speaker, utterance.text[::-1])