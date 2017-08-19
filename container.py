import config
from repository.AsyncJobs import AsyncJobs
from tasks.SendEmailAlert import SendEmailAlert
from tasks.StoreData import StoreData
from tasks.TaskRunner import TaskRunner
from tasks.RulesEvaluator import RulesEvaluator
from repository.RulesRepository import RulesRepository
from repository.SensorsRepository import SensorsRepository
from repository.UsersRepository import UsersRepository
from rules.parser.ExpressionBuilder import ExpressionBuilder
from rules.parser.Tokenizer import Tokenizer
from rules.interpretter.InterpretterContext import InterpretterContext
from rules.RuleChecker import RuleChecker


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
        return StoreData(Container.get('sensors_repository'))

    @staticmethod
    def rules_evaluator():
        return RulesEvaluator(Container.get('rules_repository'), Container.get('sensors_repository'),
                              Container.get('users_repository'), Container.get('rule_checker'))

    @staticmethod
    def task_runner():
        task_runner = TaskRunner()
        task_runner.add_task(Container.get('send_email_alert'))
        task_runner.add_task(Container.get('store_data'))
        task_runner.add_task(Container.get('rules_evaluator'))

        return task_runner

    @staticmethod
    def rules_repository():
        return RulesRepository(config.mongodb_uri)

    @staticmethod
    def rule_checker():
        return RuleChecker(Container.get('expression_builder'), Container.get('interpretter_context'))

    @staticmethod
    def users_repository():
        return UsersRepository(config.mongodb_uri)

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
