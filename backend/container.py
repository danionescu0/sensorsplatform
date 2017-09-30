from typing import Callable
import sys
from logging import RootLogger

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

def singleton(function: Callable):
    caching = {}
    def wrapper(*args, **kwargs):
        if function.__name__ in caching:
            return caching[function.__name__]
        caching[function.__name__] = function(*args, **kwargs)

        return caching[function.__name__]

    return wrapper

class Container():
    def async_jobs(self) -> AsyncJobs:
        return AsyncJobs(config.rabbitmq_host)

    @singleton
    def send_email_alert_listener(self) -> SendEmailAlertListener:
        return SendEmailAlertListener(self.email_sender(), self.rule_timed_lock(),
                                      self.logging())

    @singleton
    def valid_rule_event(self) -> ValidRuleEvent:
        return ValidRuleEvent()

    @singleton
    def email_sender(self) -> EmailSender:
        return EmailSender(config.email['email'], config.email['password'], config.email['notifiedAddress'])

    @singleton
    def store_momentary_data(self) -> StoreMomentaryData:
        return StoreMomentaryData(self.sensors_repository(), self.async_jobs(), self.logging())

    @singleton
    def store_durable_data(self) -> StoreDurableData:
        return StoreDurableData(self.sensors_repository(), self.logging())

    @singleton
    def rules_evaluator(self) -> RulesEvaluator:
        return RulesEvaluator(self.rules_repository(), self.sensors_repository(),
                              self.users_repository(), self.rule_checker(),
                              self.valid_rule_event(), self.logging())

    @singleton
    def task_runner(self) -> TaskRunner:
        task_runner = TaskRunner()
        task_runner.add_task(self.store_momentary_data())
        task_runner.add_task(self.store_durable_data())
        task_runner.add_task(self.rules_evaluator())

        return task_runner

    @singleton
    def rules_repository(self) -> RulesRepository:
        return RulesRepository(config.mongodb_uri)

    @singleton
    def rule_checker(self) -> RuleChecker:
        return RuleChecker(self.expression_builder(), self.interpretter_context())

    @singleton
    def users_repository(self) -> UsersRepository:
        return UsersRepository(config.mongodb_uri)

    @singleton
    def sensors_repository(self) -> SensorsRepository:
        return SensorsRepository(config.mongodb_uri)

    @singleton
    def alerts_repository(self) -> AlertRepository:
        return AlertRepository(config.mongodb_uri)

    @singleton
    def timed_lock(self) -> TimedLock:
        return TimedLock(config.redis['host'], config.redis['port'])

    @singleton
    def rule_timed_lock(self) -> RuleTimedLock:
        return RuleTimedLock(self.timed_lock())

    @singleton
    def tokenizer(self) -> Tokenizer:
        tokenizer = Tokenizer(self.logging())
        tokenizer.add_token_converter(self.average_sensor_token_converter())
        tokenizer.add_token_converter(self.sensor_token_converter())
        tokenizer.add_token_converter(self.gis_distance_token_converter())
        tokenizer.add_token_converter(self.speed_token_converter())
        tokenizer.add_token_converter(BooleanTokenConverter())
        tokenizer.add_token_converter(CurrentTimeTokenConverter())
        tokenizer.add_token_converter(IntTokenConverter())

        return tokenizer

    @singleton
    def average_sensor_token_converter(self) -> AverageSensorTokenConverter:
        return AverageSensorTokenConverter(self.sensors_repository())

    @singleton
    def sensor_token_converter(self) -> SensorTokenConverter:
        return SensorTokenConverter(self.sensors_repository())

    @singleton
    def gis_distance_token_converter(self) -> GisDistanceTokenConverter:
        return GisDistanceTokenConverter(self.sensors_repository())

    @singleton
    def speed_token_converter(self) -> SpeedTokenConverter:
        return SpeedTokenConverter(self.sensors_repository())

    @singleton
    def expression_builder(self) -> ExpressionBuilder:
        return ExpressionBuilder(self.tokenizer())

    @singleton
    def interpretter_context(self) -> InterpretterContext:
        return InterpretterContext()

    @singleton
    def logging(self) -> RootLogger:
        logging_config = LoggingConfig(config.logging['log_file'], config.logging['log_entries'])
        sys.excepthook = logging_config.set_error_hadler

        return logging_config.get_logger()

    @singleton
    def jwt_token_factory(self) -> JwtTokenFactory:
        return JwtTokenFactory(config.web['jwt_secret'])