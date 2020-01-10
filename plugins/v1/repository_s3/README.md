This directory contains the (optional) keystore configuration for the `repository-s3` plugin.
For more details on secure settings for the repository-s3 plugin please refer to the [repository-s3-client](https://www.elastic.co/guide/en/elasticsearch/plugins/7.5/repository-s3-client.html) documentation.

### Parameters

This configuration allows to set the following parameters with Rally using `--plugin-params` in combination with `--elasticsearch-plugins="repository-s3"`:

* `aws_access_key`: A string specifying the AWS access key (mandatory)
* `aws_secret_key`: A string specifying the AWS secret key (mandatory)
* `aws_session_token`: A string specifying the AWS session token (optional)

Example:

`--elasticsearch-plugins="repository-gcs" --plugin-params="aws_access_key:XXXXX,aws_aws_secret_key:YYYYY,aws_session_token:ZZZZZ"`

The above settings can also be stored in a JSON file that can be specified as well with `--plugin-params`.

Example:

```json
{
  "aws_access_key": "XXXXX",
  "aws_secret_key": "YYYYY",
  "aws_session_token": "ZZZZZ"
}
```   

Save it as `params.json` and provide it to Rally with `--elasticsearch-plugins="repository-s3" --plugin-params="/path/to/params.json"`.
