import argparse
import yaml
from pathlib import Path


def load_assumptions():
    config_path = Path(__file__).resolve().parent.parent / "config" / "assumptions.yml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="Run MI report")
    parser.add_argument("--week", required=True, help="Week format: YYYY-MM-DD_to_YYYY-MM-DD")
    args = parser.parse_args()

    assumptions = load_assumptions()

    print("=" * 50)
    print("MI REPORT")
    print("=" * 50)
    print(f"Week: {args.week}")
    print("\nAssumptions Loaded:")
    print(f"  Maintenance per mile: ${assumptions['maint_per_mile']}")
    print(f"  Trailer speed (mph): {assumptions['trailer_speed_mph']}")
    print(f"  Box route hours: {assumptions['box_route_hours']}")
    print("  Yard hours paid:")
    for yard, hours in assumptions["yard_hours_paid"].items():
        print(f"    {yard}: {hours}")
    print("\nStatus: MI skeleton running successfully.")
    print("=" * 50)


if __name__ == "__main__":
    main()