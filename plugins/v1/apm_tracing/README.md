This directory contains the (optional) keystore configuration for the `repository-s3` plugin.
For more details on secure settings for the repository-s3 plugin please refer to the [repository-s3-client](https://www.elastic.co/guide/en/elasticsearch/plugins/current/repository-s3-client.html) documentation.

### Parameters

This plugin allows to set the following parameters with Rally using `--plugin-params` in combination with `--elasticsearch-plugins="repository-s3"`:

* `apm_secret_token`: A string specifying the APM Tracing secretToken in order to properly send telemetry

Example:

`--elasticsearch-plugins="apm-tracing" --plugin-params="amp_secret_token:XXXXX"`

Alternatively, the above settings can also be stored in a JSON file that can be specified via `--plugin-params`.

Example:

```json
{
  "apm_secret_token": "XXXXX",
}
```   

Save it as `params.json` and provide it to Rally with `--elasticsearch-plugins="repository-s3" --plugin-params="/path/to/params.json"`.
