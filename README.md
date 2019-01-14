rally-teams
-----------

This repository contains the default teams for the Elasticsearch benchmarking tool [Rally](https://github.com/elastic/rally).

Currently it consists only of individual "cars", which describe the configuration of a single Elasticsearch node in Rally.

You should not need to use this repository directly, except if you want to look under the hood or create your own teams.

Versioning Scheme
-----------------

From time to time, settings change in Elasticsearch. As we want to be able to support multiple versions of Elasticsearch, we also need to version our team specifications. Therefore, this repository contains multiple branches. The following examples should give you an idea how the versioning scheme works:

* master: compatible with the latest development version of Elasticsearch
* 5.0.0-alpha2: compatible with the released version 5.0.0-alpha2.
* 2: compatible with all Elasticsearch releases with the major release number 2 (e.g. 2.1, 2.2, 2.2.1)
* 1.7: compatible with all Elasticsearch releases with the major release number 1 and minor release number 7 (e.g. 1.7.0, 1.7.1, 1.7.2)

As you can see, branches can match exact release numbers but Rally is also lenient in case settings did not change for a few releases. Rally will try to match in the following order:

1. major.minor.patch-extension_label (e.g. 5.0.0-alpha5)
2. major.minor.patch (e.g. 2.3.1)
3. major.minor (e.g. 2.3)
4. major (e.g. 2)

Apart from that, the master branch is always considered to be compatible with the Elasticsearch master branch.

To specify the version to check against, add `--distribution-version` when running Rally. It it is not specified, Rally assumes that you want to benchmark against the Elasticsearch master version. 

Example: If you want to benchmark Elasticsearch 5.0.0, run the following command:

```
esrally --distribution-version=5.0.0
```

How to Contribute
-----------------

If you want to contribute a car, please ensure that it works against the master version of Elasticsearch (i.e. submit PRs against the master branch). We can then check whether it's feasible to backport the car to earlier Elasticsearch versions.
 
See all details in the [contributor guidelines](https://github.com/elastic/rally/blob/master/CONTRIBUTING.md).

Backporting changes
-------------------

If you are a contributor with direct commit access to this repository then please backport your changes. This ensures that cars do not work only for the latest `master` version of Elasticsearch but also for older versions. Apply backports with cherry-picks. Below you can find a walkthrough:

Assume we've pushed commit `abc123` to master and want to backport it. This is a change to the `my_new_car` car. Let's check what branches are available for backporting:

```
daniel@io:teams/default ‹master›$ git branch -r
  origin/1
  origin/2
  origin/5
  origin/HEAD -> origin/master
  origin/master
```

We'll go backwards starting from branch `5`, then branch `2` and finally branch `1`. After applying a change, we will test whether the car works as is for an older version of Elasticsearch.

```
git checkout 5
git cherry-pick abc123

# test the change now with an Elasticsearch 5.x distribution
esrally --car=my_new_car --distribution-version=5.4.3 --test-mode

# push the change
git push origin 5
```

Continue the same steps now on the branches `2` and `1`.
 
License
-------

This software is licensed under the Apache License, version 2 ("ALv2"), quoted below.

Copyright 2017-2019 Elasticsearch <https://www.elastic.co>

Licensed under the Apache License, Version 2.0 (the "License"); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations under
the License.
