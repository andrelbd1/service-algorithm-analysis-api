import logging
from src.evaluation.base import BaseEvaluation

log = logging.getLogger(__file__)


class RunningTime(BaseCode):
    name = 'Running Time'

    def process(self, params: dict):
        result = {'value': None,
                  'unit': None,
                  'message': None,
                  }
        # TODO: Implement the process function
        return result
