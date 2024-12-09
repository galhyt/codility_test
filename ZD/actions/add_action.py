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

    def on_start(self):
        print("on_start")
        return False
