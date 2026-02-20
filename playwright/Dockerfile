FROM mcr.microsoft.com/playwright:v1.58.2-noble

WORKDIR /app/playwright

# Install Playwright project dependencies.
COPY playwright/package.json playwright/package-lock.json ./
RUN npm ci

# Copy Playwright tests/config plus shared test fixtures.
COPY playwright/ ./
COPY test_data/ /app/test_data/

CMD ["npx", "playwright", "test"]
