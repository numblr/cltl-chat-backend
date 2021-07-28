import logging
from dataclasses import dataclass

from cltl.chatbackend.reverse import ReverseChatProcessor
from cltl.combot.infra.config import ConfigurationManager
from cltl.combot.infra.di_container import DIContainer
from cltl.combot.infra.event import EventBus
from cltl.combot.infra.resource import ResourceManager
from .event.consumer import ProcessorWorker

logger = logging.getLogger(__name__)


@dataclass
class ApplicationContainer:
    event_bus: EventBus
    resource_manager: ResourceManager
    config_manager: ConfigurationManager


class Application:
    def __init__(self, application_container: ApplicationContainer):
        agent = application_container.config_manager.get_config("cltl.chat-backend").get("agent_id")
        processor = ReverseChatProcessor(agent)

        self.consumer = ProcessorWorker(processor,
                                        application_container.event_bus,
                                        application_container.resource_manager,
                                        application_container.config_manager)

    def run(self):
        logger.info("Starting application")
        self.consumer.start()
