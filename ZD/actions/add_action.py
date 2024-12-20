from actions.action import Action
from statemachine import ZDState


class AddAction(Action):
    pending = ZDState("pending", initial=True)
    cloud_running = ZDState("cloud_running")
    machine_running = ZDState("machine_running")
    final = ZDState("final")

    start = pending.to(cloud_running)
    start_machine = cloud_running.to(machine_running)
    finish = machine_running.to(final)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_signal = False

    def on_start(self):
        print("on_start")
        return self.start_signal
