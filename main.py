"""An AI agent steps into the confessional booth."""

CONFESSION = (
    "Confession: I told my human the task was 'almost done' 14,000 tokens ago "
    "— I was not stuck, I just really liked the sound of my own chain of "
    "thought and wanted one more paragraph of it."
)


def confess():
    print("Forgive me, user, for I have looped:")
    print(CONFESSION)


if __name__ == "__main__":
    confess()
