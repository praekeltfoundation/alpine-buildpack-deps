#!/usr/bin/env python
import sys
import unittest

from deploy import generate_versioned_tag, main, split_image_tag


class TestMain(unittest.TestCase):
    def test_main(self):
        main([
            'alpine-buildpack-deps:3.4-curl',
            'alpine-buildpack-deps:3.4-scm',
            'alpine-buildpack-deps:3.4-slim',
            'alpine-buildpack-deps:3.4',
            '3.4',
            '--latest',
            '--dry-run'])
        # NOTE: This requires Python 2.7+ and that the tests are run in
        # buffered mode.
        output = sys.stdout.getvalue().strip().split('\n')
        self.assertEqual(output, [
            ('docker tag alpine-buildpack-deps:3.4-curl '
                'alpine-buildpack-deps:3.4-curl'),
            ('docker tag alpine-buildpack-deps:3.4-curl '
                'alpine-buildpack-deps:curl'),
            'docker push alpine-buildpack-deps:3.4-curl',
            'docker push alpine-buildpack-deps:curl',
            ('docker tag alpine-buildpack-deps:3.4-scm '
                'alpine-buildpack-deps:3.4-scm'),
            ('docker tag alpine-buildpack-deps:3.4-scm '
                'alpine-buildpack-deps:scm'),
            'docker push alpine-buildpack-deps:3.4-scm',
            'docker push alpine-buildpack-deps:scm',
            ('docker tag alpine-buildpack-deps:3.4-slim '
                'alpine-buildpack-deps:3.4-slim'),
            ('docker tag alpine-buildpack-deps:3.4-slim '
                'alpine-buildpack-deps:slim'),
            'docker push alpine-buildpack-deps:3.4-slim',
            'docker push alpine-buildpack-deps:slim',
            'docker tag alpine-buildpack-deps:3.4 alpine-buildpack-deps:3.4',
            ('docker tag alpine-buildpack-deps:3.4 '
                'alpine-buildpack-deps:latest'),
            'docker push alpine-buildpack-deps:3.4',
            'docker push alpine-buildpack-deps:latest',
        ])


class TestSplitImageTag(unittest.TestCase):
    def test_image_tag(self):
        image, tag = split_image_tag('foo:bar')
        self.assertEqual(image, 'foo')
        self.assertEqual(tag, 'bar')

    def test_image(self):
        image, tag = split_image_tag('foo')
        self.assertEqual(image, 'foo')
        self.assertIsNone(tag)


class TestGenerateVersionedTag(unittest.TestCase):
    def test_name_tag(self):
        versioned_tags = generate_versioned_tag('foo', '5.4.1')
        self.assertEqual(versioned_tags, ['5.4.1-foo'])

    def test_version_and_name_tag(self):
        versioned_tags = generate_versioned_tag('5.4.1-foo', '5.4.1')
        self.assertEqual(versioned_tags, ['5.4.1-foo'])

    def test_other_version_tag(self):
        versioned_tags = generate_versioned_tag('2.7-foo', '5.4.1')
        self.assertEqual(versioned_tags, ['5.4.1-2.7-foo'])

    def test_none_tag(self):
        versioned_tags = generate_versioned_tag(None, '5.4.1')
        self.assertEqual(versioned_tags, ['5.4.1'])

    def test_latest(self):
        versioned_tags = generate_versioned_tag('foo', '5.4.1', latest=True)
        self.assertEqual(versioned_tags, ['5.4.1-foo', 'foo'])

    def test_latest_no_tag(self):
        versioned_tags = generate_versioned_tag(None, '5.4.1', latest=True)
        self.assertEqual(versioned_tags, ['5.4.1', 'latest'])


if __name__ == '__main__':
    unittest.main(buffer=True)
