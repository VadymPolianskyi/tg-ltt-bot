import json

from telebot.types import CallbackQuery

from app.handler.activity.delete_activity import DeleteActivityBeforeVoteCallbackHandler, \
    DeleteActivityAfterVoteCallbackHandler
from app.handler.track.start_tracking import StartTrackingAfterVoteCallbackHandler
from app.handler.track.stop_tracking import StopTrackingAfterVoteCallbackHandler
from app.handler.track.track import TrackAfterVoteCallbackHandler


class CallbackRouter:
    def __init__(self,
                 delete_activity_before_vote_callback_handler: DeleteActivityBeforeVoteCallbackHandler,
                 delete_activity_after_vote_callback_handler: DeleteActivityAfterVoteCallbackHandler,
                 track_after_vote_callback_handler: TrackAfterVoteCallbackHandler,
                 start_tracking_after_vote_callback_handler: StartTrackingAfterVoteCallbackHandler,
                 stop_tracking_after_vote_callback_handler: StopTrackingAfterVoteCallbackHandler,
                 ):

        self.callback_handler: dict = {
            DeleteActivityBeforeVoteCallbackHandler.MARKER: delete_activity_before_vote_callback_handler,
            DeleteActivityAfterVoteCallbackHandler.MARKER: delete_activity_after_vote_callback_handler,
            TrackAfterVoteCallbackHandler.MARKER: track_after_vote_callback_handler,
            StartTrackingAfterVoteCallbackHandler.MARKER: start_tracking_after_vote_callback_handler,
            StopTrackingAfterVoteCallbackHandler.MARKER: stop_tracking_after_vote_callback_handler
        }

    def route(self, call: CallbackQuery):
        payload: dict = json.loads(call.data)

        for key in payload.keys():
            if key in self.callback_handler:
                print(f"Found rote for callback '{key}' from user({call.from_user.id})")
                self.callback_handler[key].handle(call)
                break