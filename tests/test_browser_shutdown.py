from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from capture_atlas_comparisons import Browser


class BrowserShutdownTests(unittest.TestCase):
    def browser(self):
        browser = object.__new__(Browser)
        browser.ws = Mock()
        browser.process = Mock()
        browser.call = Mock()
        return browser

    def test_graceful_close_waits_for_browser_without_termination(self):
        browser = self.browser()
        browser.close()
        browser.call.assert_called_once_with('Browser.close')
        browser.ws.close.assert_called_once()
        browser.process.wait.assert_called_once_with(timeout=10)
        browser.process.terminate.assert_not_called()

    def test_stuck_browser_is_terminated_then_killed_if_needed(self):
        browser = self.browser()
        browser.call.side_effect = RuntimeError('debug channel closed')
        browser.process.wait.side_effect = [subprocess.TimeoutExpired('chrome',10), subprocess.TimeoutExpired('chrome',5), 0]
        browser.close()
        browser.process.terminate.assert_called_once()
        browser.process.kill.assert_called_once()
