import spidev
import time

# spi 인스턴스 생성
spi = spidev.SpiDev()

# spi 통신 시작
spi.open(0, 0) # bus : 0, dev : 0

# spi 통신 속도 설정
spi.max_speed_hz = 100000

# 채널에서 spi 데이터 읽기 (0 ~ 1023)
def analing_read(channel):
    # [byte_1, byte_2, byte_3]
    ret = spi.xfer2([1, (8 + channel) << 4, 0])
    print(ret)
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        reading = analing_read(0) # reading(0~1023)
        print("Reading=%d" % reading)
        time.sleep(0.5)
finally:
    spi.close()