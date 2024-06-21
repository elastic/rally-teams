This directory contains the keystore configuration and configuration template for the `apm-tracing` mixin to enable APM Tracing.

## Parameters

This configuration allows to set the following parameters with Rally using `--car-params` in combination
with `--cars="defaults,apm-tracing"`:

- `apm_secret_token`: A string specifying the APM Tracing secretToken in order to properly send telemetry
- `apm_tracing_server_url`: A string specifying the APM Tracing server to send telemetry data to.

Example:

`--car="defaults,apm-tracing" --car-params="apm_secret_token:XXXXX,apm_tracing_server_url:'https://example.com:443'"`

Alternatively, the above settings can also be stored in a JSON file that can be specified via `--car-params`.

Example:

```json
{
  "apm_secret_token": "XXXXX",
  "apm_tracing_server_url": "https://example.com:443"
}
```

Save it as `params.json` and provide it to Rally with `--car="defaults,apm-tracing" --car-params="/path/to/params.json"`.
