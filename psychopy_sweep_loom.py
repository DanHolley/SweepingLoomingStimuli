from psychopy import visual, core  # import some libraries from PsychoPy
import numpy as np 


class LoomingSweepingStimulus():
    def __init__(self, **kwargs):
        self.win = visual.Window([800,600], monitor="testMonitor", units="deg")
        self.win.update()
        #self.loom_threat()
        #self.sweep_threat()

    #create some stimuli
    def create_threat(self, size, color="white"):
        return visual.Circle(self.win, units="norm", radius=size, fillColor='white', autoDraw=True )

    def sweep_threat( self, time_across=0.3, num_steps=100.0):
        threat = self.create_threat( size=.1 )
        x_min = -1
        x_max = 1

        core.wait(1.0)
        clock = core.Clock()
        while clock.getTime() < time_across:  # clock times are in seconds
            x_pos = x_min + (x_max-x_min) * (1-(time_across-clock.getTime())/time_across )
            #print( (time_across-clock.getTime())/time_across, x_pos) 
            threat.pos = [x_pos, .5]
            #threat.draw()
            self.win.flip()

    def loom_threat( self, time_across=0.5, num_steps=100.0):
        z_min = 0
        z_max = 1
        threat = self.create_threat( size=z_min )

        core.wait(1.0)
        clock = core.Clock()
        while clock.getTime() < time_across:  # clock times are in seconds
            z_pos = z_min + (z_max-z_min) * (1-(time_across-clock.getTime())/time_across )
            # print z_pos, 1-(time_across-clock.getTime())/time_across 
            threat.radius = z_pos
            #threat.draw()
            self.win.flip()


app=LoomingSweepingStimulus()

for i in range(1,4):
    app.sweep_threat( time_across=i )
#app.loom_threat()


