import time, math
import pyjoycon as pjc

device_ids = pjc.get_device_ids()
print(pjc.device.get_device_ids())

#create a controller object
class controller:
    def __init__(self, controller_mode="single", side="right") -> None:
        self.controller_mode = controller_mode
        self.stick_range = {"left": {"vertical": (-1,1), "horizontal": (-1, 1)}, "right": {"vertical": (-1,1), "horizontal": (-1, 1)}}
        if self.controller_mode == "single":
            self.r = pjc.wrappers.PythonicJoyCon(*pjc.get_R_id())
            self.l = pjc.wrappers.PythonicJoyCon(*pjc.get_L_id())
            self.stick_centered = [0,0]
        elif self.controller_mode == "dual":
            if side == "right":
                self.device = pjc.wrappers.PythonicJoyCon(*pjc.get_R_id())
                self.side = "right"
            elif side == "left":
                self.device = pjc.wrappers.PythonicJoyCon(*pjc.get_L_id())
                self.side = "left"
    def get_stick_position(self, side="right") -> tuple:
        if self.controller_mode == 'single':
            if side == "right":
                return self.r.get_stick_right_horizontal(), self.r.get_stick_right_vertical()
            elif side == "left":
                return self.l.get_stick_left_horizontal(), self.l.get_stick_left_vertical()
        elif self.controller_mode == 'dual':
            if self.side == "right":
                return self.device.get_stick_right_horizontal(), self.device.get_stick_right_vertical()
            elif self.side == "left":
                return self.device.get_stick_left_horizontal(), self.device.get_stick_left_vertical()
    def set_centers(self):
        if self.controller_mode == "single":
            self.stick_center_range = [(self.l.get_stick_left_horizontal(), self.l.get_stick_left_vertical()), (self.r.get_stick_right_horizontal(), self.r.get_stick_right_vertical())]
        elif self.controller_mode == "dual":
            if self.side == "right":
                slef.stick_center_range = [(self.device.get_stick_left_horizontal(), self.device.get_stick_left_vertical()), (self.device.get_stick_right_horizontal(), self.device.get_stick ]
    def set_stick_range(self, stick="right", value=0):
        if self.controller_mode == "single":
            if value > max(self.stick_range[stick]):
                self.stick_range[stick][1] = value
            elif value < min(self.stick_range[stick]):
                self.stick_range[stick][0] = value
        elif self.controller_mode == "dual":
            if value > max(self.stick_range[self.side]):
                self.stick_range[self.side][1] = value
            elif value < min(self.stick_range[self.side]):
                self.stick_range[self.side][0] = value


    def get_status(self) -> str:
        if self.controller_mode == "single":
            return self.r.get_status(), self.l.get_status()
        elif self.mode == "dual":
            return self.device.get_status()
        

joycon = controller()

calibrating = 1

print("Time to calibrate the joycons, please center the sticks and press the enter key to begin the calibration sequence.")
input()
joycon.set_centers()
print("We will begin with the right stick calibration.")
print("")
while calibrating == 1:
