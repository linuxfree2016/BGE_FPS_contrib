import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

#if bge.logic.keyboard.events[bge.events.WKEY] == bge.logic.KX_INPUT_ACTIVE:
#    own['timer'] += 1
#if bge.logic.keyboard.events[bge.events.WKEY] != bge.logic.KX_INPUT_ACTIVE:  
#    own['timer'] = 0
          
#properties
equiped = own['equiped']
target = own['target']
timer = own['timer']
change = own['change']


#animations
M24up = cont.actuators['M24up']
M24down = cont.actuators['M24down']
Glockup = cont.actuators['Glockup']
Glockdown = cont.actuators['Glockdown']
Knifeup = cont.actuators['Knifeup']
Knifedown = cont.actuators['Knifedown']

self = scene.objects[own.name]



# change property
if equiped != target: # and change == False: in logibricks defined
    self['change'] = True
elif equiped == target:
    self['change'] = False
    
#if ((bge.logic.keyboard.events[bge.events.WKEY] or bge.logic.keyboard.events[bge.events.SKEY] or bge.logic.keyboard.events[bge.events.AKEY] or bge.logic.keyboard.events[bge.events.DKEY]) != (bge.logic.KX_INPUT_ACTIVE)):
#    if change == True and timer < 40:
#        own['timer'] += 1
if change == True and timer < 40:
        own['timer'] += 1
    
# down animations
#if ((bge.logic.keyboard.events[bge.events.WKEY] or bge.logic.keyboard.events[bge.events.SKEY] or bge.logic.keyboard.events[bge.events.AKEY] or bge.logic.keyboard.events[bge.events.DKEY]) != (bge.logic.KX_INPUT_ACTIVE)):
#    if equiped == 1 and change == True and timer == 0:
#        cont.activate(M24down)
#    if equiped == 2 and change == True and timer == 0:
#        cont.activate(Glockdown)
#    if equiped == 3 and change == True and timer == 0:
#        cont.activate(Knifedown)    
if equiped == 1 and change == True and timer == 0:
    cont.activate(M24down)
if equiped == 2 and change == True and timer == 0:
    cont.activate(Glockdown)
if equiped == 3 and change == True and timer == 0:
    cont.activate(Knifedown)    
    
    
# end old weapon, deactivated animations DOWN
if equiped == 1 and change == True and timer == 20:
    own.sendMessage('M24 end', "", "M24")
    cont.deactivate(M24down)
if equiped == 2 and change == True and timer == 20:
    own.sendMessage('End_Glock', "", "glock")
    cont.deactivate(Glockdown)    
if equiped == 3 and change == True and timer == 20:
    own.sendMessage('Knife end', "", "knife")
    cont.deactivate(Knifedown)

# spawn a new weapon
#if ((bge.logic.keyboard.events[bge.events.WKEY] or bge.logic.keyboard.events[bge.events.SKEY] or bge.logic.keyboard.events[bge.events.AKEY] or bge.logic.keyboard.events[bge.events.DKEY]) != (bge.logic.KX_INPUT_ACTIVE)):
#    if target == 1 and change == True and timer == 20:
#        scene.addObject("M24", own, 0)
    
#    if target == 2 and change == True and timer == 20:
#        scene.addObject("glock", own, 0)
    
#    if target == 3 and change == True and timer == 20:
#        scene.addObject("knife", own, 0)
   
    
#    if target == 1 and change == True and timer > 20 and timer < 40:
    
#        cont.activate(M24up)
#    if target == 2 and change == True and timer > 20 and timer < 40:
    
#        cont.activate(Glockup)
#    if target == 3 and change == True and timer > 20 and timer < 40:
    
#        cont.activate(Knifeup)
if target == 1 and change == True and timer == 20:
    scene.addObject("M24", own, 0)
    
if target == 2 and change == True and timer == 20:
    scene.addObject("glock", own, 0)
    
if target == 3 and change == True and timer == 20:
    scene.addObject("knife", own, 0)
   
    
if target == 1 and change == True and timer > 20 and timer < 40:
    
    cont.activate(M24up)
if target == 2 and change == True and timer > 20 and timer < 40:
    
    cont.activate(Glockup)
if target == 3 and change == True and timer > 20 and timer < 40:
    
    cont.activate(Knifeup) 

# reset properties and deactivated animations UP
if timer == 40 and change == True: 
    cont.deactivate(M24up)   
    cont.deactivate(Glockup)
    cont.deactivate(Knifeup)
    own['timer'] -= 41
    own['equiped'] = own['target']

if timer > 40: # pulo do gato ;)
    change = False    
    
