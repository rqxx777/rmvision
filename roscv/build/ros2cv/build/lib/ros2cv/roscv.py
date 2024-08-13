import rclpy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from rclpy.node import Node
class Image__review:
    def __init__(self):
        self.publisher1=rclpy.Publisher("cv_bridge_image",Image,queue_size=1)
        self.brideg=CvBridge
        self.subscriber1=rclpy.subscriber("/usb_cam/image_raw",Image,self.callback)
    def callback(self,img):
        
        cv_image=self.brideg.imgmsg_to_cv2(img,"bgr8")# ros img turn to opencv img
        cv2.rectangle(cv_image,(1,1),(20,25),(0,255,0),3)# paint a square
        self.publisher1.publish(self.brideg.cv2_to_imgmsg(cv_image,"bgr8"))# img turn to ros img and publish

def main(args=None):#enter def
    rclpy.init(args=args)
    roscv_node=Node("roscv")
    #roscv_node.get_logger().info("bugcheck")
    rclpy.spin(roscv_node)
    rclpy.shutdown(
    )


        