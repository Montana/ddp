DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=$(realpath ${DIR}/../src):$PYTHONPATH
export DJANGO_SETTINGS_MODULE=project.settings
