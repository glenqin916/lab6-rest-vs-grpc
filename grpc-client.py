import grpc
import sys
import time
import random
import base64
import lab6_pb2
import lab6_pb2_grpc

def run():
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <server ip> <cmd> <reps>")
        return

    host = sys.argv[1]
    cmd = sys.argv[2]
    reps = int(sys.argv[3])

    channel = grpc.insecure_channel(f'{host}:50051')
    stub = lab6_pb2_grpc.Lab6Stub(channel)

    start = time.perf_counter()

    for _ in range(reps):
        if cmd == 'add':
            stub.Add(lab6_pb2.addMsg(a=5, b=10))
        elif cmd == 'rawImage':
            img_data = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
            stub.RawImage(lab6_pb2.rawImageMsg(img=img_data))
        elif cmd == 'dotProduct':
            a = [random.random() for _ in range(100)]
            b = [random.random() for _ in range(100)]
            stub.DotProduct(lab6_pb2.dotProductMsg(a=a, b=b))
        elif cmd == 'jsonImage':
            img_data = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
            img_b64 = base64.b64encode(img_data).decode('utf-8')
            stub.JsonImage(lab6_pb2.jsonImageMsg(img=img_b64))
        else:
            print("Unknown command")
            return

    delta = ((time.perf_counter() - start) / reps) * 1000
    print(f"gRPC {cmd} took {delta:.4f} ms per operation")

if __name__ == '__main__':
    run()