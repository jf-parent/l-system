#! /usr/bin/env bash

echo "Name of the system:"
read name

cat <<EOF > systems/${name}.py
rules = [
    "{CHANGEME}->{CHANGEME}",
    "{CHANGEME}->{CHANGEME}"
]
axiom = "w={CHANGEME}"
iterations = {CHANGEME}
segment_length = {CHANGEME}
alpha_zero = {CHANGEME}
angle = {CHANGEME}
EOF
