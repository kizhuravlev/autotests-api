from concurrent import futures

import grpc

import grpc.course_service_pb2 as course_service_pb2
import grpc.course_service_pb2_grpc as course_service_pb2_grpc

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):

    def GetCourse(self, request, context):
        print(f'Получен запрос от пользователя к методу GetCourse: {request.course_id}')
        return course_service_pb2.GetCourseResponce(
            course_id = request.course_id,
            title = 'Автотесты API',
            description = 'Будем изучать написание API автотестов'
        )
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    server.add_insecure_port('[::]:50051')

    server.start()
    print("Сервер запущен")

    server.wait_for_termination()

if __name__ == "__main__":
    serve()