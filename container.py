import config
from repository.AsyncJobs import AsyncJobs
from tasks.SendEmailAlert import SendEmailAlert
from tasks.StoreData import StoreData
from tasks.TaskRunner import TaskRunner
from repository.RulesRepository import RulesRepository
from repository.SensorsRepository import SensorsRepository
from rules.parser.ExpressionBuilder import ExpressionBuilder
from rules.parser.Tokenizer import Tokenizer
from rules.interpretter.InterpretterContext import InterpretterContext

class Container():

    @staticmethod
    def get(service_name):
        return getattr(Container, service_name)()

    @staticmethod
    def async_jobs():
        return AsyncJobs(config.rabbitmq_host)

    @staticmethod
    def send_email_alert():
        return SendEmailAlert(config.email['email'], config.email['password'], config.email['notifiedAddress'])

    @staticmethod
    def store_data():
        return StoreData()

    @staticmethod
    def task_runner():
        task_runner = TaskRunner()
        task_runner.add_task(Container.get('send_email_alert'))
        task_runner.add_task(Container.get('store_data'))

        return task_runner

    @staticmethod
    def rules_repository():
        return RulesRepository(config.mongodb_uri)

    @staticmethod
    def sensors_repository():
        return SensorsRepository()

    @staticmethod
    def tokenizer():
        return Tokenizer(Container.get('sensors_repository'))

    @staticmethod
    def expression_builder():
        return ExpressionBuilder(Container.get('tokenizer'))

    @staticmethod
    def interpretter_context():
        return InterpretterContext()

