import logging
import os
import shlex
import subprocess

from esrally import exceptions
from esrally.utils import process

LOGGER_NAME = "esrally.provisioner.apm_tracing"


def resolve_binary(install_root, binary_name):
    return os.path.join(install_root, "bin", binary_name)


def resolve_keystore_config(install_root):
    return os.path.join(install_root, "config", "elasticsearch.keystore")


def create_keystore(install_root, keystore_binary, env):
    logger = logging.getLogger(LOGGER_NAME)

    keystore_create_command = "{keystore} -s create".format(keystore=keystore_binary)

    return_code = process.run_subprocess_with_logging(keystore_create_command, env=env)

    if return_code != 0:
        logger.error(
            "%s has exited with code [%d]", keystore_create_command, return_code
        )
        raise exceptions.SystemSetupError(
            "Could not initialize a keystore. Please see the log for details."
        )


def add_property_to_keystore(keystore_binary, property_name, property_value, env):
    logger = logging.getLogger(LOGGER_NAME)

    echo_value = subprocess.Popen(["echo", property_value], stdout=subprocess.PIPE)

    keystore_command = "{keystore} --silent add --stdin {key}".format(
        keystore=keystore_binary, key=property_name
    )

    return_code = process.run_subprocess_with_logging(
        keystore_command, stdin=echo_value.stdout, env=env
    )

    if return_code != 0:
        logger.error("%s has exited with code [%d]", keystore_command, return_code)
        raise exceptions.SystemSetupError(
            "Could not add S3 keystore secure setting [{}]. Please see the log for details.".format(
                property_name
            )
        )


def configure_keystore(config_names, variables, **kwargs):
    logger = logging.getLogger(LOGGER_NAME)
    secret_token = variables.get("apm_secret_token")

    # skip keystore configuration entirely if any of the mandatory params is missing
    if not secret_token:
        logger.warning(
            "Skipping keystore configuration for apm-tracing "
            "as mandatory plugin-params [`apm_secret_token`] was not supplied",
        )
        return False

    keystore_binary_filename = "elasticsearch-keystore"
    install_root = variables["install_root_path"]
    keystore_binary = resolve_binary(install_root, keystore_binary_filename)
    env = kwargs.get("env")

    if not os.path.isfile(resolve_keystore_config(install_root)):
        create_keystore(install_root, keystore_binary, env)

    add_property_to_keystore(keystore_binary, "telemetry.secret_token", secret_token, env)

    # Success
    return True


def register(registry):
    registry.register("post_install", configure_keystore)
