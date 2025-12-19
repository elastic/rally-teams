# rally-teams

This repository contains the default teams for the Elasticsearch benchmarking tool [Rally](https://github.com/elastic/rally).

Currently it consists only of individual "cars", which describe the configuration of a single Elasticsearch node in Rally.

> [!NOTE]
> Direct interaction with this repository is only necessary for inspecting its internals or for creating custom teams.

# Versioning Scheme

Refer to the official [Rally docs](https://esrally.readthedocs.io/en/stable/track.html#custom-track-repositories) for more details.

# How to Contribute

Contributions of new cars should be compatible with the `main` version of Elasticsearch (i.e., pull requests should be submitted against the `rally-teams` master branch). Feasibility of backporting to earlier Elasticsearch versions will be evaluated after submission.

> [!NOTE]
> For complete details, refer to the [contributor guidelines](https://github.com/elastic/rally/blob/master/CONTRIBUTING.md).

# Backporting changes

Backporting ensures compatibility of cars with both the latest main version of Elasticsearch and older versions. Periodic reminders will be issued when a backport is pending as part of the contribution process.

To initiate backporting of a pull request, at least one `vX.Y` label must be applied.
- Please supply all the labels that correspond to next, current and past elasticsearch versions expected to work with this PR, but select only from the available ones.
- If the PR being merged is using functionality from future Elasticsearch versions, please wait for the creation of Elasticsearch `vX.Y` version branch.

When a `vX.Y` label is added, a new pull request is automatically created, unless merge conflicts are detected or if the label supplied points to the next Elasticsearch minor version. The status of this process is reported via a comment, and if successful, a link to the newly opened pull request targeting the specified version branch is provided. This pull request will include a backport label and will require a review. Upon approval, it will be merged automatically.

## Merge conflicts
Merge conflicts must be resolved manually. There are two primary methods for manually creating a backport pull request:

### Fork and cherry-pick
1. Fork the rally-teams repository and clone it locally.
2. Pull and check out the intended version branch.
3. Create a new local branch from the selected version branch.
4. Cherry-pick the commit from the pull request to be backported.
5. Resolve any merge conflicts, commit the changes locally, and push to the fork.
6. Open a pull request against the target branch and manually add the backport label.
7. Request a review and proceed with merging.
8. Repeat this process for additional version branches as needed.

### Use backport tool (requires Node.js)
1. Refer to the [Backport tool](https://github.com/sorenlouv/backport?tab=readme-ov-file#backport-cli-tool) for installation instructions in the local rally-teams directory. Ensure that a personal access token is configured in `~/.backport/config.json` with the required [repository access](https://github.com/sorenlouv/backport/blob/main/docs/config-file-options.md#global-config-backportconfigjson). Upon completion, the `backport` command should be available within the rally-teams repository.
2. Navigate to the local `rally-teams` repository and execute `backport --pr <merged_pr_number>`. This command initiates an interactive dialog for selecting branches to backport to. Only version branches with merge conflicts can be selected. After branch selection, the tool will indicate a directory (e.g., `Please fix the conflicts in /home/<user>/.backport/repositories/elastic/rally-teams`) where conflicts must be resolved manually for each selected branch. If resolving multiple branches simultaneously is not feasible, repeat the procedure for each target version branch individually.
3. Once merge conflicts are resolved, re-execute `backport --pr <merged_pr_number>`. The process should now complete successfully, and pull requests will be opened against the target version branches, ready for review and merging.

> [!NOTE]
> In the event of conflicts, git blame is a useful tool for identifying changes that must be included in a version branch prior to backporting. The history of modified files can be compared between the target backport branch and the master branch.

## Final steps
To complete the process, ensure the following:

- The merged pull request includes all relevant version labels.
- Each associated backport pull request is labeled with backport.
- Each backport pull request is merged into the appropriate version branch.

Finally, remove the `backport pending` label.

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
