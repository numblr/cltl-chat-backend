import logging.config

from cltl.chatbackend.api import ChatProcessor
from cltl.chatbackend.reverse import ReverseChatProcessor
from cltl.combot.infra.event.kombu import KombuEventBusContainer
from cltl.combot.infra.event.memory import SynchronousEventBusContainer
from cltl.combot.infra.topic_worker import TopicWorker

logging.config.fileConfig('config/logging.config')

from cltl.combot.infra.config.k8config import K8LocalConfigurationContainer
from cltl.combot.infra.di_container import singleton
from cltl.combot.infra.resource.threaded import ThreadedResourceContainer
from event.consumer import ProcessorWorker

logger = logging.getLogger(__name__)

K8LocalConfigurationContainer.load_configuration()
run_local = K8LocalConfigurationContainer.get_config("cltl.chat-ui.events", "local")


if run_local.lower() == 'true':
    class ApplicationContainer(SynchronousEventBusContainer, ThreadedResourceContainer, K8LocalConfigurationContainer):
        logger.info("Initialized ApplicationContainer with local event bus")
else:
    class ApplicationContainer(KombuEventBusContainer, ThreadedResourceContainer, K8LocalConfigurationContainer):
        logger.info("Initialized ApplicationContainer with kombu event bus")


class Application(ApplicationContainer):
    @property
    @singleton
    def processor(self) -> ChatProcessor:
        return ReverseChatProcessor()

    @property
    @singleton
    def consumer(self) -> TopicWorker:
        return ProcessorWorker(self.processor, self.event_bus, self.resource_manager, self.config_manager)

    def run(self):
        self.consumer.start()


if __name__ == '__main__':
    Application().run()
