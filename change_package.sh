#!/bin/bash
NEW_PACKAGE=$1
if [ -z "$NEW_PACKAGE" ]; then
  echo "Usage: ./change_package.sh com.new.package"
  exit 1
fi
sed -i "s/\"appId\": \".*\"/\"appId\": \"$NEW_PACKAGE\"/g" capacitor.config.json
sed -i "s/applicationId \".*\"/applicationId \"$NEW_PACKAGE\"/g" android/app/build.gradle
sed -i "s/namespace \".*\"/namespace \"$NEW_PACKAGE\"/g" android/app/build.gradle
echo "Package changed to $NEW_PACKAGE!"
