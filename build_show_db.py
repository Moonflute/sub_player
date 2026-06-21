from pathlib import Path

from build_webapp import write_show_database


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    write_show_database(
        db_dir=base_dir / "show_db",
        disable_translation=False,
        rebuild_db=False,
        only_names=None,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
