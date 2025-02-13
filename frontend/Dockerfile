# Use Node 18 for the frontend
FROM node:18-alpine

# Create and set the working directory
WORKDIR /app

# Copy package.json first
COPY package*.json ./

# Install dependencies
RUN npm install
RUN npm install -g @quasar/cli

# Create Quasar project non-interactively
RUN quasar create . -- --branch next --type=spa --pkg-manager=npm --typescript=false --eslint=false --pinia=false --force

# Copy your application code
COPY . .

# Build the production-ready files (optional - if you want a production image)
# RUN npm run build

# Expose the frontend port (often 8080 if using Vue CLI)
EXPOSE 8080

# Default command to run the dev server
CMD ["npm", "run", "serve"]
