#!/usr/bin/env python
from __future__ import print_function

import argparse
import sys
import subprocess


def main(raw_args=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description='Tag Docker images with a version and push the tags')
    parser.add_argument(
        'image_tags', nargs='+', help='the Docker image to (re-)tag and push')
    parser.add_argument(
        'version', help='the full version to tag the image with')
    parser.add_argument(
        '-l', '--latest', action='store_true',
        help='tag and push this image with an unversioned tag to make it the '
             'latest default release')
    parser.add_argument(
        '-d', '--dry-run', action='store_true',
        help="don't execute any Docker commands, just print them")

    args = parser.parse_args(raw_args)
    image_tags, version, dry_run = args.image_tags, args.version, args.dry_run

    for image_tag in image_tags:
        image, tag = split_image_tag(image_tag)

        # Generate all the tags
        versioned_tags = generate_versioned_tag(tag, version, args.latest)
        versioned_image_tags = (
            [':'.join((image, vtag)) for vtag in versioned_tags])

        # Tag the image with all the tags
        for versioned_image_tag in versioned_image_tags:
            cmd('docker', 'tag', image_tag, versioned_image_tag,
                dry_run=dry_run)

        # Push all the tags
        for versioned_image_tag in versioned_image_tags:
            cmd('docker', 'push', versioned_image_tag, dry_run=dry_run)


def split_image_tag(image_tag):
    """ Split an image tag into its name and tag parts (<name>[:<tag>]). """
    image_tag_parts = image_tag.split(':', 1)
    image = image_tag_parts[0]
    tag = image_tag_parts[1] if len(image_tag_parts) == 2 else None
    return image, tag


def generate_versioned_tag(tag, version, latest=False):
    """
    Generate tags with version information from the given version. Appends the
    version to the given tag if the version is not already present.
    e.g. 'foo', '5.4.1'       => ['5.4.1-foo']
         '5.4.1-foo', '5.4.1' => ['5.4.1-foo']
         '2.7-foo', '5.4.1'   => ['5.4.1-2.7-foo']
         None, '5.4.1'        => ['5.4.1']
         'foo', '5.4.1', True => ['5.4.1-foo', 'foo']
         None, '5.4.1', True  => ['5.4.1', 'latest']

    :param latest:
        Whether to return the unversioned tag (or 'latest' tag) as well as the
        versioned tags.
    """
    if tag is None:
        # No existing tag, just tag with the version
        return [version, 'latest'] if latest else [version]

    unversioned_tag = get_unversioned_tag(tag, version)
    if not unversioned_tag:
        # No part of existing tag is not the version, just tag with the version
        return [version, 'latest'] if latest else [version]

    versioned_tag = '-'.join((version, unversioned_tag))
    return [versioned_tag, unversioned_tag] if latest else [versioned_tag]


def get_unversioned_tag(tag, version):
    """
    Trim the version from the start of the given tag if the given version is
    present.
    """
    if tag == version:
        return ''
    if tag.startswith(version + '-'):
        return tag[len(version) + 1:]

    return tag


def cmd(*args, **kwargs):
    if kwargs.get('dry_run', False):
        print(*args)
        return
    subprocess.check_call(args)


if __name__ == '__main__':  # pragma: no cover
    main()
