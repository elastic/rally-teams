This directory contains example configurations for x-pack:

* `security`: Configures TLS for all HTTP and transport communication using self-signed certificates.
* `monitoring-local`: Enables x-pack monitoring with export to the current cluster.

The configurations have been implemented so that you can either only one of them or both together, i.e. all of the following combinations will work:

* `--elasticsearch-plugins="x-pack:security"`
* `--elasticsearch-plugins="x-pack:monitoring-local"`
* `--elasticsearch-plugins="x-pack:security+monitoring-local"`

The `security` configuration will enable basic authentication and TLS for the HTTP and the transport layer. It will also add a `rally` super-user with the password `rally-password`. As a consequence, you will need to add the following client options when benchmarking this configuration:

```
--client-options="use_ssl:true,verify_certs:false,basic_auth_user:'rally',basic_auth_password:'rally-password'"
```

If you are benchmarking a single node cluster, you'll also need to add `--cluster-health=yellow ` as precondition checks in Rally mandate that the cluster health has to be "green" by default but the x-pack related indices are created with a higher replica count. 

**Security Note**

The focus here is on providing a usable configuration for benchmarks. This configuration is **NOT** suitable for production use because:

* All clusters configured by Rally will use the same (self-signed) root certificate that will basically never expire
* Rally will add a "rally" user with super-user privileges with a hard-coded password.

Both of these measures mean that the cluster is not any more secure than without using x-pack. But once again: The idea is to be able to measure the performance characteristics not to secure the cluster that is benchmarked.