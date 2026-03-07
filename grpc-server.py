import grpc
from concurrent import futures
import lab6_pb2
import lab6_pb2_grpc
from PIL import Image
import io
import base64

class Lab6Servicer(lab6_pb2_grpc.Lab6Servicer):
    def Add(self, request, context):
        return lab6_pb2.addReply(sum=request.a + request.b)

    def RawImage(self, request, context):
        img = Image.open(io.BytesIO(request.img))
        return lab6_pb2.imageReply(width=img.size[0], height=img.size[1])

    def DotProduct(self, request, context):
        result = sum(x * y for x, y in zip(request.a, request.b))
        return lab6_pb2.dotProductReply(dotproduct=result)

    def JsonImage(self, request, context):
        img_bytes = base64.b64decode(request.img)
        img = Image.open(io.BytesIO(img_bytes))
        return lab6_pb2.imageReply(width=img.size[0], height=img.size[1])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lab6_pb2_grpc.add_Lab6Servicer_to_server(Lab6Servicer(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server started on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()