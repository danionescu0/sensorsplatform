import json
from datetime import datetime
from dateutil import tz

from security.secure import secure
from web.CorsHandler import CorsHandler
from repository.AlertRepository import AlertRepository
from repository.RulesRepository import RulesRepository
from repository.UsersRepository import UsersRepository

class AlertsHandler(CorsHandler):
    def initialize(self, alerts_repo: AlertRepository, rules_repo: RulesRepository, users_repo: UsersRepository):
        self.__alerts_repository = alerts_repo
        self.__rules_repository = rules_repo
        self.__users_repository = users_repo

    @secure
    def get(self, user_id):
        user = self.__users_repository.get_by_id(user_id)
        if not user:
            self.set_status(404)
            return
        alerts = self.__alerts_repository.get_for_user(user.userid)
        alerts_presentation_data = []
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('Europe/Bucharest')
        for alert in alerts:
            rule_data = self.__rules_repository.get(alert.rule_id)
            initial_date = datetime.fromtimestamp(int(alert.timestamp)).replace(tzinfo=from_zone)
            local_date = initial_date.astimezone(to_zone)
            alerts_presentation_data.append(
                {'date' : local_date.strftime('%Y-%m-%d %H:%M:%S'),
                 'rule_text': rule_data.rule_text, 'name' : rule_data.name}
            )
        self.write(json.dumps(alerts_presentation_data))