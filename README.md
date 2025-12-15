# rally-teams

This repository contains the default teams for the Elasticsearch benchmarking tool [Rally](https://github.com/elastic/rally).

Currently it consists only of individual "cars", which describe the configuration of a single Elasticsearch node in Rally.

> [!NOTE]
> You should not need to use this repository directly, except if you want to look under the hood or create your own teams.

# Versioning Scheme

Refer to the official [Rally docs](https://esrally.readthedocs.io/en/stable/track.html#custom-track-repositories) for more details.

# How to Contribute

If you want to contribute a car, please ensure that it works against the master version of Elasticsearch (i.e. submit PRs against the master branch). We can then check whether it's feasible to backport the car to earlier Elasticsearch versions.

> [!NOTE]
> See all details in the [contributor guidelines](https://github.com/elastic/rally/blob/master/CONTRIBUTING.md).

# Backporting changes

Backporting ensures that cars do not work only for the latest `main` version of Elasticsearch but also for older versions. As part of contributing to this repository, a reminder will periodically notify you that backport is pending.

In order to backport your PR, at least one `vX.Y` label has to be added. 
- Please supply all the labels that correspond to both current and past elasticsearch versions you expect this PR to work with, but choose only from all the available ones. 
- If the PR being merged is using functionality from future Elasticsearch versions, please wait for the creation of new Elasticsearch `vX.Y` version branch. In such case, it would be useful if you kept the 'backport pending' label attached to the PR, so the backport reminder can periodically notify you.

When adding a `vX.Y` label, the creation of a new PR is triggered unless there are merge conflicts. Its status is reported through a comment and in case it is successfully created, you get a link to the PR opened against the target version branch. This new PR has a `backport` label and expects a review. When approved, it will be automatically merged.

## Merge conflicts
Merge conflicts need to be resolved manually. There are two ways to manually create a backport PR 

## Fork and cherry-pick
1. Create a rally-teams fork, and clone it locally.
2. Pull and checkout to the intended version branch. 
3. Create a new local branch from this version branch.
4. Cherry-pick the commit from the PR that will be backported.
5. Resolve merge conflicts, commit locally and push to fork.
6. Open a PR against the target branch, add `backport` label manually.
7. Request a review and merge.
8. Repeat for other version branches. 

## Use backport tool (requires node)
1. Go to the [Backport tool](https://github.com/sorenlouv/backport?tab=readme-ov-file#backport-cli-tool) documentation and follow the guidelines to install it in your local `rally-teams` directory. Note that you have to add your personal access secret token locally in `~/.backport/config.json` with the [specified](https://github.com/sorenlouv/backport/blob/main/docs/config-file-options.md#global-config-backportconfigjson) repository access. At the end of this step, you should be able to execute `backport` command inside rally-teams repo.
2. cd in your local `rally-teams` repository and execute `backport --pr <merged_pr_number>`. This will open an interactive dialog where you are required to selected branches to backport to. You can only select the version branches that have merge conflicts. After selecting the branches, backport tool will mention some directory in a message `Please fix the conflicts in /home/<user>/.backport/repositories/elastic/rally-teams` and you will have to go and resolve those conflicts manually for all of the selected branches. If it is not easy to tackle multiple branches in a single sweep, repeat this procedure for each target version branch separately.
3. After resolving the merge conflicts you can execute `backport --pr <merged_pr_number>` which this time it will be successful. PRs will be opened against the target version branches and they will be ready for approval and merge.

> [!NOTE]
> In case of conflicts, git blame is a wonderful tool to understand what changes need to be included in a version branch before backporting your PR. You can always check the history of the files you touch between the target backport branch and master version branch.

## Finish line
For wrapping up ensure the following:
- Your merged PR has all the correct version labels.
- Every related backport PR has the `backport` label.
- Every related backport PR is merged to the correct version branches.

Finally, remove the `backport pending` label from your PR.

# License

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
