
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|---	|
|   REST add	|   3.4535	|   3.4411	|  320.6313	|
|   gRPC add	|   0.7100	|   0.8075	|    158.5558	|
|   REST rawimg	|   6.6109	|   7.8908	|   1285.2831	|
|   gRPC rawimg	|    8.7613   |  12.2129 	|   197.3481	|
|   REST dotproduct	|   3.9904	|   4.3368	| 322.8870 	|
|   gRPC dotproduct	|   0.7826	|   1.0003	|   164.6878 	|
|   REST jsonimg	|   38.9321	|   44.8885	|   1445.9906	|
|   gRPC jsonimg	|   24.1778    |  25.5948 	|   218.0394	|
|   PING        |   0.054    |   0.318   |   151.908    |

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.

For small messages (add and dotproduct), gRPC is 5x faster than REST locally (0.71ms vs 3.45ms). This is due to REST's connection overhead as it needs to open a new TCP connection per query, while gRPC resuses a single connection. The cross-region test (151.9ms ping) highlights this even more as add took 320ms with REST call while it only took 158ms with gRPC. This means that gRPC eliminates the overhead that comes with REST calls. Overall, gRPC is consistently faster than REST and the advantage is even greater when as the network latency grows.