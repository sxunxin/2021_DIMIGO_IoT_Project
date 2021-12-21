import picamera
import time

path = '/home/pi/src4/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3)

    while True:
        cmd = input('photo: 1, video: 2, exit: 9 >')
        if cmd == '1':
            print('사진 촬영')
            now_str = time.strftime("%Y%m%d_%H%M%S")
            time.sleep(1)
            camera.rotation = 180
            camera.capture('%s/photo_%s.jpg' % (path, now_str))

        elif cmd == '2':
            print('동영상 촬영')
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.rotation = 180
            camera.start_recording('%s/video_%s.H264' % (path, now_str))
            input('press enter to stop recoding..')
            camera.stop_recording()

        elif cmd == '9':
            break
        else:
            print('incorrcet command')
finally:
    camera.stop_preview()