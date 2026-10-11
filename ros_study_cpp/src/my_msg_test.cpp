#include "rclcpp/rclcpp.hpp"
#include "ros_study_msgs/msg/my_msg.hpp"

class MyMsgPublisher : public rclcpp::Node
{

private:
    rclcpp::Publisher<ros_study_msgs::msg::MyMsg>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    float count_;

    void timer_callback()
    {
        auto message = ros_study_msgs::msg::MyMsg();
        message.num = count_;
        publisher_->publish(message);
        RCLCPP_INFO(this->get_logger(), "Publishing: %f", count_);
        count_ += 1.0;
    }

public:
    MyMsgPublisher()
    : Node("my_msg_test"),count_(0.0)
    {
        publisher_ = this->create_publisher<ros_study_msgs::msg::MyMsg>("hi_baejunha_pizza",10);
        timer_ = this->create_wall_timer(
            std::chrono::milliseconds(1),
            std::bind(&MyMsgPublisher::timer_callback, this));
    }
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MyMsgPublisher>());
    rclcpp::shutdown();
    return 0;
}