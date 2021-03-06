from core.services import BaseService


class UpdateGoalService(BaseService):
    def __init__(self, instance, text):
        self.instance = instance
        self.text = text

    def perform(self):
        self._save_goal()

    def _save_goal(self):
        self.instance.text = self.text

        self.instance.save()
