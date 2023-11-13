import sys
 
# setting path
sys.path.append('..')

from motor_control import *

dc_motor_init()
servo_motor_init()

logging.info('Start dc motor test')
dc_motor_start(50)
logging.info('dc motor start')
time.sleep(3)
dc_motor_stop()
logging.info('dc motor stop')
time.sleep(3)

logging.info('Start servo motor test')
servo_motor_set_left()
logging.info('servo motor set left')
time.sleep(3)
servo_motor_set_middle()
logging.info('servo motor set middle')
time.sleep(3)
servo_motor_set_right()
logging.info('servo motor set right')
time.sleep(3)
servo_motor_stop()
logging.info('servo motor stop')