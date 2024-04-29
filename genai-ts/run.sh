#!/bin/bash

# Install dependencies
npm install

# Build the project
npm run build

# Start the server in the background
npm run start &
