
import config
from listener.SendEmailAlertListener import SendEmailAlertListener
from repository.AsyncJobs import AsyncJobs
from repository.RulesRepository import RulesRepository
from repository.SensorsRepository import SensorsRepository
from repository.UsersRepository import UsersRepository
from rules.RuleChecker import RuleChecker
from rules.interpretter.InterpretterContext import InterpretterContext
from rules.parser.ExpressionBuilder import ExpressionBuilder
from rules.parser.Tokenizer import Tokenizer
from rules.parser.AverageSensorTokenConverter import AverageSensorTokenConverter
from rules.parser.BooleanTokenConverter import BooleanTokenConverter
from rules.parser.CurrentTimeTokenConverter import CurrentTimeTokenConverter
from rules.parser.IntTokenConverter import IntTokenConverter
from rules.parser.SensorTokenConverter import SensorTokenConverter
from services.EmailSender import EmailSender
from sync_events.ValidRuleEvent import ValidRuleEvent
from tasks.RulesEvaluator import RulesEvaluator
from tasks.StoreData import StoreData
from tasks.TaskRunner import TaskRunner
from lock.TimedLock import TimedLock
from lock.RuleTimedLock import RuleTimedLock


class Container():
    cached = {}

    @staticmethod
    def get(service_name):
        if service_name in Container.cached.keys():
            return Container.cached[service_name]

        Container.cached[service_name] = getattr(Container, service_name)()

        return Container.cached[service_name]

    @staticmethod
    def async_jobs():
        return AsyncJobs(config.rabbitmq_host)

    @staticmethod
    def send_email_alert_listener():
        return SendEmailAlertListener(Container.get('email_sender'), Container.get('rule_timed_lock'))

    @staticmethod
    def valid_rule_event():
        return ValidRuleEvent()

    @staticmethod
    def email_sender():
        return EmailSender(config.email['email'], config.email['password'], config.email['notifiedAddress'])

    @staticmethod
    def store_data():
        return StoreData(Container.get('sensors_repository'))

    @staticmethod
    def rules_evaluator():
        return RulesEvaluator(Container.get('rules_repository'), Container.get('sensors_repository'),
                              Container.get('users_repository'), Container.get('rule_checker'),
                              Container.get('valid_rule_event'))

    @staticmethod
    def task_runner():
        task_runner = TaskRunner()
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
        return SensorsRepository(config.mongodb_uri)

    @staticmethod
    def timed_lock():
        return TimedLock(config.redis['host'], config.redis['port'])

    @staticmethod
    def rule_timed_lock():
        return RuleTimedLock(Container.get('timed_lock'))

    @staticmethod
    def tokenizer():
        tokenizer = Tokenizer()
        tokenizer.add_token_converter(Container.get('average_sensor_token_converter'))
        tokenizer.add_token_converter(Container.get('sensor_token_converter'))
        tokenizer.add_token_converter(BooleanTokenConverter())
        tokenizer.add_token_converter(CurrentTimeTokenConverter())
        tokenizer.add_token_converter(IntTokenConverter())

        return tokenizer

    @staticmethod
    def average_sensor_token_converter():
        return AverageSensorTokenConverter(Container.get('sensors_repository'))

    @staticmethod
    def sensor_token_converter():
        return SensorTokenConverter(Container.get('sensors_repository'))

    @staticmethod
    def expression_builder():
        return ExpressionBuilder(Container.get('tokenizer'))

    @staticmethod
    def interpretter_context():
        return InterpretterContext()

