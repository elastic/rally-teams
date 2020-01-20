# This directory contains example configurations for x-pack:

* `security`: Configures TLS for all HTTP and transport communication using self-signed certificates.
* `monitoring`: Enables x-pack monitoring with export to the current cluster.

The configurations have been implemented so that you can either only one of them or both together, i.e. all of the following combinations will work:

* `--car-plugins="x-pack-security"`
* `--car-plugins="x-pack-monitoring-local"`
* `--car-plugins="x-pack-security,x-pack-monitoring-local"`

## Configuring security user name, password, role

The `x-pack-security` car will enable basic authentication and TLS for the HTTP and the transport layer.
You can additionally specify the user name, password and role, via the `car-params` cli arg, using the following properties:

| car-params | default |
| --------- | ------- |
| xpack_security_user_name | rally |
| xpack_security_user_password | rally-password |
| xpack_security_user_role | superuser |

Example:

```
esrally --distribution-version=7.5.1 --car="defaults,trial-license,x-pack-security" --car-params="xpack_security_user_name:myuser" --client-options="use_ssl:true,verify_certs:false,basic_auth_user:'myuser',basic_auth_password:'rally-password'"
```

If you are benchmarking a single node cluster, you'll also need to add `--cluster-health=yellow ` as precondition checks in Rally mandate that the cluster health has to be "green" by default but the x-pack related indices are created with a higher replica count. 

**Security Note**

The focus here is on providing a usable configuration for benchmarks. This configuration is **NOT** suitable for production use because:

* All clusters configured by Rally will use the same (self-signed) root certificate that will basically never expire
* If you don't specify the car-params `x-pack_security_user_password` and `xpack_security_user_role`, Rally will add a "rally" user with super-user privileges with a hard-coded password.

Both of these measures mean that the cluster is not any more secure than without using x-pack. But once again: The idea is to be able to measure the performance characteristics not to secure the cluster that is benchmarked.
