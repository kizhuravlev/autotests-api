import grpc

import grpc.course_service_pb2 as course_service_pb2
import grpc.course_service_pb2_grpc as course_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

responce = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id='api-course'))
print(responce.course_id)
print(responce.title)
print(responce.description)