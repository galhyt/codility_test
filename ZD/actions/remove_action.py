from actions.action import Action
from statemachine import ZDState


class RemoveAction(Action):
    pending = ZDState("pending", initial=True)
    machine_remove = ZDState("machine_remove")
    cloud_remove = ZDState("cloud_remove")
    final = ZDState("final")

    start = pending.to(machine_remove)
    start_cloud = machine_remove.to(cloud_remove)
    finish = cloud_remove.to(final)

    def on_start_cloud(self):
        print("on_start_cloud")
        return False
