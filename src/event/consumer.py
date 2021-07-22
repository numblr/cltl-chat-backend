import logging

from cltl.chatbackend.api import ChatProcessor
from cltl.combot.infra.config import ConfigurationManager
from cltl.combot.infra.event.api import Event, EventBus
from cltl.combot.infra.resource import ResourceManager
from cltl.combot.infra.topic_worker import TopicWorker

logger = logging.getLogger(__name__)


class ProcessorWorker(TopicWorker):
    def __init__(self, processor: ChatProcessor, event_bus: EventBus, resource_manager: ResourceManager, config_manager: ConfigurationManager,
                 name: str = None) -> None:
        self._processor = processor
        event_config = config_manager.get_config("cltl.chat-ui.events")
        utterance_topic = event_config.get("topic_utterance")
        self._response_topic = event_config.get("topic_response")

        super().__init__([utterance_topic], event_bus, interval=0, name=name, resource_manager=resource_manager,
                         requires=[], provides=[])

    def process(self, event: Event) -> None:
        response = self._processor.process(event.payload)
        self.event_bus.publish(self._response_topic, Event.for_payload(response))
