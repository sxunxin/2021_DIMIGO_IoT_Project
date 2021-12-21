#include <wiringPi.h>
#define LED_PIN 4

int main (void)
{
  //wiringPiSetup () ;
  wiringPiSetupGpio();
  pinMode (LED_PIN, OUTPUT) ;
  for (int i = 0; i< 3; i++)
  {
    digitalWrite (LED_PIN, HIGH) ; delay (3000) ;
    digitalWrite (LED_PIN,  LOW) ; delay (1000) ;
  }

  pinMode (LED_PIN, INPUT) ;

  return 0 ;
}