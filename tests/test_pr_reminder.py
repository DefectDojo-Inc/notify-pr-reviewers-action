import importlib.util
import os
import unittest

_spec = importlib.util.spec_from_file_location(
    "pr_reminder", os.path.join(os.path.dirname(__file__), "..", "pr-reminder.py"))
pr_reminder = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pr_reminder)


def pull_request(title, milestone=None):
    return {
        "head": {"repo": {"name": "repo"}},
        "title": title,
        "html_url": "https://github.com/o/repo/pull/5",
        "number": 5,
        "milestone": milestone,
    }


class EscapingTest(unittest.TestCase):
    # A contributor writes the PR title and can edit it later. Slack mrkdwn would turn
    # these into a ping and a disguised link inside the bot's own link.
    HOSTILE = "Fix <!channel> see <https://evil.example|docs> & more"

    def test_pr_title_is_literal(self):
        text = pr_reminder.format_pr_message(pull_request(self.HOSTILE), [])["text"]["text"]
        self.assertNotIn("<!channel>", text)
        self.assertNotIn("<https://evil.example", text)
        self.assertEqual(
            text,
            "<https://github.com/o/repo/pull/5|repo (#5): Fix &lt;!channel&gt; see "
            "&lt;https://evil.example|docs&gt; &amp; more>",
        )

    def test_milestone_title_is_literal(self):
        milestone = {"due_on": "2026-12-01T00:00:00Z",
                     "html_url": "https://github.com/o/repo/milestone/1", "title": "1.0 <!here>"}
        text = pr_reminder.format_pr_message(pull_request("ok", milestone), [])["text"]["text"]
        self.assertNotIn("<!here>", text)
        self.assertIn("<https://github.com/o/repo/milestone/1|1.0 &lt;!here&gt;>", text)


if __name__ == "__main__":
    unittest.main()
