#!/usr/bin/env python3
import rclpy #ros2 파이썬 라이브러리
from rclpy.node import Node #프로세스 단위의 클래스
from rclpy.qos import QoSProfile #라디오 주파수 같은 개념
from ros_study_msgs.msg import MyMsg #인터페이스 주입

class my_msg_test(Node): #노드 상속

    def __init__(self):
        super().__init__('my_msg_test') #프로세스 노드의 이름
        qos_profile = QoSProfile(depth=10) #주파수가 10으로 맞춰졌다 생각한다
        self.publisher_ = self.create_publisher(MyMsg, 'baejunha_pizza', qos_profile)
        #토픽을 발행하는 퍼블리셔 생성 함수
        timer_period = 0.5 #seconds 토픽의 주기
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0.0
    
    def timer_callback(self): #토픽을 발행하면서 어쩔건데
        msg = MyMsg() #인터페이스 안에 float32 num
        msg.num = self.i #인터페이스 객체 안에 있는 num에다가 값을 넣음
        self.publisher_.publish(msg) #토픽 발행
        self.get_logger().info(str(self.i))
        #로그를 찍는 함수
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    my_msg_test_publisher = my_msg_test() #앞에 정의한 클래스 호출

    rclpy.spin(my_msg_test_publisher) #클래스 실행

    my_msg_test_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()