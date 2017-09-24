import sys

import config
from listener.SendEmailAlertListener import SendEmailAlertListener
from lock.RuleTimedLock import RuleTimedLock
from lock.TimedLock import TimedLock
from repository.RulesRepository import RulesRepository
from repository.SensorsRepository import SensorsRepository
from repository.UsersRepository import UsersRepository
from repository.AlertRepository import AlertRepository
from rules.RuleChecker import RuleChecker
from rules.interpretter.InterpretterContext import InterpretterContext
from rules.parser.AverageSensorTokenConverter import AverageSensorTokenConverter
from rules.parser.BooleanTokenConverter import BooleanTokenConverter
from rules.parser.CurrentTimeTokenConverter import CurrentTimeTokenConverter
from rules.parser.ExpressionBuilder import ExpressionBuilder
from rules.parser.IntTokenConverter import IntTokenConverter
from rules.parser.SensorTokenConverter import SensorTokenConverter
from rules.parser.GisDistanceTokenConverter import GisDistanceTokenConverter
from rules.parser.SpeedTokenConverter import SpeedTokenConverter
from rules.parser.Tokenizer import Tokenizer
from security.JwtTokenFactory import JwtTokenFactory
from services.AsyncJobs import AsyncJobs
from services.EmailSender import EmailSender
from services.LoggingConfig import LoggingConfig
from sync_events.ValidRuleEvent import ValidRuleEvent
from tasks.RulesEvaluator import RulesEvaluator
from tasks.StoreMomentaryData import StoreMomentaryData
from tasks.StoreDurableData import StoreDurableData
from tasks.TaskRunner import TaskRunner


class Container():
    cached = {}
    uncacheable = ['async_jobs']

    @staticmethod
    def get(service_name):
        if service_name in Container.uncacheable:
            return getattr(Container, service_name)()
        if service_name in Container.cached.keys():
            return Container.cached[service_name]
        Container.cached[service_name] = getattr(Container, service_name)()

        return Container.cached[service_name]

    @staticmethod
    def async_jobs():
        return AsyncJobs(config.rabbitmq_host)

    @staticmethod
    def send_email_alert_listener():
        return SendEmailAlertListener(Container.get('email_sender'), Container.get('rule_timed_lock'),
                                      Container.get('logging'))

    @staticmethod
    def valid_rule_event():
        return ValidRuleEvent()

    @staticmethod
    def email_sender():
        return EmailSender(config.email['email'], config.email['password'], config.email['notifiedAddress'])

    @staticmethod
    def store_momentary_data():
        return StoreMomentaryData(Container.get('sensors_repository'), Container.get('async_jobs'), Container.get('logging'))

    @staticmethod
    def store_durable_data():
        return StoreDurableData(Container.get('sensors_repository'), Container.get('logging'))

    @staticmethod
    def rules_evaluator():
        return RulesEvaluator(Container.get('rules_repository'), Container.get('sensors_repository'),
                              Container.get('users_repository'), Container.get('rule_checker'),
                              Container.get('valid_rule_event'), Container.get('logging'))

    @staticmethod
    def task_runner():
        task_runner = TaskRunner()
        task_runner.add_task(Container.get('store_momentary_data'))
        task_runner.add_task(Container.get('store_durable_data'))
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
    def alerts_repository():
        return AlertRepository(config.mongodb_uri)

    @staticmethod
    def timed_lock():
        return TimedLock(config.redis['host'], config.redis['port'])

    @staticmethod
    def rule_timed_lock():
        return RuleTimedLock(Container.get('timed_lock'))

    @staticmethod
    def tokenizer():
        tokenizer = Tokenizer(Container.get('logging'))
        tokenizer.add_token_converter(Container.get('average_sensor_token_converter'))
        tokenizer.add_token_converter(Container.get('sensor_token_converter'))
        tokenizer.add_token_converter(Container.get('gis_distance_token_converter'))
        tokenizer.add_token_converter(Container.get('speed_token_converter'))
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
    def gis_distance_token_converter():
        return GisDistanceTokenConverter(Container.get('sensors_repository'))

    @staticmethod
    def speed_token_converter():
        return SpeedTokenConverter(Container.get('sensors_repository'))

    @staticmethod
    def expression_builder():
        return ExpressionBuilder(Container.get('tokenizer'))

    @staticmethod
    def interpretter_context():
        return InterpretterContext()

    @staticmethod
    def logging():
        logging_config = LoggingConfig(config.logging['log_file'], config.logging['log_entries'])
        sys.excepthook = logging_config.set_error_hadler

        return logging_config.get_logger()

    @staticmethod
    def jwt_token_factory():
        return JwtTokenFactory(config.web['jwt_secret'])