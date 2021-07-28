from cltl.chatui.api import Utterance


class ReverseChatProcessor:
    def __init__(self, agent: str):
        self._agent = agent

    def process(self, utterance: Utterance):
        return Utterance(utterance.chat_id, self._agent, utterance.text[::-1])