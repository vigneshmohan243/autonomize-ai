import { test, expect } from '@playwright/test';

/**
 * UX/UI Validation – Medical Chart Upload
 * Scenario:
 * - User attempts to upload invalid or oversized medical chart
 * - System should show clear error message
 */

test.describe('Medical Chart Upload Validation', () => {

  test('should reject unsupported file format', async ({ page }) => {
    // Dummy URL for assignment
    await page.goto('http://localhost:3000/upload');

    // Upload unsupported file
    await page.setInputFiles(
      'input[type="file"]',
      '../test_data/dummy_invalid.txt'
    );

    // Expect validation message
    const errorMessage = page.locator('.error-message');

    await expect(errorMessage).toBeVisible();
    await expect(errorMessage).toContainText(/invalid file format/i);
  });


  test('should reject file exceeding allowed page limit', async ({ page }) => {
    await page.goto('http://localhost:3000/upload');

    // Upload large medical chart (dummy)
    await page.setInputFiles(
      'input[type="file"]',
      '../test_data/large_chart.pdf'
    );

    const errorMessage = page.locator('.error-message');

    await expect(errorMessage).toBeVisible();
    await expect(errorMessage).toContainText(/exceeds allowed limit/i);
  });

});
