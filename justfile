_ensure_min_just_version := `min="1.51.0"; cur="$(just --version | cut -d' ' -f2)"; if [ "$(printf '%s\n%s\n' "$min" "$cur" | sort -V | head -n1)" != "$min" ]; then echo "just $cur is too old — this justfile requires just >= $min. See https://just.systems/man/en/pre-built-binaries.html" >&2; exit 1; fi`

set dotenv-load := true # Support for .env file
PROJECT_DIR := "dbt_project"
export ACCESS_MODEL_SCHEMA := "common_access_model"
export DBT_PROJECT_DIR := join(justfile_directory(), "dbt_transforms")
export DBT_PROFILES_DIR := join(justfile_directory(), "dbt_transforms")


cam_version := "0.2.2"
cam_url     := "https://github.com/include-dcc/common-access-model/releases/download/v" + cam_version + "/common_access_model-" + cam_version + "-py3-none-any.whl"

# Basic list of commands and variable names as currently defined
help:
  @echo ----------------------------------
  @echo - Variables Defined
  @echo - CAM Version: {{cam_url}}
  @echo ----------------------------------
  @echo
  @just --list

# Install CAM wheel file, extract the test data into the right places and
# dbt's dependencies
setup:
  uv sync --upgrade-package "common_access_model @ {{cam_url}}"
  # cd dbt && uv run dbt deps

# dbt DEBUG
dbt-debug:
    uv run dbt debug
# dbt run
dbt-run:
    uv run dbt run
