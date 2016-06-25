#!/usr/bin/env bash
set -e

# Given a list of images as input...
IMAGES=("$@")

# Parse the Alpine version from the curl Dockerfile
BASE_IMAGE="$(awk '$1 == "FROM" { print $2; exit }' curl/Dockerfile)"
ALPINE_VERSION="${BASE_IMAGE##*:}"

docker login -u "$REGISTRY_USER" -p "$REGISTRY_PASS"

for image in "${IMAGES[@]}"; do
  tag="${image##*:}"
  if [[ "$tag" != "latest" ]]; then
    version_tag="$ALPINE_VERSION-$tag"
  else
    version_tag="$ALPINE_VERSION"
  fi

  docker-ci-deploy --tag "$tag" "$version_tag" -- "$image"
done
