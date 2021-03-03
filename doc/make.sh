#!/usr/bin/env sh

set -e

cd $(dirname "$0")

asciidoctor index.adoc
